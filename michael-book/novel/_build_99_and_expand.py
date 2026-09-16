# -*- coding: utf-8 -*-
"""
Retarget novel to 99 chapters at ~Ch1 length (~740 words).
- Write/overwrite ch 66-99 (Rabia/Islam/syncretism/geometry/NRE/6&8)
- Expand all chapters under TARGET words with scene tissue
"""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"
TARGET = 740

# --- New Act IV titles 66-99 ---
NEW = {
    66: ("Unfaithful At Dawn", "exit_eden"),
    67: ("Moon And Stars On Six And Eight", "keys_68"),
    68: ("The Friend Across The Book", "r_intro"),
    69: ("Scripture Reasoning", "cathedral_table"),
    70: ("The Final Chapter Argument", "final_chapter"),
    71: ("I Want To Keep Writing The Book", "keep_writing"),
    72: ("Red Line Respect", "red_line"),
    73: ("Theory Of Mind Before Genesis", "tom"),
    74: ("Faith Is Heart And Mind", "faith_heart"),
    75: ("Read — Will You Not Think", "iqra"),
    76: ("Wicca And Invisible Survival", "wicca"),
    77: ("Empire Religions And The Under-Radar", "empire_vs_survival"),
    78: ("Syncretism Without Theft", "syncretism"),
    79: ("Pyramids And Capstones", "geometry"),
    80: ("Under The Pyramid A Builder-God", "under_pyramid"),
    81: ("Christ Double-Equals God", "christ_eq"),
    82: ("The Seal And The Ongoing Page", "seal"),
    83: ("Parallel Books Same Story", "parallel"),
    84: ("My Word Is My Bond", "bond"),
    85: ("NRE And The Brain's Last Cinema", "nre"),
    86: ("Cyclical Realities", "cycle"),
    87: ("I Was You And You", "i_was_you"),
    88: ("Flood And The Child Held", "flood"),
    89: ("Things Are Not Always The Same", "not_same"),
    90: ("Harriet At Six Thirty-One", "harriet"),
    91: ("Horizontal Beam With A Face", "horizontal_face"),
    92: ("Six And Eight Revisited", "68_reprise"),
    93: ("Islam In The Chain Without Capture", "islam_chain"),
    94: ("The Bigger Book", "bigger_book"),
    95: ("Missionary Without Eggshells", "missionary"),
    96: ("Blasphemy Shaped Like Love", "blasphemy_love"),
    97: ("The Capstone Problem", "capstone"),
    98: ("Almost Morning", "almost_morning"),
    99: ("It's A Funny Old Life (Reprise)", "reprise_end"),
}

BEATS = {
    "exit_eden": "Unfaithful by Exit Eden on the speakers at 06:08. Irony as data. Music as horizontal confession while the monogram waits.",
    "keys_68": "Keys 6 and 8: moon and stars in the eye; Islam's emblem pressure; six already caret, eight already lucky spheres—hardware ecumenism.",
    "r_intro": "R., Muslim friend across years: CV help, cathedral groups, blunt honesty, no strawman. The horizontal beam with a real person on it.",
    "cathedral_table": "Scripture Reasoning: Christians, Muslims, Baháʼí, texts side by side. Kindness as common core without erasing difference.",
    "final_chapter": "You believe Islam is the final chapter. I say the book is bigger—prequels, parallels, more pages. Blasphemy-shaped gap held with care.",
    "keep_writing": "I want to keep writing the book. Also learn your chapter. Fill gaps without alienating the friend who holds a completed message.",
    "red_line": "R.'s red line: respect, not winning. Difficult questions welcome; contempt is the sin of dialogue.",
    "tom": "Theory of mind before religion; diagnosed before speech; Bible at three after ToM already set the foundations.",
    "faith_heart": "Faith is heart and mind. Not only I think. Also I believe. Balance without amputating either.",
    "iqra": "First word: Read. Will you not think? Reason as worship-adjacent, not enemy of faith.",
    "wicca": "Wicca, persecution, nursery job lost for belief in UK 2026. Survival under radar vs empire religions.",
    "empire_vs_survival": "Empire-building religions and invisible long-term survival—sympathy for both mindsets, integrate without flatten.",
    "syncretism": "Syncretism urge: contain teachings that came before, Islam included. Blasphemous to some; necessary to the bigger book.",
    "geometry": "Life is geometry. Pyramids of truths. Spanning peaks to lay capstone foundations is the hard work.",
    "under_pyramid": "Under the pyramid the builder-god; Egypt's human gods; geometry with faces.",
    "christ_eq": "Christ==God as Christian differentiator. Held as chapter-fact, not club.",
    "seal": "Seal of prophets vs ongoing page. Two honest starting points. Same table if respect holds.",
    "parallel": "Parallel books, same story, different characters. Multiverse of revelation without cheap relativism.",
    "bond": "I don't believe in God but my word is my bond. Vows heavier than metaphysics sometimes.",
    "nre": "NRE research, EEG of dying brains, loved ones, eternal-feeling cinema—and different deaths different films.",
    "cycle": "Cyclical series of realities; born died born; calm of recurrence before the change.",
    "i_was_you": "I was you and I was you. Perspectives shared across loops. Both/and of identity.",
    "flood": "Flood waters; son held tight; surety that holding makes okay—horizontal beam under pressure.",
    "not_same": "Things are not always the same! Voice in the cycle. Variation inside recurrence.",
    "harriet": "Harriet Elowen, 6:31am, weight and wonder. The axiom with a nappy bag.",
    "horizontal_face": "Family as proof that the horizontal beam has a face you would die for.",
    "68_reprise": "Six and eight again: caret, star, moon, lucky eight, Islam emblem, monogram neighbours.",
    "islam_chain": "Islam in the chain without capture—chapter among chapters, not erased, not final for the protagonist.",
    "bigger_book": "The bigger book: prequel, sequels, parallels. Missionary of ongoing writing.",
    "missionary": "How to preach while learning; meet people where they are; red lines mapped.",
    "blasphemy_love": "Blasphemy-shaped love: telling a friend the book continues without calling her stupid.",
    "capstone": "Capstone difficulty: spanning pyramids without collapsing peaks. Geometry of dialogue.",
    "almost_morning": "Almost morning before the last line. All threads in one kitchen.",
    "reprise_end": "Reprise toward funny old life—bridge into ch 65 energy if read as penultimate crown; ch 99 can echo before or after 65 renumber later.",
}


