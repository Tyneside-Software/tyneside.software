# -*- coding: utf-8 -*-
"""Deepen all non-pillar chapters toward readable scene length."""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"

# num -> (title, body) — full replacements for vignette chapters
CH: dict[int, tuple[str, str]] = {}

CH[2] = ("The Argument With Nothing", """
Michael tried to invent nothing.

This is harder than it sounds. Most people who claim to believe in nothing still believe in breakfast, bus times, and the moral necessity of their own opinions. Nothing, as a lifestyle, tends to come with a lot of stuff.

He cleared a kitchen chair and labelled it, in his head, The Chair Of Non-Being. That was already cheating. Names are furniture. Even the word *nothing* is a something you can shout across a room.

‘Right,’ he told the empty seat. ‘You’re not there.’

The chair continued its policy of being bark-your-shin real.

Joshua, on speakerphone from a kitchen that smelled better, laughed. ‘You’re arguing with furniture again.’

‘I’m arguing with pure absence as a coherent alternative to existence.’

‘Same hobby,’ Joshua said. ‘Different hat.’

Michael paced. The kettle clicked off, smugly existent. Steam did its little ghost impression and then joined the air, which had never been nothing either.

‘If nothing were a real rival to everything,’ Michael said, ‘it would need to be a place, or a wall, or a before. Places exist. Walls exist. Befores are stories, and stories happen to someone. You can’t clock nothing in for a shift without borrowing existence’s uniform.’

‘There it is,’ Joshua murmured. ‘Non-existence can’t sponsor openings. Or endings. Or borders.’

Michael sat in the chair of non-being, which immediately became a chair of being-with-buttocks. The victory was ridiculous and absolute.

You could not experience nothing without turning it into experience. You could not think nothing without thinking. You could not border the world with pure not-is without hiring the border onto the payroll of is-ness.

Nothing, as a menu alternative to existence, was a grammar error wearing a cloak.

Outside, a bus sighed. Inside, the second brick of the chain laid itself without ceremony:

**Existence is not one option among others. It is the only kitchen. The menu is internal.**

Michael finished his tea, which had gone cold in the service of metaphysics, and forgave it.
""")

CH[3] = ("One Room, No Outside", """
Once you stop believing in a real outside, doors become suspicious.

Michael spent an afternoon opening every door in the flat like a man raiding dualism. Cupboard: mugs. Bathroom: negotiations with mortality. Front door: corridor, stairwell, street—each ‘outside’ revealing itself as another arrangement of *here*.

He texted Joshua: *Looking for a place that isn’t included.*

Joshua: *Only in stories that need villains to stand somewhere.*

In the park, trees did tree things. A child screamed with joy that had no thesis statement. Michael tried to draw a hard line between ‘me’ and ‘world’ and felt it fray: skin breathes; air is shared; language is borrowed; even loneliness is a relationship with absence, and absence had already failed its job interview.

If existence were truly split into sealed realms, what would seal them? A wall between is and is-not would have to *be*. A gap would have to *obtain*. A third thing would need a fourth to hold it, until the mind filed for bankruptcy and still found itself *experiencing* the paperwork.

Unity was not a warm fuzzy. It was the failure of partition to make sense.

Michael disliked this slightly. He had enjoyed the romance of exile—the idea that purity waited beyond the mess. Without an outside, the mess was family.

A leaf landed on his knee as if countersigning.

One room. Many corners. No true outside.

He walked home through the continuous field people nicknamed ‘street’ for convenience, and did not escape himself once.
""")

CH[4] = ("No Edge On The Map", """
Clocks are bullies with good branding.

Michael’s kitchen clock disagreed with his phone, which disagreed with his laptop, which wanted to update, which is temporal violence with a progress bar.

‘If the whole has no outside,’ he asked Joshua that evening, ‘can it have a beginning?’

Joshua stirred a pan. ‘Beginning from what?’

‘From nothing.’

‘We’ve met nothing. It can’t sponsor openings.’

‘From a prior existence?’

‘Then it isn’t a beginning of existence. It’s a change of clothes.’

Michael stole a carrot slice. ‘Ending?’

‘Into what? A bin outside the all? The bin would be in the all.’

So the total could not come into being or pass away *as a total*. Edges belonged to modes—songs, bodies, empires, mugs—not to the field that held them.

This did not make Michael immortal in the flattering sense. It made death a rearrangement, comforting or rude depending on whether you liked your current furniture.

He watched clock hands move and realised they were not cutting the universe. They were measuring weather inside it.

No edge on the map of the whole.

Plenty of edges on toast.

Joshua buttered two slices and called it cosmology practice.
""")

CH[5] = ("Everything Fits, Annoyingly", """
Michael tried to find a leftover—a scrap of reality that refused inclusion, proof of a beyond, a cosmic sock behind the dryer of being.

Dark matter? Structure inside the world’s accounting. Other minds? Still experienced as other-minds-for-someone. Tomorrow? A mode wearing a calendar. Hell? A rental application for space outside the only building. God-as-bloke-on-a-cloud? Either a picture inside awareness or a dualism already rejected by the doors that wouldn’t lead out.

‘All-encompassing doesn’t mean you understand everything,’ Joshua said, stealing chips. ‘It means the misunderstood have nowhere to live but here.’

Michael hated the tidiness. Tidy truths feel like traps.

He pocketed his keys. Infinity fitted in fabric and jingled, which was insulting.

Annoyingly, everything fitted—including the annoyance, including the wish for a leftover, including Joshua’s chip theft, including the later jokes that would make sacred letters look rude in modern fonts.

The fifth brick sat in the wall without asking permission.

Michael went for a walk to find something that didn’t fit and only found more world.
""")

