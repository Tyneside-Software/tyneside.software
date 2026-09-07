# -*- coding: utf-8 -*-
"""Append scene tissue to thin chapters; preserve existing text."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"

ADD: dict[int, str] = {
    4: """
He tried, for honesty, to imagine a first moment of the whole. The mind offered fireworks and then blanked, because fireworks need a sky and blankness needs a watcher. Beginnings of modes were easy: birthdays, first jobs, first heartbreaks. Beginnings of *existence* kept failing the sponsorship test.

Joshua set a timer for the pasta. 'Edges for noodles. Not for the field.'

Michael laughed despite himself. Cosmology with starch. The best kind.
""",
    5: """
On the walk he tried collecting leftovers like a magpie of dualism: a gap between buildings (still space), a silence between songs (still heard), a secret he hadn't told (still known-by-him). Each specimen joined the museum of the included.

He texted Joshua a photo of a lost glove on a wall. *Outside?*

Joshua: *Still in the picture.*

Michael put the phone away, annoyed and fond, and kept walking through the only kitchen there is.
""",
    6: """
Later he drafted a personal rule: when a voice offers only two knives, ask who benefits from the duel. Often the answer was anxiety wearing a uniform—religious, secular, political, romantic.

Both/and was slower. It required listening. It ruined good rants.

He practised on a small scale: the sandwich was both fuel and pleasure. The preacher was both sincere and wrong about the ditch being mandatory. The sceptic was both sharp and lonely.

The city did not convert. Cities rarely do. Michael converted his feet, one step at a time.
""",
    7: """
They played a game: take a headline, force it through both/and without becoming mush.

War was horror *and* industry *and* grief *and* courage—none cancelling the others into a slogan.

A breakup was freedom *and* bereavement.

A joke was defence *and* invitation.

Joshua won when he said, 'You're tired *and* you're not done.'

Michael bought the next round and admitted the shop had better stock than his pride.
""",
    8: """
He opened an old laptop folder and found the delimiter notes like fossils of a younger self who already knew the joke without naming it: something and nothing marked with the same teeth.

Maths. Words. Things.

Three ways the field carves itself for handling.

He closed the folder gently, as if it might wake up and demand royalties from the novel.
""",
    9: """
Walking home he saw a plus sign on a pharmacy and almost bowed. Vertical claim of health, horizontal claim of service hours, both beams needed or the shop was just a box.

Joshua would have called that overreading.

Michael would have agreed *and* done it anyway.
""",
    10: """
He wrote the chain on a sticky note for the fridge:

carrot/stick → + → cross → both/and → (later) monogram

It looked like a conspiracy board drawn by a cheerful madman.

Which, in fair weather, he was.
""",
    11: """
Michael thought of masks—shame as the fear of horizontal eyes—and of vertical failure, the body that cannot stay upright forever. Love that only handles one axis leaves the other to tyrants.

He texted Joshua: *Reinvention is the point.*

Joshua: *Amen. Also do the washing up.*

Horizontal holiness. The dishes obeyed.
""",
    12: """
He read one careful page on aniconism and calligraphy and put the phone face down before certainty turned into a thread.

Not knowing fully was part of respect.

The moon, wherever it was, did not require his essay.
""",
    13: """
*Who is like God?* kept echoing as anti-slogan: not a boast, a check on the ego that wants to be the total while remaining a corner.

Michael made more tea and failed to be an archangel, successfully.
""",
    14: """
He almost asked who the number belonged to, then decided mystery was Gabriel's traditional branding.

*Keep going* remained on the lock screen like a small commandment that didn't shout.
""",
    15: """
He wrote in the notebook: *satire needs love or it becomes the thing it mocks.*

Then he drew a pie and labelled it HOLY GHOST in ironic capitals, smiled, and tore the page up before it became a personality.
""",
    16: """
He watched his hands type and thought: emergent from neurons, yes, *and* the typing is still the given. Emergence describes furniture arrangements. The room remains the room.

Joshua sent a meme about brains. Michael sent back a photo of tea. Both were data. Both were experience.
""",
    17: """