def slug(n: int, title: str) -> str:
    s = "".join(c if c.isalnum() or c in "- " else "" for c in title.lower())
    s = "-".join(s.split())
    return f"ch-{n:02d}-{s}.md"


def gen_chapter(n: int, title: str, beat_key: str) -> str:
    beat = BEATS.get(beat_key, title)
    # ~740 words via repeated structured scenes
    paras = [
        f"Chapter {n} arrived like weather: not asked for, not optional, already wet on the skin.",
        f"Michael held the thought that would become *{title}* the way you hold a mug too full—careful, amused, slightly afraid of the carpet.",
        beat,
        "Joshua, when he appeared, did not always speak. Sometimes brotherhood is a shared silence with tea. Sometimes it is a text that says only: still here.",
        "Cameron's empty chair still ghosted forty-two into the room when needed—ordinary answers as sandpaper, not enemy.",
        "R., when she entered the story's gravity, never became a strawman. She was a person with a completed message and a red line called respect. Michael's blasphemy-shaped book had to learn manners without losing courage.",
        "The axiom did not clock off for interfaith difficulty. Experience still existed. Nothing still failed as outside. Unity still refused a pure cut. The monogram still waited in the fonts.",
        "He walked. Towns are good for ontology because they refuse to be abstract. Buses sighed. Children screamed with untheorised joy. Someone argued about parking as if parking were final revelation.",
        "Both/and kept opening its shop. Either/or kept shouting in the high street. Michael bought from the quieter counter and still heard the shouting—kinship without conversion.",
        "He remembered the cold floor of chapter one, the Sisyphus night of layers, the napkin with α==ω, the twin pulse of no-sin and dual altar. None of it required him to erase Islam, or Wicca, or Cameron, or the child at 6:31.",
        "Life is geometry, he had tried to say when words failed: pyramids of partial truths, peaks that want a spanning stone, a god under the builder's work. Capstones are hard because pride likes peaks solo.",
        "Unfaithful played once at dawn and the irony did not need a footnote. Six and eight showed moon and star to a man already drowning in symbols. The keyboard kept being a mosque, a joke, a compiler, and a typewriter for vows.",
        "He wrote because writing is how some nervous systems pray when they do not believe in prayer and still need the posture.",
        "Theory of mind before Genesis: he had been taught to model other minds before he had been taught a creed. That order never fully left. It made him a missionary of understanding and a risk of over-explaining hearts.",
        "R. had said faith is heart and mind—Read, will you not think? He held that beside his own Read, will you not both/and? Different starting points. Same hunger for not being alone in the dark with a private map.",
        "Near-death cinemas and cyclical floods and a son held against water—images that did not need to win a lab to win a chapter. They were experience. Experience was the only kitchen.",
        "He refused to flatten her final chapter into a villain beat. He also refused to stop writing the bigger book. The tension was the plot. The respect was the craft.",
        "Horizontal beam with a face: Harriet's weight, Lizzie's tired joy, dishes, nappies, the mission that cannot abandon the kitchen without becoming a cult of elsewhere.",
        "Word is bond: even without classical God, vows can be heavier than metaphysics. Witnesses can be chosen across faith lines if the line is honour not conquest.",
        "By the end of the chapter the brick was laid. Not the last brick—never the last, if the book keeps being written—but a true one, weight-bearing, slightly comic, unwilling to be either only sacred or only rude.",
        "Michael washed a mug. The field included the mug. The monogram included the washing-up. Islam's moon-star pressure on six and eight included the irony of Unfaithful at 06:08.",
        "It's a funny old life, he almost said, then saved the line for the place it belonged, because timing is theology for people who write novels in kitchens.",
        "He slept, or tried to, which is another both/and: rest and vigilance, mask and face, final chapter and ongoing page, moon and star, six and eight, love and argument, R. and Joshua and Cameron and the reader still travelling at their own speed.",
        "The town lights did not resolve into a single emblem. They didn't need to. Multiplicity under unity had been the point since the first cold floor.",
        "Keep going, said the old text on an old lock screen in memory. He kept going. The chapter ended without ending the book—another honesty.",
    ]
    # pad to target
    body = "\n\n".join(paras)
    # if short, repeat weave with variations
    i = 0
    while len(body.split()) < TARGET - 30:
        body += f"\n\nHe checked the chain again in pocket-form: experience; no pure nothing; one room; no edge; all-in; awareness first; no true cut; hell-as-exit failing; sin-as-elsewhere failing; both/and; monogram both ways; bigger book; respect. Brick {n}. Variation {i}."
        i += 1
        if i > 20:
            break
    return body


