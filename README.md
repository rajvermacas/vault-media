# LLM Wiki

An Obsidian vault for turning source material into a persistent, interlinked
knowledge base maintained with an LLM.

Start at [[index]]. The operating rules live in [[AGENTS]] (also available to
Codex as the repository instruction file). Put source material in `raw/`, read
the generated synthesis in `wiki/`, and keep the chronological activity record
in [[log]].

## First workflow

1. Add a source to `raw/` without editing it afterward.
2. Ask the LLM to ingest it and update the wiki.
3. Review the source note and any changed concept/entity pages in Obsidian.
4. Ask for a lint pass periodically to find stale claims, missing links, and
   useful gaps to investigate.

The supplied design note is the first source in this vault: [[wiki/sources/llm-wiki-idea]].
