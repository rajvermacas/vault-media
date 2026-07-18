# Wiki log

Append-only activity log. Each entry records a meaningful change to the wiki.

## [2026-07-18] bootstrap | LLM Wiki vault

- Created the source/wiki/schema layers for this Obsidian project.
- Seeded the vault with the supplied LLM Wiki idea.
- Created the initial overview, concept synthesis, index, and workflow rules.

## [2026-07-18] ingest | Reddit city-as-character series recommendations

- Added immutable raw capture [[raw/reddit-city-as-character-series-2026-07-18]]
  from Reddit recommendation threads.
- Created [[wiki/sources/reddit-city-as-character-series]] and durable query
  page [[wiki/queries/city-as-character-series]].
- Flagged unresolved availability for *The Kettering Incident* and the
  country-specific nature of JustWatch snapshots.

## [2026-07-18] lint | post-Reddit ingest

- Checked wikilinks, source traceability, maintained-page reachability, and
  duplicate top-level page titles.
- Found no broken wikilinks, orphaned maintained pages, or duplicate maintained
  pages.
- Corrected the stale overview statement that the vault still had one source
  and was domain-neutral.

## [2026-07-18] ingest | Alexandra Daddario movie identification

- Added immutable raw capture [[raw/alexandra-daddario-the-layover-2026-07-18]]
  containing verified plot, ratings, and India availability details for
  *The Layover*.
- Created [[wiki/sources/alexandra-daddario-the-layover]] and durable query
  page [[wiki/queries/alexandra-daddario-movie-identification]].

## [2026-07-18] lint | post-*The Layover* ingest

- Checked wikilinks, source traceability, maintained-page reachability, and
  duplicate maintained-page titles.
- Found no broken wikilinks or duplicate maintained pages; availability remains
  a time- and country-dependent snapshot.

## [2026-07-18] ingest | Alexandra Daddario and Ana de Armas recommendation set

- Added immutable raw capture [[raw/alexandra-daddario-ana-de-armas-recommendations-2026-07-18]] for the complete movie set discussed in the recommendation thread.
- Created [[wiki/sources/alexandra-daddario-ana-de-armas-recommendations]] and durable query page [[wiki/queries/glamorous-alexandra-daddario-ana-de-armas-movies]].
- Preserved the existing detailed [[wiki/sources/alexandra-daddario-the-layover]] source note.

## [2026-07-18] lint | post-recommendation-set ingest

- Checked wikilinks, source traceability, maintained-page reachability, and duplicate maintained-page titles.
- Flagged all streaming details as country- and date-dependent snapshots; no broken wikilinks found.

## [2026-07-18] maintenance | wiki capture and publish skill

- Added project-local `.codex/skills/wiki-capture-publish/SKILL.md` for
  conversation capture, duplicate-aware ingest, linting, and focused Git
  commit/push handling.
- Updated duplicate handling to require dynamic, claim-level semantic review by
  the agent rather than a deterministic scanner or fixed threshold.
