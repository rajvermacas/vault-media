---
type: overview
status: active
updated: 2026-07-18
sources:
  - "[[wiki/sources/llm-wiki-idea]]"
---

# LLM Wiki overview

This vault treats an LLM as the maintainer of a persistent wiki rather than as
a one-shot retrieval layer. New material enters through `raw/`; the LLM reads
it, updates the structured synthesis under `wiki/`, and records the work in
[[log]]. Obsidian is the browsing and review surface.

## Layers

1. **Raw sources** — curated, immutable articles, papers, notes, images, and
   other source files.
2. **Wiki** — interlinked summaries, concepts, entities, comparisons, and
   durable answers maintained from those sources.
3. **Schema** — [[AGENTS]], which defines page formats, link discipline, and
   ingest, query, and lint workflows.

## Current state

The vault is bootstrapped with one source and one initial concept page. It is
intentionally domain-neutral until more sources establish the first subject
area.

## Design principles

- Compile knowledge once, then keep the synthesis current.
- Make connections and disagreements visible.
- Keep source material immutable and claims traceable.
- File durable answers back into the wiki.
- Let the human curate sources and direction while the LLM handles
  bookkeeping.