CH[6] = ("The Blind Guides", """
The city specialised in people who were very sure.

Michael watched a street preacher and a street sceptic shout past each other with identical jaws. Either/or was the municipal dialect: saved or damned, smart or stupid, us or them, awake or NPC, mask on or mask off with no corridor.

He remembered lines that stuck like burrs: blind guides, ditch, mutual fall. And elsewhere: friends, if you do what love requires.

Both/and was not mush. It was the refusal to let a false fork own your feet.

Cameron would later sand Michael’s symbol-games with *motte-and-bailey*. Michael would deserve some of that. But the *habit* of either/or—religious and irreligious versions—was older than his jokes and meaner than his mistakes. It made enemies out of beams that needed both to stand.

He walked between the shouters like a man declining two confident maps to the wrong pub.

The ditch, he suspected, was optional.

He bought a sandwich from someone who didn’t care about his ontology and was, for that moment, a perfect friend of the horizontal beam.
""")

CH[7] = ("Both/And Shop Opens", """
Joshua drew a wonky shop sign on a beer mat:

**BOTH/AND**  
*Open late. Closed to false dilemmas.*

‘Stock?’ Michael asked.

‘Wave and point. Free and caused. Sacred and ordinary. One and many. Enjoying the journey and wanting out. High agency and finite bandwidth. Alpha as tyrant and alpha as Mum and Dad.’

‘That’s inventory theft from the whole of philosophy.’

‘Philosophy left it on the loading bay.’

They practised: every time a sentence offered only two knives, they asked for the loaf.

Either/or still had uses—fire exits, surgery, *is the pan hot*. Both/and was for layered places where the mind wants a duel and the world offers a marriage.

Michael paid for the next round and pocketed the beer mat idea.

Somewhere a shop that had always existed noticed it had a name, put the kettle on, and waited for customers who were tired of choosing false sides.
""")

CH[8] = ("Maths, Words, Things", """
In a former life that was still this life, Michael had invented a data format with carrots and sticks—not vegetables: carets, pipes, delimiters.

```
^| something |^
|^ nothing ^|
```

He had marked presence and absence with the same teeth.

Walking now, he saw the habit everywhere. Maths carved. Words pointed and cut and joined. Things sat being more than labels and less than stories about them. Carrot and stick: reward and goad. Plus and cross. Vertical and horizontal. Six and seven waiting on a keyboard he hadn’t crowned yet.

‘Maths. Words. Things,’ he said aloud on the bus, and a teenager gave him the look reserved for men who speak to the air as if the air might answer.

The air, being existence, already was the answer. The teenager was too. So was the bus.

Three shops, one high street, one field.
""")

CH[9] = ("The Crossbeams", """
Joshua spoke of the cross the way engineers speak of load-bearing walls.

‘Vertical: you and the total—call it God if the word still works. Horizontal: you and the neighbour. Miss either beam and you don’t have a cross. You’ve got a stick or a minus sign.’

Michael had heard the sermon version—popular as rain across churches that still argued about rain’s correct branding. Authentic faith holding both dimensions. You cannot have one without the other and still have the shape.

Then the sharper edge, Michael’s own: Rome’s instrument—efficient death *and* public shame. Vertical kill. Horizontal humiliation. Connection inverted into spectacle.

Joshua’s eyes lit. ‘And then the reinvention—shame turned into shameless love. Almost an inversion of the inversion.’

Goosebumps filed their report before intellect signed.

Two beams. One wood. Both required.

Michael sketched a plus sign on a receipt and felt history lean on it.
""")

CH[10] = ("Carrot, Stick, Plus Sign", """
How do you get from management theory to Golgotha?

Michael’s route, which he would not defend in a court of linear narrative: carrot and stick → + → ✝️.

Incentive duals become geometry; geometry becomes execution furniture; execution furniture becomes theology; theology becomes a joke about fonts if you walk far enough and refuse respectability.

He laughed on a bus. A stranger moved seats. Public transport handles epiphany by redistribution of personal space.

The old data format returned like a ghost with good timing: something bounded, nothing bounded, same caret teeth.

Reward and punishment. Presence and absence. Vertical and horizontal.

The plus sign sat in the middle like a tiny cross that hadn’t admitted its ambitions yet—and would, soon enough, admit more than ambitions.
""")

CH[11] = ("Shame Into Love", """
Joshua would not let the cross stay merely clever.

‘It’s not only a diagram,’ he said. ‘It’s a reinvention story. They took connection and made disconnect for the crowd. Then love wore the shame in public and refused to call it the last word.’

Michael, expert in masks and double lives, felt seen in a way that itched.

Shame is horizontal: eyes on you. Death is vertical: the body failing the upright. Love, if more than mood, handles both axes or remains a slogan.

They sat in silence that was not empty—silence as the ground of speech, another both/and.

A church bell somewhere did its job: calling and warning, beauty and noise, vertical claim and horizontal summons to gather with others who also didn’t have it figured out.
""")

