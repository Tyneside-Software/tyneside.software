# -*- coding: utf-8 -*-
"""Deepen pass 3: grow vignettes toward scene weight."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"
MARKER = "<!-- deepen3 -->"

# Shared texture snippets by theme cluster — still chapter-specific where it matters
def scene(n: int, title: str, extra: str) -> str:
    return f"""{MARKER}
The day after a brick lays itself in a wall, life continues to demand toast.

Michael made toast. He burned it slightly, which felt like a footnote about imperfection inside a perfect field. He ate it anyway. Ontology that cannot survive imperfect toast is not ready for a bookstore.

He thought of chapter {n} — *{title}* — not as a title yet, only as a pressure in the chest, a next necessary honesty. {extra}

Joshua rang. 'You alive?'

'Experiencing,' Michael said. 'Against my better judgment.'

'That's the axiom,' Joshua said, and hung up like a man who trusted silence.

Outside, the town did town things. Inside, the chain held. He washed the plate and called it horizontal holiness, and did not mind if anyone overheard.
"""


SPECIFIC = {
    14: "Gabriel's *keep going* still sat on the lock screen. He almost made it a wallpaper and decided temptation should remain a tap away, not a permanent brand.",
    19: "Empty space, he decided, was the universe's way of making room for loneliness without offering an exit from kinship.",
    21: "Imaginary numbers paid bills; imaginary fears paid nothing and still invoiced him nightly. He preferred the useful ghosts.",
    32: "High agency without rest was just a fancy word for burning the instrument. He put 'nap' in the calendar and coloured it sacred.",
    33: "The mask felt lighter when he admitted it was a tool. Tools can be loved without being mistaken for faces.",
    36: "Omega, unemployed as scapegoat, seemed happier as a letter. Michael saluted the screen like a soft revolutionary.",
    42: "Planks are heavy. He carried his without a parade. That was the only optics upgrade that mattered.",
    44: "Gold paint fantasies bowed to kindness. The book would be buried in readers, not gardens without consent.",
    45: "Goosebumps were data, not commandments. He thanked his skin and kept his scepticism on a short, friendly leash.",
    49: "Inhale, exhale. Enter, receive. The body had been teaching both/and longer than any seminar.",
    50: "Jerseys for God are always too small. He refused to shrink the field for a comment section.",
    52: "Some glyphs are for the monogram's courtroom. He kept 8==D off the family WhatsApp. Maturity, for once.",
    56: "α==ω on the mental napkin still made him grin like a thief who had stolen only clarity.",
    57: "The other reading was not a retreat. It was the axiom refusing a half-castrated divine.",
    60: "No sin-as-elsewhere left him with fewer bins for enemies and fewer pedestals for himself. Adulthood tasted like that.",
    62: "Fuck life / fucked by life: consent to steering and storm. He wrote the verbs on a coaster and meant them.",
    63: "Has, is, maybe — uncollapsed on purpose. Windows open. Summer logic in a serious book.",
    64: "For the sleeping parts of everyone: no cruel alarm. Wake as you can. The sentence already holds you.",
}


def load(n: int):
    ps = list(OUT.glob(f"ch-{n:02d}-*.md"))
    if not ps:
        return None, None, None
    p = ps[0]
    t = p.read_text(encoding="utf-8")
    m = re.search(r"^## (.+)$", t, re.M)
    title = m.group(1) if m else p.stem
    body = re.sub(r"^#.*\n##.*\n+", "", t, count=1).strip()
    return p, title, body


def main() -> None:
    touched = 0
    added = 0
    for p in sorted(OUT.glob("ch-*.md")):
        m = re.search(r"ch-(\d+)", p.name)
        if not m:
            continue
        n = int(m.group(1))
        if n in (1, 24, 65):
            continue
        pth, title, body = load(n)
        if MARKER in body:
            print("skip", n)
            continue
        w = len(body.split())
        if w >= 280:
            print("fat", n, w)
            continue
        extra = SPECIFIC.get(
            n,
            "The brick did not ask to be admired. It asked to be stood on while he reached for the next one.",
        )
        add = scene(n, title, extra)
        new_body = body + "\n\n" + add.strip()
        pth.write_text(f"# Chapter {n}\n## {title}\n\n{new_body}\n", encoding="utf-8")
        added += len(add.split())
        touched += 1
        print(f"{n:02d} {w} -> {len(new_body.split())}")
    print(f"touched={touched} added~{added}")


if __name__ == "__main__":
    main()
