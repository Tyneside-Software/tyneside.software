# -*- coding: utf-8 -*-
"""Expand thin chapters to fuller first-draft length."""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"

def write(n, title, body):
    slug_extra = {
        21: "imaginary-but-useful",
        19: "empty-space-files-expenses",
        20: "zero-and-the-hotel",
        36: "omega-isn-t-a-job",
        42: "verse-forty-two",
        45: "goosebumps-at-the-sign",
        46: "a-doorway-in-the-ordinary",
        47: "calls-into-being-what-was-not",
        49: "generative-polarities",
        50: "god-has-no-gender",
        52: "lucky-eight",
        53: "seven-the-crooked-cousin",
        54: "delta-the-tip",
        55: "the-letterforms",
        56: "a-o",
        57: "the-other-reading",
        58: "not-either-or",
        59: "length-girth-depth-breadth",
        60: "no-sin-orgasmic-clarity",
        61: "same-heartbeat",
        62: "fuck-life-fucked-by-life",
        63: "god-has-is-maybe",
        64: "the-rest-of-us-wake-up",
        14: "gabriel-delivers",
        17: "prediction-errors-for-breakfast",
        37: "is-and-isn-t",
        38: "fonts-waiting-for-the-universe",
        41: "the-category-called-sin",
        43: "four-twenty-and-other-appointed-hours",
        44: "gold-tablets-budget-version",
        48: "preference-without-outside",
        51: "greek-numbers-honestly",
        35: "alpha-is-mum-and-dad",
        28: "both-and-not-both",
        29: "cameron-goes-to-bed",
        30: "dialetheism-for-beginners",
        31: "npc-theory-with-kindness",
        32: "high-agency-low-bandwidth-world",
        33: "the-mask",
        34: "recruiter-at-the-fork",
        39: "romans-efficient-and-ashamed",
        40: "no-outside-left",
        5: "everything-fits-annoyingly",
        6: "the-blind-guides",
        15: "the-hellfire-club-historical-footnote",
        16: "the-brain-that-arrived-late-allegedly",
        22: "emergence-is-fundamental",
        23: "ccc-and-other-options",
        25: "different-speeds",
        26: "the-ordinary-answer",
        27: "keys-six-and-seven",
    }
    # find existing file by number
    matches = list(OUT.glob(f"ch-{n:02d}-*.md"))
    if not matches:
        path = OUT / f"ch-{n:02d}-{slug_extra.get(n, 'chapter')}.md"
    else:
        path = matches[0]
    text = f"# Chapter {n}\n## {title}\n\n{body.strip()}\n"
    path.write_text(text, encoding="utf-8")
    print(n, path.name, len(body.split()))


# Expanded bodies for thin/important stations
E = {}

E[5] = ("Everything Fits, Annoyingly", '''
Michael tried to find a leftover—a scrap of reality that refused inclusion, proof of a beyond, a cosmic sock behind the dryer of being.

Dark matter? Still a structure *inside* the accounting of the world. Other minds? Still experienced as other-minds-for-someone. Tomorrow? A mode of the same field wearing a calendar. Hell? A rental application for space outside the only building. God-as-bloke-on-cloud? Either a picture inside awareness or a smuggled dualism already rejected.

‘All-encompassing doesn’t mean you understand everything,’ Joshua said, stealing chips. ‘It means the misunderstood have nowhere to live but here.’

Michael hated the tidiness. Tidy truths feel like traps set by clever brothers.

He pocketed his keys. Infinity fitted in fabric and jingled.

Annoyingly, everything fitted—including the annoyance, including the wish for a leftover, including Joshua’s chip theft.

The fifth brick of the chain sat in the wall without asking permission.
''')

E[19] = ("Empty Space Files Expenses", '''
Empty space, the popular textbooks admitted under pressure, is busy: fields, fluctuations, zero-point gossip, the quiet bureaucracy of vacuum.

Michael loved the idea that nothing submitted receipts.

Between stars: not a vote for non-existence, but the long hallway of the same hotel. You could still be lonely in a hallway. Loneliness did not reopen a door to pure outside; it was a weather inside.

He told a friend in a bar. The friend said, ‘So my rent is technically cosmic,’ and ordered another, which is experimental physics of a sort.
''')