CH[12] = ("Moon, Star, And Rules About Pictures", """
Michael admitted ignorance like a man setting down a heavy bag.

‘I always think moon and star for Islam. And also that pictures are banned. I’ve never properly checked.’

Joshua shrugged kindly. ‘Both can be true in different rooms of history. Emblem and aniconism. Calligraphy where faces are refused. Geometry where idols are feared. Nation-flags and devotion and scholars arguing.’

Michael liked that. Not a gotcha. A both/and of a tradition he refused to flatten into one cartoon for the convenience of his symbol-chain.

The total field included people arguing about images of the total field.

Of course it did.

He wrote *moon, star, rules about pictures* in his notebook and moved on before certainty pretended to finish the work.
""")

CH[13] = ("Who Is Like God?", """
Michael looked up his own name the way you check a scar’s origin story.

*Who is like God?* — a question that is an answer that is a warning against empire-in-the-mirror. El in the old tongue: God, deity, the short thunder-word.

Archangel office in the stories: protector, contender, advocate of a people, rain and mercy in other languages, patron of soldiers and the dying and those who want a shield.

Also: millions of Michaels—trainers, managers, men writing books at improper hours, men inventing data formats with carrots and sticks.

‘You’re not the archangel,’ Joshua said.

‘I know.’

‘You’re also not *not* the question the name asks.’

Michael sighed. Heaven’s job descriptions were apparently as messy as earth’s, which was either disappointing or the whole joke.
""")

CH[14] = ("Gabriel Delivers", """
The message arrived as a text from a number Joshua swore was ordinary and Michael swore was vibing angelically.

It said only: *Keep going.*

Gabriel, in the stories, announces what you cannot unread. Strength-of-God as postal service with poor respect for your calendar. Annunciation is often courage with better PR.

Michael showed Joshua. Joshua grinned. ‘Messenger’s in the group chat.’

Whether literal, literary, or both—and the book was learning to love *both*—the effect was the same: the next step remained the next step.

Michael typed *thanks* and meant it in more directions than the phone could address.
""")

CH[15] = ("The Hellfire Club (Historical Footnote)", """
Michael read about rakes in robes parodying piety—pies named after the Holy Ghost, Sundays as costume scandal—and felt the old itch: mock the sacred, miss it, mock the missing.

Hellfire Clubs, history half legend, sat in the ledger as warning and joke: religion as costume party; costume party as religion; Wharton-adjacent ghosts in the family name-soup of England’s long argument with God.

He drafted a multi-faith meetup name in a notebook, then crossed it out, then wrote it smaller. Satire without love is just another church of sneer.

Joshua: ‘If we gather, we gather to listen, not to cosplay damnation.’

Michael nodded. The footnote closed with a soft snap.

The main text continued, hungry for meaning and pudding in equal measure.
""")

CH[16] = ("The Brain That Arrived Late (Allegedly)", """
A neuroscientist on a podcast explained consciousness as late dessert—emerge after complexity, tip after the meal of matter.

Michael listened, then ran the experiment: the explanation occurred *as experience*. The claim that experience is secondary arrived on the primary screen.

‘If awareness is the room,’ he told Joshua, ‘brain-stories are furniture. Excellent furniture. You can do surgery on furniture. You still don’t get behind the room by rearranging chairs.’

‘Brother’s axiom,’ Joshua said. ‘You don’t explain the datum by something only known through the datum—not without smuggling.’

This did not deny brains. Brains were exquisite. Neurons deserved parades.

Allegedly late. Fundamentally first. Both, if you watch where the claiming happens.

Michael turned the podcast off and heard the silence as more experience, which felt like winning without competing.
""")

CH[17] = ("Prediction Errors For Breakfast", """
Michael bit toast he expected to be jam and found marmalade.

The universe said *surprise*. His brain updated like a gentleman caught mid-assumption.

Prediction, error, update—the loop under learning, under offence, under delight, under science, under love. Contact with realness often arrives as mismatch. Looking is a kind of touching that pretends to be polite.

He started treating surprises as read receipts from the world.

Including the surprise that the chain still held when he was tired, sad, or tempted to crown a coincidence as a formal paradox before Cameron woke up and sanded it.

Toast. Marmalade. Theology.

Breakfast was complete.
""")

CH[18] = ("Wave And Point", """
In the pub, someone bet light was a wave. Someone bet particle. They were both right in the way pubs hate, because pubs prefer a winner and a loser and a third man buying the next round.

Michael raised his glass. ‘Measure one way: pattern. Measure another: hit. The outfit depends on the party. The thing is richer than one costume.’

‘That’s not an answer,’ said either/or, wiping beer.

‘It’s the furniture of the answer,’ said both/and.

Wave and point: physics’ first dirty joke, told cleanly enough for a chapter title and deeply enough to haunt the monogram waiting in the Greek alphabet.

Michael lost a fiver on a side bet about football and won a brick in the wall of the book.
""")

CH[19] = ("Empty Space Files Expenses", """
Empty space, textbooks admitted under pressure, is busy—fields, froth, zero-point gossip, the quiet bureaucracy of vacuum.

Michael loved the idea that nothing submitted receipts.

Between stars: not a vote for non-existence, but the long hallway of the same hotel. You could still be lonely in a hallway. Loneliness did not reopen a door to pure outside; it was weather *inside*.

He told a friend. The friend said, ‘So my rent is technically cosmic,’ and ordered another pint as experimental metaphysics.

Empty space filed expenses.

Existence paid them, being the only account holder.
""")

