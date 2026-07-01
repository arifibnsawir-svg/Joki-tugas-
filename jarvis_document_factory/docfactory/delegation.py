"""Optional sub-agent delegation for large multi-step jobs.

The Router decides whether delegation is worth the cost. When it is, the
Orchestrator hands each Worker a self-contained brief with explicit PASS or FAIL
criteria, and accepts a returned result only if it satisfies those PASS criteria.
Small jobs are executed directly rather than delegated. This brief-level gate is
consistent with the global rule that a deterministic check, not the model,
declares work acceptable.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class WorkerBrief:
    subtask_id: str
    context: str                      # self-contained context for the worker
    pass_criteria: list[str]          # explicit PASS criteria
    fail_criteria: list[str] = field(default_factory=list)

    def is_complete(self) -> bool:
        """A brief is complete iff it has self-contained context and explicit
        PASS criteria (Requirement 10.2)."""
        return bool(self.context.strip()) and len(self.pass_criteria) > 0


@dataclass(frozen=True)
class WorkerResult:
    subtask_id: str
    satisfied_criteria: list[str]     # which PASS criteria the result met
    artifact_path: str = ""


def make_brief(subtask_id: str, context: str, pass_criteria, fail_criteria=None) -> WorkerBrief:
    return WorkerBrief(
        subtask_id=subtask_id,
        context=context,
        pass_criteria=list(pass_criteria),
        fail_criteria=list(fail_criteria or []),
    )


def brief_for_section(spec, section) -> WorkerBrief:
    """Build a self-contained brief to render one section as a delegated subtask."""
    context = (
        "Document: %s. Render section %r (%s) titled %r using the shared SPEC "
        "renderers. Read content only from the SPEC and verified paths."
        % (spec.identity.title, section.id, section.kind, section.title)
    )
    pass_criteria = [
        "output file exists",
        "gate returns PASS for the section",
        "text is humanizer clean",
    ]
    fail_criteria = ["missing file", "gate FAIL", "hallucinated image or citation"]
    return make_brief(section.id, context, pass_criteria, fail_criteria)


def accept_worker_result(brief: WorkerBrief, result: WorkerResult) -> bool:
    """Accept the result iff it satisfies every PASS criterion in the brief."""
    return set(brief.pass_criteria).issubset(set(result.satisfied_criteria))
