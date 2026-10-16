---
name: deep-research
description: Plans and conducts new evidence investigations to find and evaluate additional sources, competing explanations, or missing evidence for practical judgments. Use for 심층 리서치, 문헌 탐색, 연구 근거 검증. Routine fact lookups and comparisons confined to supplied or specified sources use project rules or faithful-synthesis.
---

# Deep research

Follow the project GEMINI.md for reply language, register, interpretation of user words, and presentation. This skill supplies research procedures; it does not relax the prose-format requirements.

Use the shared routing criteria in GEMINI.md. Read this workflow before framing or searching for a new evidence investigation. If findings need substantive interpretation, comparison, or a source-based report, read faithful-synthesis before that phase. For a planning-only request, prepare the plan and stop before searching or drafting findings. Skill discovery and reading are distinct from execution: perform the relevant steps, and report only checks actually completed.

Produce an answer whose conclusions can be traced to evidence and whose limits the reader can understand. Depth is resolving important uncertainties, not accumulating pages, queries, or agents.

## Frame and choose the effort
Identify the user's purpose, audience, deliverables, boundaries, and any stage gate. Ask only material questions that cannot reasonably be inferred. Choose exploratory mapping when concepts and possible explanations are unsettled; choose comparative or systematic searching when the question and selection criteria are defined. Do not label an exploratory web search a systematic review.

For sustained multi-stage investigations create a fresh, descriptive run directory under `research/`. Read [record-contract.md](references/record-contract.md) for the compact record format. Maintain `brief.md`, `evidence.json`, `report.md`, and `audit.md`; use these to resume without asking the user to repeat context. Record factual decisions, evidence, and concise reasons needed to resume the work. Ordinary or single-turn investigations must keep the equivalent reasoning and sources in the response without creating disk files, and any temporary scratch files must be removed before finishing.

## Explore, then narrow
Start with concepts and plausible alternative explanations, not a conclusion to defend. Use overviews to identify terminology and original evidence. Broaden vocabulary, disciplines, languages, dates, and source types when the question warrants it. Search for disconfirming evidence, limitations, and relevant null or failure results. Follow useful citations in both directions where tools allow. Record important queries and why a new search is needed; do not impose a fixed source quota.

Select evidence by fit to the claim, methods, transparency, independence, and relevance. Original studies and technical documents establish what was done; reviews help characterize a field. Vendor documents establish documented behavior, not independent effectiveness. Deduplicate common underlying studies. Never manufacture agreement from repetitions or give weak claims equal weight merely to appear balanced.

Read the passage supporting a decisive claim and nearby definitions, qualifications, and objections. Record the source locator and original excerpt or faithful note. A search snippet alone is provisional. For inaccessible sources record limited access and pursue another route; do not silently fill gaps.

## Synthesize and revise the question
Group evidence by the questions it answers. Identify where findings genuinely disagree and whether definitions, populations, methods, or assumptions explain the disagreement. Keep contradictions open when evidence does not resolve them. A counterargument also needs evidence and may be defeated by another stated premise.

Track the consequential uncertainty: what further evidence could change the answer? Direct follow-up searches there. Revisit the framing if the literature exposes a mistaken premise or a missing distinction. Use `faithful-synthesis` for the report; do not hand it a stack of source blurbs without their relationships.

## Finish proportionately

Before writing a sustained report, save a short `outline.md` organized around the user's question and necessary logical links. Link major sections to decisive evidence and open issues. Update the outline when evidence changes the framing. Preserve original passages and nearby conditions; downstream summaries are navigation aids, not substitute sources.

For substantial reports with consequential conclusions, use `evidence-reviewer` when supported and useful for checking decisive evidence. Supply the exact current request, stage limits, `report.md`, `evidence.json`, and relevant original passages or local source files with locators. The reviewer does not inherit the conversation: 'review the current harness' is insufficient. Use the existing workspace and read-only reviewer. Do not send credentials or unrelated private files.

Save actual returned findings in `review.md`, distinguishing demonstrated mismatches from unresolved checks. Compare findings to originals before editing; the reviewer may invent a flaw or miss a premise. Record adopted changes and rejected findings with source-based reasons in `audit.md`. If delegation is unavailable or outside the user's budget, record that and perform a focused manual comparison. Never invent reviewer results. Continue targeted review and revision while an unresolved issue could change the answer and the user's budget permits. Stop repeating a check that yields no new evidence; no fixed editorial pass limit applies.
Stop when important questions have an evidence-backed answer or explicit unresolved status, the strongest relevant challenges have been considered, and further searches have diminishing value within the user's budget. This is a judgment, not a guaranteed exhaustive-search test. If a budget or tool limit ends work earlier, deliver a useful provisional answer and describe the actual coverage gap.

Before delivery run `python3 -B .agents/skills/deep-research/scripts/check_records.py research/<run>` or `python -B .agents/skills/deep-research/scripts/check_records.py research/<run>` from the project root for a sustained run. Resolve structural errors; review warnings in context. The script checks record integrity only. It cannot establish truth, source independence, citation entailment, or logical quality. Read the sources to perform those checks and record the observed results in `audit.md`. If execution is unavailable, perform equivalent manual checks and say the automated check was not run.

Review wording in context rather than maintaining a banned-word list. Check whether your own stronger interpretation is warranted. Do not turn evidence gaps into categorical negative conclusions or mark a generated audit independently verified. Link project files with real paths or relative project links rather than invented file URL line fragments.

Deliver findings and their reasons in the reply language and register specified by GEMINI.md, with adjacent sources. Show important limits in the main prose. Link detailed evidence only when useful; do not bury the requested explanation behind files. End with the answer to the actual question rather than a ceremonial checklist.