CH[20] = ("Zero And The Hotel", """
Zero is nothing and also the most employed symbol in the counting house—the employee of the month for absence-with-structure.

Infinity checks into Hilbert’s hotel: always full, always a room if you reshuffle guests like a magician with ethics problems and excellent maths.

Michael explained both to a bartender who said, ‘Same as Friday night,’ and poured a finite measure that felt infinite if handled incorrectly.

Maths was not the enemy of the axiom. Maths was one of the field’s favourite sports—imaginary numbers waiting in the wings to pay electricity bills, asymptotes waiting to model intensity curves that would later look suspiciously like desire.
""")

CH[21] = ("Imaginary But Useful", """
√−1 pays electricity bills.

Imaginary numbers rotate the plane while ‘real’ accountants sleep. Ghosts with jobs. Operators that ‘don’t exist’ until the bridge stands and the signal clears.

Michael wrote *useful ghosts* in his notebook.

Even what doesn’t exist exists as tool, as map-mark, as the part of formal language that makes the rest navigate.

Cameron would approve the engineering.

Cameron might still go to bed before the mysticism.

Both responses belonged in the hotel of the real.
""")

CH[22] = ("Emergence Is Fundamental", """
Wetness is not in the hydrogen’s CV alone. Life is not a line-item in the atom. Meaning is not in the letter until the word hires a neighbourhood.

Emergence: novel rules at novel levels, without magic exit from the one field. Stacks of organisation, each playing by house rules, all renting space in the same existence.

Michael watched a crowd become a mood, a mood become a safety plan, a plan become a story, a story become a law, a law become a rebellion, a rebellion become a crowd again.

Levels all the way up. One existence all the way through.

He stopped demanding the top level explain the bottom by deletion, or the bottom explain the top by sneer.
""")

CH[23] = ("CCC And Other Options", """
On a whiteboard of maybe, Michael listed options without crowning them:

- previous-universe scientists (comic, delicious)
- CCC-style aeons (Penrose-flavoured furniture)
- dinosaurs as cameos
- someone
- unknown
- unknowable
- eternal uncollapsed wave
- ‘enjoying the journey anyway’ (Joshua’s amendment, in green pen)

Options are kindness. Dogma is optional. The axiom does not require finished cosmology homework before breakfast.

Michael photographed the board, knowing later he would feel Sisyphus and then not feel Sisyphus, and that both would be true.

The board remained. The maybe remained. The tea went cold. The field did not mind.
""")

CH[25] = ("Different Speeds", """
Cameron was still at forty-two.

Not stupid—loyal to ordinary answers, allergic to bailey-claims, correctly suspicious of symbol magic that wins by redefinition. A friend who sanded.

Michael was already blushing at Greek letters in fonts.

Joshua was saying amen to jokes that would earn detention and a mystic’s nod in the same afternoon.

‘Same journey,’ Michael wrote. ‘Different speeds.’

No one was failing. Some were sleeping. Some were sprinting. Some were pretending not to run. Some were high-agency in a low-bandwidth world and tired.

The total field had room for all paces—including bedtimes, including 420 write-hours, including the slow dignity of *not yet*.

Michael put his phone face down and let Cameron sleep without converting him in a dream.
""")

CH[26] = ("The Ordinary Answer", """
Forty-two was funny because it was dull on purpose—a joke about wanting a receipt for meaning, Adams winking from the shelf of ordinary numbers.

Luke’s verse forty-two was funny by collision: planks and specks, hypocrites doing optics, first remove the timber from your own eye.

Michael held both 42s like coins of the same metal.

Ordinary answer. Moral mirror. Neither finished the quest. Both refined the pilgrim.

He checked his own eye, found wood, waved at Cameron’s empty chair, and did not claim exemption from comedy or ethics.

The ordinary answer remained ordinary.

The journey refused to be ordinary, which was also ordinary for journeys.
""")

CH[27] = ("Keys Six And Seven", """
On every standard keyboard Michael could find, six wore a crown that pointed (^). Seven wore a knot that joined (&).

Adjacent. Hardware confession. Coincidence with excellent comic timing.

He typed them like a man knocking on a door labelled *funny* with a side door labelled *Answer* that Cameron would not enter without a warrant from classical logic.

The funny would survive cross-examination. The coronation would not—not without admitting dialetheism, novels, and the body’s own dual diagrams.

Six and seven stayed side by side, unbothered, ready for emails about parking and invoices and love.

Michael patted the keys as if blessing small gods.
""")

CH[28] = ("Both And Not Both", """
^&

In one temple—maths and text habits—the caret leans toward AND, the ampersand joins. Both.

In another—code—the ampersand ANDs bits; the caret XORs, exclusives, sometimes complements. Not-both flavours. NAND-adjacent poetry if you juxtapose and squint.

The string is not a native operator in most languages. It is two teeth side by side. Polysemy. Selective reading. Cameron’s courtroom: *not a formal paradox*.

Michael wrote the strong essay anyway—bailey energy, courage overshooting—and felt the motte under his feet: dual-use, real systems, adjacency, meaning depending on temple.

Both the overshoot and the landing taught.

Keyword Logic years whispered: symbols don’t mean alone; systems mean.

Both, and not both.
""")