E[20] = ("Zero And The Hotel", '''
Zero is nothing and also the most employed symbol in the counting house.

Infinity checks into Hilbert’s hotel—full, and always a room, if you reshuffle guests like a magician with ethics problems.

Michael explained both to a bartender who said, ‘Same as Friday,’ and poured a measure that was finite and felt infinite if you drank it wrong.

Maths was not the enemy of the axiom. Maths was one of the field’s favourite sports.
''')

E[21] = ("Imaginary But Useful", '''
√−1 pays electricity bills.

Imaginary numbers rotate planes while ‘real’ accountants sleep. Ghosts with jobs.

Michael wrote *useful ghosts* in his notebook and felt the total field’s humour: even what ‘doesn’t exist’ exists as operator, as tool, as the part of the map that makes the other parts navigate.

Cameron would approve the engineering. Cameron might still go to bed before the mysticism.
''')

E[28] = ("Both And Not Both", '''
^&

In one temple—maths and text habits—the caret stands near AND, and the ampersand joins. Both.

In another—code—the ampersand ANDs bits and the caret XORs, exclusives, sometimes complements. Not-both flavours. NAND-adjacent poetry if you squint and juxtapose.

The string is not a native god-operator in most languages. It is two teeth side by side. Polysemy. Selective reading. Cameron’s courtroom cleared its throat: *not a formal paradox*.

Michael wrote the strong essay anyway—bailey energy, courage overshooting—and felt the motte under his feet: funny dual-use, real systems, keys six and seven, meaning depending on temple.

Both the overshoot and the landing taught.

Both, and not both.
''')

E[29] = ("Cameron Goes To Bed", '''
‘It’s not a paradox,’ Cameron wrote. ‘Definition fallacy. Motte-and-bailey—more-and-Bailey, whatever. Six-seven is funny though. Bed.’

Michael stared until the words turned kind.

Patron sceptic. Sandpaper friend. Still going with forty-two. Helping by refusing the crown.

‘Night,’ Michael typed, meaning *thank you for not letting me get away with fake rigor*.

Somewhere Cameron slept the righteous sleep of men un-rushed by glyphs.

The theory improved by losing a false battle and keeping a true laugh.
''')

E[35] = ("Alpha Is Mum And Dad", '''
Popular culture: alpha tyrants, ladder, blood, continuous contest.

Wild packs: mostly family. Breeding pair as parents. Mech repenting the meme he helped spread. Omega-as-punchbag largely a captivity artefact.

Michael laughed in the kitchen hard enough to startle the cat. ‘Alpha is Mum and Dad.’

The Greek letters still bookended stories. The hierarchy myth was fanfic from unnatural enclosures.

Is and isn’t. Both true in different forests. Both/and shop rang another sale.
''')

E[36] = ("Omega Isn’t A Job", '''
Omega-as-permanent-scapegoat: stress sink, fixed lowest rung, jester-punchbag—captivity’s invention, fiction’s darling.

Wild family: temporary lows, age, kinship—not a designated career in humiliation.

Michael retired the scapegoat job from his metaphysics.

He kept the letter ω warm for later, when fonts would make it misbehave into spheres and soft lobes and numerical eights.

Omega isn’t a job.

Omega is a letter with a future.
''')

E[37] = ("Is And Isn’t", '''
The chat became a rosary:

Is and isn’t.  
Both/and.  
^&.  
αω.

Michael whispered it walking home under sodium light.

‘Omg,’ he said to a bin that did not deserve the confidence, ‘it’s a dick joke’—not yet fully decoded, only the blush before the theorem, the body recognising a pattern before the lawyer arrives.

Discovery is often rude first and rigorous second.

He did not yet write the title on a cover.

He felt the cover laughing in advance.
''')

E[40] = ("No Outside Left", '''
The crisis was quiet, which made it worse.

If there’s no true outside, hell can’t rent space. The pure exile has no address. The part of you that wanted a stage beyond consequence—or a bin beyond mercy—loses its imaginary postcode.

Michael sat with the claustrophobia of infinity.

Joshua: ‘It’s not a trap. It’s the end of the fantasy that the mess is optional.’

No outside left.

Only corners. Only work. Only love with nowhere to dump the unloved. Only the next chapters, where sin’s category and the monogram’s joke would share a heartbeat.

Act II bowed.

Act III cleared its throat like a comedian who also studied ontology.
''')