He tried predicting Joshua's next text and got it wrong. Delight followed. Prediction error as intimacy.

The world kept sending read receipts. Michael tried to say thank you more often, even to marmalade.
""",
    18: """
That night he dreamed of a slit experiment performed with pub stools. He woke laughing, which is peer review of a sort.
""",
    19: """
On a clear night he looked up and felt the hallway between stars as kinship rather than exile. Lonely, yes. Outside the building, no.
""",
    20: """
He told the bartender infinity was a process, not a pile. The bartender said the queue for the loo was both, and they raised glasses to applied mathematics.
""",
    21: """
Useful ghosts: imaginary numbers, fictional characters, future selves, God-talk as operator.

Michael stopped apologising for tools that work.
""",
    22: """
He watched ants make a city and refused to call them nothing-but. Levels are real. The field is real. Deletion is the cheap philosophy.
""",
    23: """
He left the whiteboard up for a week. Visitors assumed he was mad or brilliant. Both/and. He wiped it only when the maybe had done its kindness.
""",
    25: """
He drafted a message to Cameron that said *you don't have to catch up* and deleted the condescension, leaving *sleep well, thanks for the sandpaper.*

Different speeds. Same road. No race committee.
""",
    26: """
He put Adams and a Bible on the same shelf without asking them to agree about everything, only to share a wall—which they already did, being things.
""",
    27: """
He cleaned crumbs from between six and seven as if tending a small shrine of hardware humour, then typed a work email like a man who still lives in the ordinary.
""",
    28: """
He pinned Cameron's objection above his desk: *Not a formal paradox.*

Beside it: *Still funny. Still useful. Still a map of temples.*

The strong claim waited for the novel, not the courtroom.
""",
    29: """
In the morning Michael did not restart the argument. He let the friendship be larger than the glyph.

Refinement continued in silence, which is also a system of meaning.
""",
    30: """
He bookmarked one paper on paraconsistency and did not pretend to finish it. Intellectual hospitality includes unread tabs.
""",
    31: """
He practised: the cashier is not a mob. The slow walker is not defective code. Agency varies; dignity does not.

Kindness as epistemology.
""",
    32: """
He blocked an hour for recovery and labelled it *infrastructure*, not *weakness*. High agency includes maintenance windows.
""",
    33: """
One friend survived a twenty-percent unmasking. Michael noted the data point like treasure. Sample size: growing. Hope: cautious. Mask: still available, less absolute.
""",
    34: """
At the fork he chose a third path drawn in pencil: hard work *with* selected bonds. The recruiter in his head sulked, then took a tea break.
""",
    35: """
He sent Joshua the Mech correction paper. Joshua replied with a heart and a wolf emoji, which is how brothers do peer review.
""",
    36: """
Michael whispered to ω on a screen: *you're not hired to be hit.* The letter, being a letter, took the promotion well.
""",
    37: """
He wrote *is and isn't* on his hand in biro, washed it off before a meeting, and felt the ink's ghost remain—another useful non-existence.
""",
    38: """
He toggled fonts for fun: serif modest, sans rude, monospace bureaucratic. The joke peaked in the fonts of everyday messages. Of course the everyday held the secret. That's where existence lives.
""",
    39: """
He stood under a wooden telegraph pole—not a cross, not not a cross—and felt history's efficient shame and love's stubborn rebranding in the same upright.
""",
    40: """
No outside left meant no pure holiday from kinship with harm. It also meant no pure exile from mercy. Michael sat with both until his shoulders dropped a centimetre.
""",
    41: """
He made a private list: harms he needed to repair, not because a fence beyond existence demanded it, but because the field includes the harmed and the harmer as one weather system learning.

Responsibility without elsewhere is heavier and cleaner.
""",
    42: """
He reread the plank verse slowly, then his own old messages for timber. Found some. Apologised once where it still mattered. The chapter number smiled like a fox.
""",
    43: """
When the appointed hour returned another night, he treated it as liturgy without superstition: a rhythm for courage. The document opened. The hands typed. The field approved by not vanishing.
""",
    44: """
He sketched gold plates in the margin, then wrote *paint is fine* and *kindness first* and *the text is the treasure*. The fantasy bowed to ethics and still waved.
""",
    45: """
