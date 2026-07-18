#!/usr/bin/env python3
"""Find likely duplicate or overlapping Markdown sources in an Obsidian vault."""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


STOPWORDS = {
    "about", "after", "again", "also", "been", "being", "between", "could",
    "from", "have", "into", "more", "only", "other", "should", "that",
    "their", "there", "these", "they", "this", "through", "under", "were",
    "what", "when", "where", "which", "while", "with", "would", "your",
}
WORD_RE = re.compile(r"[a-z0-9]+(?:['-][a-z0-9]+)*")


@dataclass(frozen=True)
class Document:
    path: Path
    digest: str
    words: frozenset[str]
    title_words: frozenset[str]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :]
    return text


def normalized(text: str) -> str:
    text = strip_frontmatter(text)
    text = re.sub(r"!?\[\[([^]|#]+)(?:[#|][^]]*)?\]\]", r"\1", text)
    text = re.sub(r"https?://\S+", " ", text.lower())
    text = re.sub(r"[^a-z0-9\s'-]", " ", text)
    return " ".join(text.split())


def words(text: str) -> frozenset[str]:
    return frozenset(
        word for word in WORD_RE.findall(normalized(text))
        if len(word) > 2 and word not in STOPWORDS
    )


def title_words(path: Path, text: str) -> frozenset[str]:
    heading = re.search(r"^#\s+(.+?)\s*$", strip_frontmatter(text), re.MULTILINE)
    title = heading.group(1) if heading else path.stem
    return words(title)


def load_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    canonical = normalized(text)
    return Document(
        path=path,
        digest=hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        words=words(text),
        title_words=title_words(path, text),
    )


def similarity(left: frozenset[str], right: frozenset[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def candidates(root: Path, candidate: Path) -> list[Path]:
    paths: list[Path] = []
    for folder in (root / "raw", root / "wiki"):
        if folder.exists():
            paths.extend(folder.rglob("*.md"))
    return sorted(path for path in paths if path.resolve() != candidate.resolve())


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--threshold", type=float, default=0.55)
    args = parser.parse_args()

    root = args.root.resolve()
    candidate = args.candidate.resolve()
    if not candidate.is_file():
        parser.error(f"candidate does not exist: {candidate}")

    target = load_document(candidate)
    print(f"candidate: {display_path(candidate, root)}")
    print(f"normalized_sha256: {target.digest}")
    print("matches:")

    found = False
    for path in candidates(root, candidate):
        other = load_document(path)
        exact = target.digest == other.digest
        body_score = similarity(target.words, other.words)
        title_score = similarity(target.title_words, other.title_words)
        if not exact and body_score < args.threshold and title_score < 0.5:
            continue
        found = True
        kind = "EXACT" if exact else "OVERLAP"
        relative = display_path(path, root)
        print(
            f"- {kind} body={body_score:.3f} title={title_score:.3f} {relative}"
        )

    if not found:
        print("- none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
