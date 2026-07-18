---
type: source
status: active
updated: 2026-07-18
source_file: "[[raw/llm-wiki-idea]]"
---

# LLM Wiki idea

## Summary

The source proposes using an LLM to incrementally build and maintain a
persistent personal wiki in Markdown. Raw documents remain immutable, while a
structured layer of summaries, concepts, entities, comparisons, and an overview
is updated as new sources arrive. The LLM performs the cross-referencing and
bookkeeping; the human curates sources, directs exploration, and reviews the
evolving synthesis.

## Key claims

- A persistent wiki can avoid reconstructing the same synthesis from raw
  documents on every query.
- Cross-references, contradictions, and evolving summaries are valuable
  knowledge artifacts in their own right.
- Ingest, query, and lint are the core operating loops.
- A content-oriented `index.md` and chronological `log.md` make a Markdown wiki
  navigable and auditable at moderate scale.
- Obsidian is a useful review surface because links and graph view make the
  structure visible.
- Search tooling can be added later when the index is no longer sufficient.

## Implications for this vault

This project adopts the source's three-layer architecture through `raw/`,
`wiki/`, and [[AGENTS]]. The initial implementation stays deliberately
small and domain-neutral; future sources should determine which entities and
concepts deserve dedicated pages.

## Related pages

- [[wiki/concepts/llm-wiki]] — maintained concept synthesis.
- [[wiki/overview]] — current vault state and design principles.

## Provenance

The complete supplied idea is preserved unchanged in [[raw/llm-wiki-idea]].