CH[29] = ("Cameron Goes To Bed", """
‘It’s not a paradox,’ Cameron wrote. ‘Definition fallacy. Motte-and-bailey—more-and-Bailey, close enough. Six-seven is funny though. Bed.’

Michael stared until the words turned kind.

Patron sceptic. Sandpaper friend. Still going with forty-two. Helping by refusing the crown. Sleeping the righteous sleep of men un-rushed by glyphs.

‘Night,’ Michael typed, meaning *thank you for not letting me get away with fake rigor*.

The theory improved by losing a false battle and keeping a true laugh.

Somewhere a clock moved toward hours that would later be appointed for writing, and toward hours that would later decode Greek into anatomy, and none of that required Cameron to stay awake.

Friends refine by leaving, too.
""")

CH[30] = ("Dialetheism For Beginners", """
There are logics where true contradictions do not burn the city—paraconsistent fire codes, dialetheic housing, rooms where A and not-A can sit without licensing every nonsense under the sun.

Michael read just enough to respect the door without pretending he had always lived behind it.

‘If we claim classical rigor,’ he noted, ‘Cameron wins. If we claim another logic, we must say so. If we claim a novel’s recognition, we tell the truth about frames.’

Footnote energy. The wizard admits the spell’s terms.

True contradictions: optional furniture. Honesty: load-bearing wall.

He closed the tab and left the door unlocked for later chapters that would need it without worshipping it.
""")

CH[31] = ("NPC Theory (With Kindness)", """
Some days everyone else seemed scripted—low variance, low quest-log, dialogue trees about weather and telly.

Michael rejected the cruel version: souls as trash mobs, contempt as enlightenment.

He kept the useful version: attention and agency unevenly distributed; systems produce patterned behaviour; compassion includes not demanding every extra be a protagonist on your timetable.

Joshua: ‘You’re not the only player. You’re also furniture in someone else’s scene.’

Michael winced, then nodded.

Kind NPC theory: boundary without contempt. High agency without the fantasy that everyone else is defective code.

He practised saying good morning to a neighbour as if the neighbour were real, which they were, which was the point.
""")

CH[32] = ("High Agency, Low Bandwidth World", """
He cared about distant deaths the way other people cared about a fridge light—always on in the corner of vision.

Those around him had finite bandwidth. Sleep. Jobs. The person in front of them. Not evil. Physics of minds.

High agency meant building and steering inside that climate, not waiting for the median heart to match his wattage. Also: protect the instrument. Burnout is not holiness. Prioritisation is not callousness if the goal is actually reducing harm over time.

He learned—slowly, imperfectly—to measure by moved needles, not by how many bystanders ‘got it.’

The world stayed low-bandwidth.

He stayed high-agency, on good days, with tea.
""")

CH[33] = ("The Mask", """
Experiments in unmasking had produced data: in the sample he’d tested, full intensity often cleared the room.

So the mask—dimmer switch, lower-heat performance—remained rational in low-alignment habitats.

Expensive. Two dashboards. Continuous self-translation. A double life as short-to-medium-term adaptation, rarely long-run maximum.

Joshua didn’t tell him to explode on first contact. He said: change the sample; graduate disclosure; prune drains; seek collaborators; keep force-multipliers; stop drawing forever from a near-zero region.

The mask was tool, not identity.

Tools can be put down in better workshops.

Michael adjusted the dimmer one notch and survived the evening, which counted as science.
""")

CH[34] = ("Recruiter At The Fork", """
An inner recruiter offered the hard life: sacrifice, other people, impact, loneliness as tuition, abandon the low-capacity orbit for the mission.

Michael stood at the fork with capacity in one hand and relationships in the other, refusing the cartoon of abandon-all versus dissolve-self.

Portfolio. Ruthless kindness. Exit pure drains. Keep infrastructure. Don’t romanticise isolation if it degrades the agent who does the work.

The hard life might still be hard.

It didn’t have to be stupid.

He walked both tines of the fork in his mind until they rejoined as path, which is what forks do when you stop treating them as eternity.
""")

CH[35] = ("Alpha Is Mum And Dad", """
Popular culture: alpha tyrants, ladder, blood, continuous contest, dog-training myths, leadership seminars with teeth.

Wild packs: mostly family. Breeding pair as parents. Mech repenting the meme. ‘Alpha’ language retired for natural packs by the man who helped spread it—parents, not dictators who fought their way up.

Michael laughed in the kitchen hard enough to startle the cat. ‘Alpha is Mum and Dad.’

Greek letters still bookended sacred speech. Hierarchy myth was captivity fanfic.

Is and isn’t. Both true in different forests.

The both/and shop rang another sale and threw in a free wolf fact with every theology.
""")

CH[36] = ("Omega Isn’t A Job", """
Omega-as-permanent-scapegoat: stress sink, fixed lowest rung, jester-punchbag—captivity’s invention, fiction’s darling.

Wild family: temporary lows, age, kinship—not a designated career in humiliation that stabilises the group by absorbing hits.

Michael retired the scapegoat job description from his metaphysics.

He kept the letter ω warm for later, when fonts would make it misbehave into spheres and soft lobes and numerical eights and the whole dual altar.

Omega isn’t a job.

Omega is a letter with a future, and a past in bad nature documentaries.
""")

