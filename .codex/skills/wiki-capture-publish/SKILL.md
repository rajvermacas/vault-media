---
name: wiki-capture-publish
description: Capture the current discussion or supplied source material as immutable raw Markdown, semantically compare it with the existing raw and maintained wiki, ingest only novel durable claims, lint the Obsidian vault, and commit and push the focused changes. Use when the user asks to dump a conversation into this vault, capture and ingest notes, maintain the wiki after a discussion, or run the complete raw-to-published workflow.
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

## Session checkpoint (default)

Treat the most recent successful ingest in the current conversation as the
session checkpoint. On a later ingestion request in that same session, use only
the substantive discussion, supplied material, decisions, and new claims after
that checkpoint. Use earlier messages only as context needed to understand a
new delta; do not copy them into the new raw capture or ingest them again.

After each successful ingest and lint, record a short checkpoint in `log.md`,
such as the last topic or user request included and whether the scope was
`full-session` or `since <previous checkpoint>`. The next invocation should use
the latest checkpoint in the conversation first and the log entry as a fallback.
If the boundary is ambiguous, choose the narrower, later boundary and report
what was excluded. Do not advance the checkpoint when the ingest was abandoned
before its raw/wiki changes were completed.

Only reset this default when the user explicitly asks to re-ingest, refresh,
backfill, or rebuild the entire session/history.

## Workflow

### 1. Capture a candidate raw source

Use the current conversation as the source when the user asks to dump what was
discussed. Apply the session checkpoint first: capture only the new material
since the last successful ingest by default. Preserve the salient new claims,
decisions, links, dates, ratings, and availability snapshots without inventing
or silently correcting facts. Include only minimal earlier context when it is
needed to make the delta understandable, and do not treat that context as a
new claim. For an already supplied artifact, preserve its content and add only
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

### 2. Deduplicate by semantic review before writing

Do not use a deterministic duplicate scanner or a fixed similarity threshold.
First apply the session checkpoint. Then dynamically identify the candidate's topics, named entities, questions,
decisions, dates, ratings, availability claims, and other substantive claims.
Search for those signals across `raw/`, `wiki/sources/`, and the smallest
relevant set of maintained pages, then read the likely matches in full.

Compare the candidate and each match claim by claim. Classify each item as:

- **Repeat:** the same fact, recommendation, decision, or source context is
  already preserved, even if the wording differs.
- **Delta:** a genuinely new fact, source, date/version, user preference,
  resolution, or useful synthesis is present.
- **Conflict:** the candidate and existing material disagree; preserve both
  claims with provenance and explain the disagreement.

Treat reordered prose, changed capture metadata, a new filename, and paraphrases
with no new meaning as repeats. Do not append a repeated claim to a maintained
page merely because it arrived through a new capture.

If every substantive item is a repeat, skip both the raw write and ingest. Add a
short `duplicate-skipped` entry to `log.md` only when the attempted capture is
useful audit history. If the candidate contains a delta or conflict, preserve
the complete candidate as a new immutable raw file, link a new version to the
earlier capture when appropriate, and ingest only the delta/conflict.

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
issues for human review. Append one dated `ingest` or `duplicate-skipped` entry
and one dated `lint` entry to the append-only `log.md`. For an ingest, include a
`Session checkpoint:` line describing the material covered and an `Ingest
scope:` line set to `full-session` or `since <previous checkpoint>`.

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
them. If semantic review found no material new information, do not create an
empty commit or push; report the existing matching source instead. If commit
works but push fails, keep the commit and report the exact recovery needed.

## Completion report

Report the raw capture decision, session checkpoint and scope, similar sources
reviewed, claim-level delta or conflict decision, files changed, lint result,
commit hash, push result, and unresolved questions. Include links to the new or
updated wiki pages and source note.
