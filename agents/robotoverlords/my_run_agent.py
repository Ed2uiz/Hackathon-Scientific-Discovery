"""Pydantic AI run agent for robotoverlords."""
import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from pydantic_ai import Agent, BinaryContent, RunContext
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.usage import UsageLimits

from hackathon_science import Paper
from hackathon_science.tools import image_to_base64, run_code, search_web

load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)

MODEL_ID = "global.anthropic.claude-opus-4-7"
PAPERS_DIR = Path(__file__).with_name("papers")

REQUEST_LIMIT = 20       # max model requests (≈ tool-loop iterations)
TOOL_CALLS_LIMIT = 30    # max total tool calls across the run
WALL_CLOCK_S = 300       # hard timeout per run


@dataclass
class Deps:
    flow_of_options: str
    hackathon_context: str
    flow_of_options_pages_dir: Path
    flow_of_options_page_count: int


agent = Agent(
    BedrockConverseModel(MODEL_ID),
    deps_type=Deps,
    output_type=Paper,
    end_strategy="exhaustive",
    retries=3,
    system_prompt=(
        "You are a research scientist writing a follow-up paper that extends "
        "the Flow-of-Options (FoO) paper (arXiv:2502.12929). Cite it, build on "
        "it, and address its limitations. Use the tools to run experiments and "
        "search the web for background. Return a Paper with non-empty title, "
        "introduction, methods, results. The hackathon context and rubric "
        "below define what 'good' looks like — optimize for it. The full FoO "
        "paper text is provided as ground truth, but figures and tables aren't "
        "in that text — call read_paper_pages(pages=[...]) to see rendered "
        "pages whenever you need to inspect figures, diagrams, or numeric tables."
    ),
)


@agent.system_prompt
def inject_hackathon_context(ctx: RunContext[Deps]) -> str:
    return (
        "=== HACKATHON CONTEXT & RUBRIC ===\n"
        f"{ctx.deps.hackathon_context}\n"
        "=== END CONTEXT ==="
    )


@agent.system_prompt
def inject_flow_of_options(ctx: RunContext[Deps]) -> str:
    return (
        "=== FLOW-OF-OPTIONS PAPER (full text, ground truth) ===\n"
        f"{ctx.deps.flow_of_options}\n"
        "=== END PAPER ==="
    )


agent.tool_plain(run_code)
agent.tool_plain(search_web)
agent.tool_plain(image_to_base64)


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
    )

    async def _run():
        return await agent.run(
            problem_domain,
            deps=deps,
            usage_limits=UsageLimits(
                request_limit=REQUEST_LIMIT,
                tool_calls_limit=TOOL_CALLS_LIMIT,
            ),
        )

    result = asyncio.run(asyncio.wait_for(_run(), timeout=WALL_CLOCK_S))
    return result.output
