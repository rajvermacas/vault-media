---
name: wiki-capture-publish
description: Capture the current discussion or supplied source material as immutable raw Markdown, deduplicate it against the existing raw and maintained wiki, ingest only novel durable claims, lint the Obsidian vault, and commit and push the focused changes. Use when the user asks to dump a conversation into this vault, capture and ingest notes, maintain the wiki after a discussion, or run the complete raw-to-published workflow.
---

# Wiki Capture & Publish

## Overview

Run the vault's complete capture workflow from the current conversation to a
traceable, linted Git commit. Treat `raw/` as immutable source material and
`wiki/` as the maintained synthesis; never rewrite raw history or create a
second page for information the vault already contains.

## Required context

Before changing anything, read `AGENTS.md`, `index.md`, and relevant files under
`.codex/memories/`. Read the complete candidate discussion/source and the
smallest relevant set of existing raw files, source notes, query pages, and
concept/entity pages. Project-local memory overrides global preferences.

## Workflow

### 1. Capture a candidate raw source

Use the current conversation as the source when the user asks to dump what was
discussed. Preserve the salient discussion, claims, decisions, links, dates,
ratings, and availability snapshots without inventing or silently correcting
facts. For an already supplied artifact, preserve its content and add only
minimal capture metadata.

Draft the capture outside `raw/` (for example, in a temporary file), then
choose a stable lowercase hyphenated topic slug and a date-stamped filename:
`raw/<topic-slug>-YYYY-MM-DD.md`. Add concise frontmatter when practical, for
example:

```yaml
---
type: raw
captured: YYYY-MM-DD
source_kind: conversation
topics:
  - topic-slug
---
```

Raw files are append-only and immutable. If a new capture is genuinely a new
version, create a new dated file and state what it supersedes; do not edit the
older capture.

### 2. Deduplicate before writing

Before adding the candidate to `raw/`, run the bundled scanner from the
repository root against the temporary draft:

```bash
python3 .codex/skills/wiki-capture-publish/scripts/duplicate_scan.py \
  --root . --candidate /path/to/candidate.md
```

Use scanner results as evidence, then read the reported matches:

- **Exact normalized match:** skip the raw write and ingest. Append a short
  duplicate-skipped note to `log.md` only if that event is useful to preserve.
- **High overlap or same subject:** compare claims, dates, and source context.
  If there is no material new information, skip it. If there is a new version,
  date, correction, or source perspective, capture it as a new raw file and
  link the earlier capture; preserve both accounts when they disagree.
- **Low overlap:** proceed, while still checking the relevant source notes and
  maintained pages for partial duplication.

Do not treat a changed timestamp, reordered prose, or a new filename as novel
information. Do not append the same claim to a maintained page twice merely
because it arrived through a new capture.

### 3. Ingest only the delta

After the duplicate decision, create one note under `wiki/sources/` for each
new raw source. Include a concise summary, key claims, provenance, and links to
affected maintained pages. Update existing concept/entity/query pages only with
durable claims that are new to them; add the source link beside every derived
claim. If sources disagree, preserve both claims and explain the disagreement.

Create a new maintained page only when the material adds a durable concept,
entity, or query that is not already represented. Prefer updating an existing
page over creating a near-duplicate. Add new pages and source notes to
`index.md`; do not add links to pages that do not exist.

### 4. Lint and record the run

Check for broken wikilinks, orphan maintained pages, missing source links,
duplicate page titles, stale or contradictory claims, and important concepts
without pages. Fix only issues supported by available sources; record unresolved
issues for human review. Append one dated `ingest` or `duplicate-skipped`
entry and one dated `lint` entry to the append-only `log.md`.

At minimum, use repository searches to inspect links and traceability:

```bash
rg -n '\[\[[^]]+\]\]' raw wiki index.md
rg -n '^sources:|sources/|raw/' wiki index.md
```

### 5. Commit and push safely

Run `git diff --check`, inspect `git status`, and review the complete diff.
Stage only files changed by this run; preserve unrelated user work. Use a
focused commit message such as `wiki: capture and ingest <topic>`. Push the
current branch to its configured upstream with ordinary `git push`; never force
push, rewrite history, or stage the whole repository indiscriminately.

If lint has unresolved high-confidence errors, stop before committing and report
them. If duplicate detection produced no tracked changes, do not create an
empty commit or push; report the existing matching source instead. If commit
works but push fails, keep the commit and report the exact recovery needed.

## Completion report

Report the raw capture decision, files changed, duplicate evidence considered,
lint result, commit hash, push result, and unresolved questions. Include links
to the new or updated wiki pages and source note.

## Bundled script

`scripts/duplicate_scan.py` provides deterministic normalized-content hashes,
token overlap, and title overlap across `raw/` and maintained Markdown pages.
It is a triage aid, not a substitute for reading the candidate and the matched
pages; semantic novelty still requires judgment.