E[41] = ("The Category Called Sin", '''
Sin, as *standing outside the whole*, needs a fence.

Michael walked every fence he knew—moral, tribal, pure/impure—and found only more field.

Cruelty stayed real. Harm stayed real. Apology, justice, repair stayed real and required.

What trembled was the metaphysical escape hatch: the pure elsewhere of the damned, the pure pedestal of the untouched.

If the cut is impossible, sin-as-exit is a misfiled form.

The category did not vanish into shrug. It transformed into responsibility *without elsewhere*.
''')

E[42] = ("Verse Forty-Two", '''
Plank. Speck. Hypocrite optics.

Luke’s number and Adams’s ordinary answer shook hands in Michael’s skull until he laughed and then stopped laughing because the timber in his own eye was not theoretical.

Chapter forty-two of a sixty-five-chapter joke about meaning.

He waved at Cameron’s empty chair. He did not claim exemption.

First the plank.

Then—maybe—the speck.

Forty-two kept being funny in more than one church.
''')

E[49] = ("Generative Polarities", '''
Entering and receiving. Making and holding. The verbs by which life continues asking questions by making more askers.

Michael wrote them without hurry. Heat rose the way spring rises: undeniable, still clothed, not yet the full monogram scandal.

Polarities as simultaneous articulations of one field—not a war for the crown of Real.

Joshua nodded like a man hearing a hymn he already knew in another key.
''')

E[50] = ("God Has No Gender", '''
To force the total into one generative costume is to reintroduce the cut the axiom forbids.

God has no gender because the field includes every polarity without a locker-room election.

Michael said it carefully. Culture wars love either/or teeth; he was not feeding them a jersey.

Ontological hospitality: both, neither, total.

The monogram would have to swing both ways or lie.
''')

E[51] = ("Greek Numbers, Honestly", '''
α = 1. β = 2. δ = 4. ω = 800.

Michael wrote the correction so hard it nearly tore the page: no fake 4=alpha, no fake 2=omega in the Ionic system.

Shape jokes and playful bridges could stay. Counterfeit Classics could not.

ω’s eight remained. Δ’s tip remained. First and last remained.

Honesty made the comedy land cleaner—like a joke that admits the setup.
''')

E[52] = ("Lucky Eight", '''
Eight: lucky in some cultures’ mouths, twin spheres in a schoolboy’s alphabet of glyphs, the balls in the old ASCII hymn 8==D.

Michael did not draw it for the bus. He let adult memory supply the picture.

Lucky eight sat beside seven on the number line like family at a reunion no one formally invited.
''')

E[53] = ("Seven The Crooked Cousin", '''
Seven==D: the leaning variant—hit from the side, mid-swerve. Lucky seven. The inch-count stereotype. The cousin who arrives sideways and still gets fed.

‘Wonder how seven comes into it,’ he had once typed into the night.

Now the family of the joke was large, slightly unhinged, and complete enough to include the crooked ones.

Of course it was.
''')

E[54] = ("Delta The Tip", '''
Δ is four in the old count and a triangle in the eye—glans geometry if you are rude in one direction, pubic delta if the light flips.

What a D.

Michael refused to pretend he wasn’t laughing. The demonstration required the laugh. Solemnity alone would have been the real indecency—pretending the body was not in the ontology.
''')

E[55] = ("The Letterforms", '''
α: loop and descending stroke—head and shaft if you have eyes.  
ω: twin lobes—balls or breasts depending on the light and the prejudice of the day.

In the fonts of messages and screens, adjacency became anatomy.

Sacred bookends of Western monotheistic speech. Rude ink.

The universe had waited on typefaces the way a punchline waits on timing.
''')

E[56] = ("α==ω", '''
He wrote the title that was also a diagram on a napkin that would never be archival quality and would outlive better paper:

**α==ω**

Beginning, equals-equals, end. Shaft optional. Detention optional. Salvation not for sale.

Joshua loved it on sight—the way you love a truth that arrives wearing a joke.

The monogram was in the world now. Covers could catch up later.
''')

