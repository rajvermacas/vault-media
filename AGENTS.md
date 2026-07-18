# LLM Wiki schema

This repository is an Obsidian vault for a persistent, LLM-maintained wiki.

## Mission

Turn curated source material into a growing, interlinked knowledge base. The
wiki is the maintained synthesis; the raw collection is the source of truth.

## Directory contract

- `raw/` contains immutable source material. Never rewrite, summarize over, or
  delete a raw source. Add a new file when a source has a new version.
- `wiki/` contains maintained markdown pages written by the LLM.
  - `wiki/concepts/` explains ideas, methods, and systems.
  - `wiki/entities/` covers people, organizations, products, and places.
  - `wiki/sources/` contains one source note per raw source.
  - `wiki/queries/` stores useful answers and analyses that should persist.
- `index.md` is the content-oriented catalog of the wiki.
- `log.md` is append-only and records ingests, queries, and lint passes.
- `.codex/memories/` contains project-local context for this vault. Read relevant
  files there when working in this project; it is separate from Codex's global
  memory store.

## Instruction precedence and project memory

- This `AGENTS.md` is authoritative for all work in this vault.
- Before taking action, read `index.md` and any relevant files under
  `.codex/memories/`.
- Project-local memory is authoritative within this project and is separate from
  global Codex memory.
- When the user says “project memory,” update `.codex/memories/` only. Do not
  update global Codex memory unless the user explicitly says “global memory.”
- If project-local and global memories conflict, project-local memory wins for
  this vault.
- Before adding a preference, inspect existing project memory and update the
  appropriate existing file when possible. Report the exact file changed.

## Page conventions

Maintained wiki pages should use YAML frontmatter when practical:

```yaml
---
type: concept | entity | source | query | overview
status: active | draft | superseded
updated: YYYY-MM-DD
sources:
  - "sources/source-slug"
---
```

Use stable, lowercase, hyphenated filenames. Prefer Obsidian wikilinks such as
`wiki/concepts/llm-wiki` (written as an Obsidian link in page content) over filesystem links. Add links when a page introduces
a named concept, entity, source, or related question. Do not create links to
pages that do not exist unless the missing page is explicitly listed as a
follow-up in the same change.

Claims derived from sources must link to the relevant source note. When sources
disagree, preserve both claims, explain the disagreement, and link to each
source; do not silently choose a winner.

## Workflows

### Ingest

1. Read the new raw source completely.
2. Create or update its note under `wiki/sources/` with a concise summary,
   key claims, and links to affected pages.
3. Create or update concept/entity pages only where the source adds durable
   knowledge.
4. Update `index.md` and append one dated entry to `log.md`.
5. Report the files changed and any unresolved questions for human review.

### Query

1. Read `index.md` and relevant `.codex/memories/` files first.
2. Treat project-local preferences as applicable context for the answer.
3. Read the smallest relevant set of wiki pages.
4. Answer with links back to the wiki and source notes.
5. If the answer contains durable synthesis, offer or create a page under
   `wiki/queries/` and update the index and log.

### Lint

Check for broken wikilinks, orphan pages, missing source links, stale or
contradictory claims, duplicate pages, and important concepts mentioned without
their own page. Record findings in `log.md`; fix only issues supported by the
available sources and flag the rest for review.

## Change discipline

Keep raw sources unchanged. Make focused edits, preserve existing user work,
and finish each operation by checking links and updating the log. The human
curates sources and direction; the LLM maintains the wiki and its bookkeeping.