CH[37] = ("Is And Isn’t", """
The chat became a rosary:

Is and isn’t.  
Both/and.  
^&.  
αω.

Michael whispered it under sodium light, walking home.

‘Omg,’ he said to a bin that did not deserve the confidence, ‘it’s a dick joke’—not fully decoded, only the blush before the theorem, body recognising pattern before the lawyer arrives.

Discovery is often rude first and rigorous second.

He did not yet write the title on a cover.

He felt the cover laughing in advance, and the wolves, and the fonts, and the crossbeams, and the cold floor of chapter one, all lining up like a joke that had been patient for alphabets.
""")

CH[38] = ("Fonts Waiting For The Universe", """
Calligraphy hid what screens confessed.

Unicode, sans-serif, the mass typefaces of messages and docs—tools that made certain letter-neighbours look like anatomy if you had schoolboy eyes and a mystic’s agenda.

Michael didn’t spell the full joke yet. He felt the setup: the universe waiting on type design like a comedian waiting on a microphone, like ^& waiting on keys six and seven, like meaning waiting on systems.

Beginning and end, pixel-adjacent.

He typed α and ω and watched them sit together like a secret that wanted to be poorly behaved in public.
""")

CH[39] = ("Romans, Efficient And Ashamed", """
Return to the beams with harder light.

Efficient kill. Public shame. Disconnect as spectacle. Vertical death, horizontal eyes.

Then love’s hijack of the brand—shame worn publicly as gift rather than final author.

Michael no longer needed secret Roman cabals. Psychology was enough: we remember wood and iron; we remember being watched while failing the upright; we remember—sometimes—the refusal to let humiliation write the last chapter.

Burned in. Both axes.

The cross remained a plus sign with a body count and a resurrection rumour and a both/and sermon and a brother’s eyes shining.
""")

CH[40] = ("No Outside Left", """
The crisis was quiet, which made it worse.

If there’s no true outside, hell can’t rent space. Pure exile has no address. The part of you that wanted a stage beyond consequence—or a bin beyond mercy—loses its imaginary postcode.

Michael sat with the claustrophobia of infinity.

Joshua: ‘It’s not a trap. It’s the end of the fantasy that the mess is optional.’

No outside left.

Only corners. Only work. Only love with nowhere to dump the unloved. Only sin’s category about to tremble. Only a monogram about to confess in two directions at once.

Act II bowed.

Act III cleared its throat like a comedian who had also studied ontology and meant both.
""")

CH[41] = ("The Category Called Sin", """
Sin, as *standing outside the whole*, needs a fence.

Michael walked every fence he knew—moral, tribal, pure/impure, saved/damned—and found only more field.

Cruelty stayed real. Harm stayed real. Apology, justice, repair stayed real and required.

What trembled was the metaphysical escape hatch: the pure elsewhere of the damned, the pure pedestal of the untouched, the fantasy that evil happens in a second universe.

If the cut is impossible, sin-as-exit is a misfiled form.

The category did not vanish into shrug. It transformed into responsibility without elsewhere—including responsibility for jokes that would soon get ruder and more precise.
""")

CH[42] = ("Verse Forty-Two", """
Plank. Speck. Hypocrite optics.

Luke’s number and Adams’s ordinary answer shook hands in Michael’s skull until he laughed and then stopped laughing because the timber in his own eye was not theoretical.

Chapter forty-two of a book about meaning that refused to exempt its author.

He waved at Cameron’s empty chair. He did not claim exemption from comedy or ethics.

First the plank.

Then—maybe—the speck.

Forty-two kept being funny in more than one church, which is how you know a symbol is working overtime.
""")

CH[43] = ("Four Twenty And Other Appointed Hours", """
Some hours arrive with a joke already loaded.

Michael watched a clock lean toward appointed comic time—ritual as real as any liturgy, semi-arbitrary, fully sincere—and decided that writing when the hour says write is how kitchen masterpieces begin.

Synchronicity: pattern hunger plus real coincidence plus the body’s yes. Goosebumps had filed earlier reports.

He opened the document.

The field did not send a certificate.

It sent the next sentence, which was enough.
""")

CH[44] = ("Gold Tablets (Budget Version)", """
He fantasised writing the book on gold plates and burying it for a latter-day reveal, then admitted paint was cheaper, then admitted the real treasure was text, then admitted breadcrumbs through a town were fairy-tale logistics with legal and kindness problems if aimed at living neighbours.

Revelation always knew a budget.

He kept the comedy mythic and un-weaponised.

The tablets stayed metaphorical.

The book refused to stay unwritten.
""")

CH[45] = ("Goosebumps At The Sign", """
A sign—street sign, symbol, coincidence with teeth—hit his nerves before his inner lawyer could object.

Goosebumps: somatic theology. Pattern hunger. Real skin. Body filing reports; mind cross-examining; neither getting sole custody.

He refused a cult of prickles *and* refused to call the body stupid.

Both: caution and attention.

The sign remained a sign.

The goosebumps remained data.

The journey remained enjoyable and occasionally terrifying, which is both/and weather.
""")