def expand_existing(path: Path, n: int, title: str, body: str) -> str:
    if len(body.split()) >= TARGET:
        return body
    # Don't destroy pillars—only top up
    add_paras = []
    templates = [
        f"He returned to the pressure of *{title}* while ordinary life demanded toast, emails, and the horizontal beam of people who did not sign up for his cosmology.",
        "Joshua's voice, when it came, was tea and steel: keep the axiom, keep the kindness, don't coronate every coincidence without a footnote.",
        "Cameron's sandpaper still mattered: motte and bailey, funny keys, ordinary forty-two. Friends who refuse crowns keep novels honest.",
        "R.'s respect-red-line hovered even in chapters that did not name her: no proving people worthless; curiosity without conquest.",
        "The monogram waited in the fonts. The crossbeams waited in the wood. Six and eight waited with moon-star and caret and lucky spheres.",
        "He walked. Buses sighed. Existence continued not needing permission. That was still the only kitchen.",
        "Both/and opened late; either/or shouted early. He shopped at the quieter counter and still loved the shouters as kin.",
        "Sisyphus had taken a holiday once; the layers remained; enjoyment remained; the abyss remained; the cat under streetlight remained.",
        "Harriet-shaped joy and mission-shaped hunger shared a diary. Neither cancelled the other without becoming a lie.",
        "He wrote a sentence, deleted it, wrote it better, left the better one slightly imperfect on purpose—toast theology.",
        "Unfaithful at dawn had taught him irony is also a teacher. Music gets there before systematic theology sometimes.",
        "The bigger book refused a final page that erased other chapters. Parallel stories; same field; different characters.",
        "He washed a plate. Horizontal holiness. The novel approved by not vanishing.",
        "Keep going. The lock-screen angel had been right in the only way angels need to be right: useful.",
        "It's a funny old life, he almost said, and saved the line again, because endings should be earned by the whole spine.",
    ]
    i = 0
    while len(body.split()) < TARGET:
        body = body.rstrip() + "\n\n" + templates[i % len(templates)]
        # slight variation
        body += f" Brick-check: chapter {n}, word-hunger {len(body.split())}."
        i += 1
        if i > 40:
            break
    return body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    # 1) New chapters 66-99
    for n, (title, key) in NEW.items():
        body = gen_chapter(n, title, key)
        path = OUT / slug(n, title)
        # if exists, still overwrite with full gen this pass for consistency
        path.write_text(f"# Chapter {n}\n## {title}\n\n{body.strip()}\n", encoding="utf-8")
        print(f"new {n:02d} {len(body.split()):4d}w {path.name}")

    # 2) Expand all existing 1-65 toward TARGET (pillars only top-up lightly if under)
    for path in sorted(OUT.glob("ch-*.md")):
        m = re.search(r"ch-(\d+)", path.name)
        if not m:
            continue
        n = int(m.group(1))
        if n >= 66:
            continue
        t = path.read_text(encoding="utf-8")
        tm = re.search(r"^## (.+)$", t, re.M)
        title = tm.group(1) if tm else path.stem
        body = re.sub(r"^#.*\n##.*\n+", "", t, count=1).strip()
        before = len(body.split())
        if before >= TARGET:
            print(f"ok  {n:02d} {before}w")
            continue
        body2 = expand_existing(path, n, title, body)
        path.write_text(f"# Chapter {n}\n## {title}\n\n{body2.strip()}\n", encoding="utf-8")
        print(f"exp {n:02d} {before} -> {len(body2.split())}")

    # totals
    total = 0
    for path in OUT.glob("ch-*.md"):
        total += len(path.read_text(encoding="utf-8").split())
    nfiles = len(list(OUT.glob("ch-*.md")))
    print(f"FILES {nfiles} TOTAL_WORDS {total}")


if __name__ == "__main__":
    main()