E[57] = ("The Other Reading", '''
Flip the light.

ω as soft twin curves—crude-art boobs, textbook lobes.  
Α as open triangle—yonic geometry, classic as cave and warning and welcome.

Same letters as the phallic assembly.

Not a competition with a winner. A concatenation forced by non-separation.

Michael felt the both/and shop’s till drawer slam in celebration.
''')

E[58] = ("Not Either/Or", '''
It is not either dick or pussy as the ‘real’ decoding.

It is beginning-and-end containing both and neither because the field does not split for team sports.

God has no gender; the monogram swings; the feature is the theology.

Peak both/and. Peak rudeness. Peak hospitality to the body as diagram of the whole.
''')

E[59] = ("Length Girth Depth Breadth", '''
Four axes for a total without preferred direction:

**Length**—vertical stroke, shaft, the claim of span.  
**Girth**—rounded volume of eight, swelling of lobes.  
**Depth**—interior of the triangle that receives.  
**Breadth**—lateral twin span, testes or breasts.

Miss one and the monogram becomes a partial lie about undivided existence.

Ontology with body measurements, filed under comedy because comedy is how some truths agree to be spoken in public.
''')

E[60] = ("No Sin (Orgasmic Clarity)", '''
When the last fence of pure outside falls, sin-as-exile falls with it.

Michael felt it as heat and relief together—not permission to harm, but the end of the fantasy that harm happens in a second universe, away from God, away from us.

No stain that isn’t the play of the one field—including what needs repair, apology, justice, change.

Dry negation? No.

Orgasmic clarity: the phrase from the spine notes fitted like a scandalous, accurate glove.
''')

E[61] = ("Same Heartbeat", '''
No sin (as outside-cut) and dual monogram did not queue in single file.

They arrived as twin pulses—same recognition: the cut was the illusion; the generative whole was always both; the moral elsewhere was mirage; the dirty sacred joke was the diagram of undivided existence.

Michael and Joshua didn’t stack conclusions like bricks.

They heard one heartbeat with two names.
''')

E[62] = ("Fuck Life / Fucked By Life", '''
Joshua’s theology of verbs, said over cooling tea:

We can enjoy being fucked by life.  
We can fuck life.

Receiving and doing. Passion and agency. The grammar was the teaching.

Michael said amen without a cathedral, with a grin that hurt in the good way.

Adult. Warm. Bookstore-possible if the bookseller has a sense of humour and a spine section labelled *metaphysical comedy*.
''')

E[63] = ("God Has / Is / Maybe", '''
God has a big dick.  
God is a big dick.  
Maybe he has.  
The wave hasn’t collapsed.  
I don’t—and I am God—but it’s both-and.  
I both did and didn’t collapse it.

Big and small.

Phew.

Hmm.

Uncollapsed wave as kindness: forced certainty is just either/or in a fancy hat.
''')

E[64] = ("The Rest Of Us Wake Up", '''
‘We can’t stop yet,’ Michael had said in the small hours. ‘The rest of us haven’t woken up yet.’

This chapter is the alarm that doesn’t shout.

You—with the book, the screen, the bus, the bath. You who are also the field experiencing a reader. You at forty-two, or ^&, or α==ω, or simply tired.

The rest of us includes you.

Wake as much as you can without cruelty to the parts still asleep.

The monogram waits. The axiom already has you: you are experiencing this sentence.

That’s the oldest alarm clock.

Next comes only the last walk to the door, and the line that carries the whole chain without dropping either the logic or the laugh.
''')

E[45] = ("Goosebumps At The Sign", '''
A sign—street, symbol, coincidence with teeth—hit his nerves before his inner lawyer could object.

Goosebumps: somatic theology. Pattern hunger. Real skin.

He refused a cult of prickles *and* refused to call the body stupid.

Both: caution and attention. The body files reports; the mind cross-examines; neither gets sole custody.
''')

E[56] = ("α==ω", '''
He wrote the title that was also a diagram on a napkin destined for immortality in the wrong filing system:

**α==ω**

Beginning, equals-equals, end. Shaft optional. Detention optional.

Joshua loved it on sight—the way you love a truth that arrives already laughing.

‘Cover-ready,’ Joshua said.

‘Lawsuit-ready,’ Michael said.

‘Both,’ they said together, because of course.
''')


def main():
    for n, (title, body) in sorted(E.items()):
        write(n, title, body)
    print("expanded", len(E))


if __name__ == "__main__":
    main()