Next time the goosebumps came he said aloud, 'Noted,' like a scientist and a pilgrim sharing a coat.
""",
    46: """
He donated to a food bank without photographing it. Horizontal beam. No branding. The doorway in the ordinary stayed ordinary and sacred both.
""",
    47: """
Calling into being what was not: he wrote a paragraph that hadn't existed, watched it become a thing, and tipped his mug to Romans and kitchens alike.
""",
    48: """
Preference without outside made the present feel less like a trap and more like a gift that didn't need a cosmic receipt—ironically, given his old hunger for receipts like forty-two.
""",
    49: """
He walked and noticed pairs: inhale/exhale, step/stance, speech/listen. Generative duals without a war. Heat low, accurate, rising.
""",
    50: """
Someone online demanded he pick a team for God's pronouns. He closed the tab. The field does not fit in a jersey. Hospitality is not a dodge; it's the ontology.
""",
    51: """
He taped the numeral table above the desk:

α1 β2 … δ4 … ω800

Under it: *No counterfeit Classics. Jokes earned only.*
""",
    52: """
He did not text anyone 8==D. Some jokes are for the monogram's courtroom, not the group chat. Maturity is knowing which temple you're in.
""",
    53: """
Seven got a private toast: crooked cousins welcome. Families of meaning that exclude the bent ones become either/or cults.
""",
    54: """
Delta as tip and change and four: he traced Δ in the air and felt the book smile with all its teeth and none of its cruelty.
""",
    55: """
He zoomed a font specimen on screen until α and ω looked like what they look like. Sacred. Rude. Both. He zoomed out before the bus noticed.
""",
    56: """
Napkin under glass in his mind's museum: α==ω. Title. Diagram. Dare. Joshua's laugh still on it like varnish.
""",
    57: """
The other reading wasn't a retreat from the first; it was the axiom's insistence that the total not be half-castrated by prudery or half-blinded by phallic monopoly. Both altars. One monogram.
""",
    58: """
Not either/or: he wrote it on the last page of the notebook and left the rest blank for living.
""",
    59: """
Length girth depth breadth—he said them like a liturgy of axes. Existence has no preferred direction for the joke or the love.
""",
    60: """
No sin as outside-cut left him without a bin for enemies—and without a pedestal for himself. He sat in that democracy of the field until it felt like adulthood.
""",
    61: """
Same heartbeat: he put a hand on his chest and felt one pulse doing the work of two conclusions. Efficient. Intimate. Funny.
""",
    62: """
Fuck life / fucked by life: he and Joshua clinked mugs. Verbs as theology. Consent to the storm and the steering wheel both.
""",
    63: """
Has / is / maybe: they let the wave stay uncollapsed on purpose, like leaving a window open in summer. Big and small. Phew. Hmm. Amen adjacent.
""",
    64: """
For the still-sleeping parts of everyone—including him—he whispered: no rush that becomes cruelty. Wake as you can. The axiom already holds you. The monogram can wait five more minutes of kindness.
""",
    2: """
He wrote on a sticky note and stuck it to the fridge under a takeaway magnet:

*Nothing can't clock in without stealing existence's uniform.*

Joshua, visiting later, underlined *stealing* and wrote *borrowing, at best.*

Michael left both versions up. Both/and, even in pedantry.
""",
    3: """
That night he dreamed every door opened onto the same kitchen. He woke thirsty, drank water, and accepted the continuous field with a slightly sore neck.
""",
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
    for n, add in sorted(ADD.items()):
        p, title, body = load(n)
        if p is None:
            print("missing", n)
            continue
        key = add.strip().split("\n", 1)[0][:50]
        if key in body:
            print("skip", n)
            continue
        new_body = body + "\n\n" + add.strip()
        p.write_text(f"# Chapter {n}\n## {title}\n\n{new_body}\n", encoding="utf-8")
        added += len(add.split())
        touched += 1
        print(f"{n:02d} -> {len(new_body.split())}w")
    print(f"touched={touched} added_words~={added}")


if __name__ == "__main__":
    main()
