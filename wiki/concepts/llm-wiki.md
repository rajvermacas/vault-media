---
type: concept
status: active
updated: 2026-07-18
sources:
  - "[[wiki/sources/llm-wiki-idea]]"
---

# LLM Wiki

The LLM Wiki is a pattern for building a personal knowledge base in which an
LLM incrementally maintains a persistent, interlinked collection of Markdown
pages. It sits between raw source material and future questions.

## How it differs from ordinary RAG

In a conventional retrieval-augmented workflow, the model repeatedly retrieves
fragments from source files and reconstructs an answer from scratch. In an LLM
Wiki, each new source is integrated into an existing synthesis: source notes,
concept pages, entity pages, cross-references, and disagreements are updated as
knowledge accumulates.

The result is a compounding artifact. The value is not only in the summaries,
but also in the links between them and in the record of what changed over time.

## Core operations

- **Ingest**: read a raw source, create its source note, update affected pages,
  refresh the index, and append to [[log]].
- **Query**: navigate from the index through relevant pages, answer with
  citations, and file durable analyses under `wiki/queries/`.
- **Lint**: find contradictions, stale claims, orphan pages, missing
  cross-references, and promising research gaps.

## Why it compounds

The maintenance burden of a human wiki grows with every page: filing, linking,
updating summaries, and checking consistency. An LLM can perform that
bookkeeping in the same pass that it reads a new source, leaving the human to
curate sources, set direction, review changes, and ask better questions.

## Useful affordances

Obsidian's graph view exposes the shape of the knowledge base. A plain Markdown
index is enough at small scale; a local search tool can be added later if the
wiki outgrows index-driven navigation. Frontmatter can support Dataview views,
and durable comparisons or analyses can be authored as Markdown artifacts.

## Boundaries

This pattern is only as reliable as its sources and review process. The wiki is
a maintained synthesis, not an authority: preserve provenance, distinguish
claims from interpretation, and flag contradictions rather than hiding them.
