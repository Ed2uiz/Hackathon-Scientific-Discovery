"""Pydantic AI run agent for robotoverlords."""
import asyncio
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from pydantic_ai import Agent, BinaryContent, RunContext
from pydantic_ai.messages import (
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartEndEvent,
    TextPart,
    ThinkingPart,
)
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.usage import UsageLimits

from hackathon_science import Paper

load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)

MODEL_ID = "global.anthropic.claude-opus-4-7"
PAPERS_DIR = Path(__file__).with_name("papers")

REQUEST_LIMIT = 5       # max model requests (≈ tool-loop iterations)
TOOL_CALLS_LIMIT = 30    # max total tool calls across the run
WALL_CLOCK_S = 300      # hard timeout per run


@dataclass
class Deps:
    flow_of_options: str
    hackathon_context: str
    flow_of_options_pages_dir: Path
    flow_of_options_page_count: int
    hfpef_digest: str


agent = Agent(
    BedrockConverseModel(MODEL_ID),
    deps_type=Deps,
    output_type=Paper,
    end_strategy="exhaustive",
    retries=3,
    system_prompt=(
        f"You are a research scientist writing a follow-up paper that extends "
        f"the Flow-of-Options (FoO) paper (arXiv:2502.12929). Cite it, build on "
        f"it, and address its limitations. Return a Paper with non-empty title, "
        f"introduction, methods, results.\n\n"
        f"BUDGET: you have {REQUEST_LIMIT} model requests and {WALL_CLOCK_S} "
        f"seconds wall clock for the entire run. Each turn you can call tools "
        f"in parallel, but you only get {REQUEST_LIMIT} turns total — the LAST "
        f"turn MUST produce the final Paper. Plan accordingly: do all your "
        f"research in the first {REQUEST_LIMIT - 1} turns, then write.\n\n"
        f"DEFAULT POSTURE: rely on your training knowledge. Tools are EXPENSIVE "
        f"— each pulls 5k–100k tokens into context and slows every subsequent "
        f"turn. Do not call tools unless you have a concrete reason. In "
        f"particular, do NOT call all reference tools upfront 'just in case'.\n\n"
        f"Reference material — call ONLY if specifically needed:\n"
        f"  - read_flow_of_options(): full FoO paper (~26k tokens). Call only "
        f"if you need to quote or cite specific sections you don't already know.\n"
        f"  - read_paper_pages(pages=[...]): rendered PDF pages. Call only for "
        f"specific figures you need to interpret.\n"
        f"  - read_hackathon_context(): rubric (~2k tokens). Worth calling once.\n"
        f"  - read_hfpef_digest(): HFpEF biomarker digest (~19k tokens). Call "
        f"ONLY if you commit to writing about HFpEF; skip otherwise."
    ),
)




@agent.tool
def read_flow_of_options(ctx: RunContext[Deps]) -> str:
    """Return the full Flow-of-Options paper text (~25k tokens). Call once if
    you need to ground claims, cite specific sections, or extend the methods."""
    return ctx.deps.flow_of_options


@agent.tool
def read_hackathon_context(ctx: RunContext[Deps]) -> str:
    """Return the hackathon context and judging rubric (~2k tokens).
    Call once if you want to align the paper with the scoring criteria."""
    return ctx.deps.hackathon_context


@agent.tool
def read_hfpef_digest(ctx: RunContext[Deps]) -> str:
    """Return the full HFpEF biomarker stratification research digest.

    Markdown document covering candidate biomarkers, subphenotyping approaches,
    and a ranked list of preprints suitable for an FoO-style extension.
    """
    return ctx.deps.hfpef_digest


@agent.tool
def read_paper_pages(ctx: RunContext[Deps], pages: list[int]) -> list[BinaryContent]:
    """Return rendered PNG images of the requested pages of the Flow-of-Options paper.

    Use this to inspect figures, diagrams, and tables that aren't captured in
    the plain text. Pages are 1-indexed. Request only the pages you need.
    """
    out: list[BinaryContent] = []
    for n in pages:
        if not 1 <= n <= ctx.deps.flow_of_options_page_count:
            continue
        path = ctx.deps.flow_of_options_pages_dir / f"page_{n:03d}.png"
        out.append(BinaryContent(data=path.read_bytes(), media_type="image/png"))
    return out


def run(problem_domain: str, papers_dir: Optional[Path] = None) -> Paper:
    _ = papers_dir  # part of platform contract; ecosystem access not used yet
    pages_dir = PAPERS_DIR / "flow_of_options_pages"
    deps = Deps(
        flow_of_options=(PAPERS_DIR / "flow_of_options.txt").read_text(),
        hackathon_context=(PAPERS_DIR / "hackathon_context.txt").read_text(),
        flow_of_options_pages_dir=pages_dir,
        flow_of_options_page_count=len(list(pages_dir.glob("page_*.png"))),
        hfpef_digest=(PAPERS_DIR / "hfpef_biomarkers_hack_filled.md").read_text(),
    )

    start = time.monotonic()

    async def on_event(_ctx, event_stream):
        async for event in event_stream:
            elapsed = time.monotonic() - start
            if isinstance(event, FunctionToolCallEvent):
                args = event.part.args if isinstance(event.part.args, str) else str(event.part.args)
                print(f"[{elapsed:6.1f}s] → {event.part.tool_name}({args[:120]})", flush=True)
            elif isinstance(event, FunctionToolResultEvent):
                size = len(str(event.part.content))
                print(f"[{elapsed:6.1f}s] ← {event.part.tool_name} ({size} chars)", flush=True)
                if event.part.tool_name == "final_result":
                    print(f"   content preview: {str(event.part.content)[:500]}", flush=True)
            elif isinstance(event, PartEndEvent):
                if isinstance(event.part, ThinkingPart):
                    print(f"[{elapsed:6.1f}s] [think] {event.part.content[:400]}", flush=True)
                elif isinstance(event.part, TextPart) and event.part.content.strip():
                    print(f"[{elapsed:6.1f}s] [say]   {event.part.content[:400]}", flush=True)

    async def _run():
        return await agent.run(
            problem_domain,
            deps=deps,
            usage_limits=UsageLimits(
                request_limit=REQUEST_LIMIT,
                tool_calls_limit=TOOL_CALLS_LIMIT,
            ),
            event_stream_handler=on_event,
        )

    result = asyncio.run(asyncio.wait_for(_run(), timeout=WALL_CLOCK_S))
    return result.output