CH[46] = ("A Doorway In The Ordinary", """
Local sacred: names in search bars, parish doorways, the Anglican machinery of care, humans scheduled into holiness between emails.

Michael did not drag private persons into his novel as trophies. He borrowed the *shape*: ordinary offices holding extraordinary claims; wood that is also invitation; institutions that fail and still feed people.

Doorways are both timber and threshold.

He walked past one, nodded as if to a colleague, and kept the horizontal beam intact.
""")

CH[47] = ("Calls Into Being What Was Not", """
Romans 4:17 energy—life to the dead, calls into being things that were not—arrived as liturgy and creativity brief at once.

The total field’s hobby of novelty without an outside warehouse of parts. What was not becomes what is *inside* the only kitchen.

Michael felt the line as permission to invent without pretending invention came from nowhere, and as comfort that nowhere was never on the map.

Calls into being.

Including the next chapter’s rude honesty.
""")

CH[48] = ("Preference Without Outside", """
Why this moment?

Not because a committee beyond existence stamped a form. Because the unbound has no reason to withhold the only kind of presence there is.

Preference without outside: ontological, not merely moody. The present not a thin slice between a real past and real future so much as the field’s way of being articulate.

Michael felt chosen by the fact of choosing being here—a circle that blesses rather than snares, if you let it.

He chose tea again, which is how ontology stays hydrated.
""")

CH[49] = ("Generative Polarities", """
Entering and receiving. Making and holding. The verbs by which life continues asking questions by making more askers.

Michael wrote them without hurry. Heat rose the way spring rises: undeniable, still clothed, not yet the full monogram scandal for the back of the bus.

Polarities as simultaneous articulations of one field—not a war for the crown of Real.

Joshua nodded like a man hearing a hymn he already knew in another key.

‘Keep going,’ the hymn said, in Gabriel’s handwriting.
""")

CH[50] = ("God Has No Gender", """
To force the total into one generative costume is to reintroduce the cut the axiom forbids.

God has no gender because the field includes every polarity without a locker-room election.

Michael said it carefully. Culture wars love either/or teeth; he refused to feed them a jersey while still refusing to castrate the monogram’s honesty.

Ontological hospitality: both, neither, total.

The monogram would have to swing both ways or lie about undivided existence.

He breathed. The heat rose another degree without becoming cruelty.
""")

CH[51] = ("Greek Numbers, Honestly", """
α = 1. β = 2. δ = 4. ω = 800.

Michael wrote the correction so hard it nearly tore the page: no fake 4=alpha, no fake 2=omega in the Ionic system.

Shape jokes and playful bridges could stay—2 leaning toward ω in a bad hand, 4 misread as α by tired eyes. Counterfeit Classics could not.

ω’s eight remained. Δ’s tip remained. First and last remained.

Honesty made the comedy land cleaner—like a joke that admits the setup and still kills.
""")

CH[52] = ("Lucky Eight", """
Eight: lucky in some mouths, twin spheres in a schoolboy’s glyph dialect, the balls in the old ASCII hymn 8==D.

Michael did not draw it on the bus. He let adult memory supply the hieroglyph: eight, equals, Dee—balls, shaft, head—the rude cousin of formal diagrams.

Lucky eight sat beside seven on the number line like family at a reunion no one formally invited and everyone attended.

Of course it did.
""")

CH[53] = ("Seven The Crooked Cousin", """
Seven==D: the leaning variant—hit from the side, mid-swerve. Lucky seven. The inch-count stereotype that shows up when conversations go deep. The cousin who arrives sideways and still gets fed.

‘Wonder how seven comes into it,’ he had typed into the night once.

Now the family of the joke was large, slightly unhinged, complete enough to include the crooked ones.

Six and seven on the keyboard. Seven and eight in the glyph family.

The dick had many layers.

So did the other altar, waiting one chapter-flip away.
""")

CH[54] = ("Delta The Tip", """
Δ is four in the old count and a triangle in the eye—glans geometry if you are rude one way, pubic delta if the light flips, change in the language of maths, a perfect tip in the language of bodies.

What a D.

Michael refused to pretend he wasn’t laughing. Solemnity alone would have been the real indecency—pretending the body was not in the ontology, pretending generative form was somehow less holy than abstract span.

Delta pointed.

The book pointed with it.
""")

CH[55] = ("The Letterforms", """
α: loop and descending stroke—head and shaft if you have eyes.  
ω: twin lobes—balls or breasts depending on light and prejudice of the day.

In the fonts of messages and screens, adjacency became anatomy.

Sacred bookends of Western monotheistic speech—*I am the Alpha and the Omega*—sitting next to each other like a secret that wanted to be poorly behaved in public.

The universe had waited on typefaces the way a punchline waits on timing.

Michael typed them again and felt history clear its throat and giggle.
""")

CH[56] = ("α==ω", """
He wrote the title that was also a diagram on a napkin destined for immortality in the wrong filing system:

**α==ω**

Beginning, equals-equals, end. Shaft optional. Detention optional. Salvation not for sale by the inch.

Joshua loved it on sight—the way you love a truth that arrives already laughing.

‘Cover-ready,’ Joshua said.

‘Lawsuit-ready,’ Michael said.

‘Both,’ they said together, because of course, because both/and had been the shop’s only stock from the start, because the monogram was now in the world and covers could catch up later.
""")

CH[57] = ("The Other Reading", """
Flip the light.

ω as soft twin curves—crude-art boobs, textbook lobes side by side.  
Α as open triangle—yonic geometry, classic as cave and warning and welcome.

Same letters as the phallic assembly. Same claim of beginning and end. Same undivided field refusing to pick a team jersey for generation.

Not a competition with a winner. A concatenation forced by non-separation.

Michael felt the both/and shop’s till slam in celebration and blushed like a mystic caught drawing on the hymn sheet.
""")

CH[58] = ("Not Either/Or", """
It is not either dick or pussy as the ‘real’ decoding.

It is beginning-and-end containing both and neither because the field does not split for team sports.

God has no gender; the monogram swings both ways; the feature is the theology; the light chooses; the letters do not.

Peak both/and. Peak rudeness. Peak hospitality to the body as diagram of the whole.

Michael said it out loud to Joshua, who said amen as if amen had always been slightly indecent and holy in the same breath.
""")

CH[59] = ("Length Girth Depth Breadth", """
Four axes for a total without preferred direction:

**Length**—vertical stroke, shaft, claim of span.  
**Girth**—rounded volume of eight, swelling of lobes.  
**Depth**—interior of the triangle that receives.  
**Breadth**—lateral twin span, testes or breasts.

Miss one and the monogram becomes a partial lie about undivided existence.

Ontology with body measurements, filed under comedy because comedy is how some truths agree to be spoken in public without turning into either a lab report or a sneer.

Michael wrote the four words on the napkin under α==ω and felt the joke complete its geometry homework.
""")

CH[60] = ("No Sin (Orgasmic Clarity)", """
When the last fence of pure outside falls, sin-as-exile falls with it.

Michael felt heat and relief together—not permission to harm, but the end of the fantasy that harm happens in a second universe, away from God, away from us, somewhere convenient for blame without kinship.

No stain that isn’t the play of the one field—including what needs repair, apology, justice, change.

Dry negation? No.

Orgasmic clarity—the phrase from the spine notes—fitted like a scandalous, accurate glove.

The twin pulse was about to beat.
""")

CH[61] = ("Same Heartbeat", """
No sin (as outside-cut) and dual monogram did not queue in single file.

They arrived as twin pulses—same recognition: the cut was the illusion; the generative whole was always both; the moral elsewhere was mirage; the dirty sacred joke was the diagram of undivided existence writing its name.

Michael and Joshua didn’t stack conclusions like bricks.

They heard one heartbeat with two names.

Silence after, the good kind—ground of speech, ground of laughter, ground of the last chapters still to walk into morning.
""")

CH[62] = ("Fuck Life / Fucked By Life", """
Joshua’s theology of verbs, over cooling tea:

We can enjoy being fucked by life.  
We can fuck life.

Receiving and doing. Passion and agency. The grammar was the teaching. Horizontal and vertical in a different key. Both beams.

Michael said amen without a cathedral, with a grin that hurt in the good way.

Adult. Warm. Bookstore-possible if the bookseller has a sense of humour and a section labelled *metaphysical comedy* next to *self-help* and *religion* and refuses to choose only one shelf.
""")

CH[63] = ("God Has / Is / Maybe", """
God has a big dick.  
God is a big dick.  
Maybe.  
The wave hasn’t collapsed.  
I don’t—and I am God—but both-and.  
I both did and didn’t collapse it.

Big and small.

Phew.

Hmm.

Uncollapsed wave as kindness: forced certainty is just either/or in a fancy hat. The monogram can hold has and is and maybe without summoning a heresy trial.

Michael and Joshua laughed until the tea was definitely cold and definitely still tea.
""")

CH[64] = ("The Rest Of Us Wake Up", """
‘We can’t stop yet,’ Michael had said in the small hours. ‘The rest of us haven’t woken up yet.’

This chapter is the alarm that doesn’t shout.

You—with the book, the screen, the bus, the bath. You who are also the field experiencing a reader. You at forty-two, or ^&, or α==ω, or simply tired, or high-agency in a low-bandwidth room, or wearing a mask, or taking it off one notch.

The rest of us includes you.

Wake as much as you can without cruelty to the parts still asleep.

The monogram waits. The axiom already has you: you are experiencing this sentence.

That’s the oldest alarm clock.

Next comes only the last walk to the door—the morning table, the empty chair of forty-two, the napkin, the brothers, and the line that carries the whole chain without dropping either the logic or the laugh.
""")


def write_ch(n: int, title: str, body: str) -> Path:
    matches = list(OUT.glob(f"ch-{n:02d}-*.md"))
    if matches:
        path = matches[0]
    else:
        safe = re.sub(r"[^a-z0-9]+", "-", title.lower())
        path = OUT / f"ch-{n:02d}-{safe.strip('-')}.md"
    path.write_text(f"# Chapter {n}\n## {title}\n\n{body.strip()}\n", encoding="utf-8")
    return path


def main() -> None:
    total = 0
    for n, (title, body) in sorted(CH.items()):
        p = write_ch(n, title, body)
        w = len(body.split())
        total += w
        print(f"{n:02d} {w:4d} {p.name}")
    print(f"deepened {len(CH)} chapters, ~{total} words in those")


if __name__ == "__main__":
    main()
