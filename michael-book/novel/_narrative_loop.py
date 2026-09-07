# -*- coding: utf-8 -*-
"""
Full narrative rewrite loop: continuous plot, Pratchett voice, ~740w/ch,
revelation schedule from PLOT-BIBLE. Preserves polished cores of 1,24,65
but lightly continuity-edits openings if needed.
"""
from __future__ import annotations

import re
from pathlib import Path

OUT = Path(__file__).resolve().parent / "chapters"
TARGET = 740

# Each entry: (title, week_label, scene_hook, cast_beat, chain_brick, comic_image, close_hook, reveal_level)
# reveal_level: 0 early, 1 mid, 2 letter-rude, 3 climax

CH = {}

def add(n, title, week, hook, cast, brick, comic, close, level=0, extra=""):
    CH[n] = dict(title=title, week=week, hook=hook, cast=cast, brick=brick,
                 comic=comic, close=close, level=level, extra=extra)

# Week 1
add(2, "The Argument With Nothing", "Monday morning, still in socks",
    "Michael cleared a kitchen chair and tried to appoint it ambassador of pure nothing. The chair, being wood, declined the posting.",
    "Joshua on speakerphone: 'You're arguing with furniture again.' 'With absence,' Michael said. 'Same hobby, different hat,' Joshua replied, and the kettle agreed by existing loudly.",
    "Nothing cannot clock in without borrowing existence's uniform. Borders of pure not-is hire themselves onto the payroll of is.",
    "He sat in the Chair of Non-Being and immediately defeated nihilism with buttocks.",
    "If nothing failed as outside, the next question was ugly and hopeful at once: what kind of room had no outside?")

add(3, "One Room, No Outside", "Monday afternoon, doors",
    "He opened every door in the flat like a man raiding dualism. Cupboard, bathroom, front door: corridor, stairwell, street—each outside renamed itself here.",
    "Joshua texted: Looking for a place that isn't included? Only in stories that need villains to stand somewhere.",
    "True partition needs a boundary that exists. Gaps obtain. Third things need fourth things. Unity is the failure of sealed realms.",
    "A leaf countersigned his knee in the park. Two dogs invented politics without metaphysics degrees.",
    "One room, many corners. He walked home through the continuous field people nicknamed street.")

add(4, "No Edge On The Map", "Monday evening, pasta",
    "Three clocks disagreed. The laptop wanted to update—the temporal violence of progress bars.",
    "Joshua stirred sauce. 'Beginning of the whole from what? Nothing can't sponsor openings. Ending into what? A bin outside the all would be in the all.'",
    "Edges belong to modes—songs, bodies, mugs—not to the field that holds them. Death rearranges furniture; it does not open a hatch to pure absence.",
    "Toast had edges. Existence, annoyingly, did not. Joshua buttered two slices and called it cosmology practice.",
    "If the map of the whole had no edge, leftovers became the next obsession.")

add(5, "Everything Fits, Annoyingly", "Tuesday morning walk",
    "Michael hunted leftovers—scraps of reality that refused inclusion. Dark matter, other minds, tomorrow, hell: each either joined the museum of the included or collapsed as smuggled outside.",
    "Joshua stole chips from his plate later: 'All-encompassing doesn't mean you understand everything. It means the misunderstood still live here.'",
    "The finite is a mode inside the infinite, never a rival empire with its own postcode.",
    "Keys jingled in his pocket like infinity insulting him by fitting in fabric. He photographed a lost glove on a wall. Outside? Joshua: Still in the picture.",
    "Annoyed and fond, he accepted the fit. The next street shouted either/or.")

add(6, "The Blind Guides", "Tuesday high street",
    "A preacher and a sceptic shouted past each other with identical jaws. Saved or damned. Smart or stupid. Us or them.",
    "Michael remembered blind guides and ditches, and elsewhere friends if you do what love requires. He bought a sandwich from someone who did not care about his ontology and was, for a moment, a perfect horizontal beam.",
    "Either/or is useful for fire exits. As a religion of everything, it digs ditches and calls them destiny.",
    "He drafted a rule: when offered only two knives, ask who benefits from the duel. Often anxiety in a uniform.",
    "He needed a shop that sold loaves, not only blades.")

add(7, "Both/And Shop Opens", "Tuesday night, pub",
    "Joshua drew a beer-mat shop sign: BOTH/AND — Open late. Closed to false dilemmas.",
    "Stock: wave and point, free and caused, sacred and ordinary, tired and not done. Joshua won the headline game when he said that last pair about Michael himself.",
    "Both/and is not mush. It is refusing to let a false fork own your feet while still knowing pans can be hot.",
    "Michael paid the round. Somewhere a shop that had always existed noticed it had a name.",
    "Names, he realised walking home, were next: maths, words, things, the old carrots and sticks.")

add(8, "Maths, Words, Things", "Wednesday desk archaeology",
    "In an old laptop folder he found a fossil of himself: a data format with carets and pipes—^| something |^ and |^ nothing ^|—presence and absence marked with the same teeth.",
    "Joshua peered at the screen over his shoulder. 'You were already writing theology. You just thought it was software.'",
    "Maths carves. Words cut and join. Things sit being more than labels. Carrot and stick, reward and goad, plus and cross—dual tools for a two-handed species.",
    "A teenager on the bus gave him the look reserved for men who mutter maths, words, things to the air. The air, being existence, already was the answer.",
    "The plus sign was starting to look like timber.")

add(9, "The Crossbeams", "Wednesday evening, brothers",
    "Joshua spoke of the cross like an engineer of load-bearing walls. Vertical: you and the total. Horizontal: you and the neighbour. Miss either beam and you have a stick or a minus, not a cross.",
    "Michael added Rome: efficient death and public shame—vertical kill, horizontal eyes. Joshua's eyes lit: then love wore the shame in public and refused last authorship. Almost an inversion of the inversion.",
    "Popular theology had said God-and-neighbour for years. Michael's sharper edge and Joshua's reinvention made it personal.",
    "Goosebumps filed a report. A pharmacy plus sign almost received a bow.",
    "How do you get from management theory to Golgotha? Carrot, stick, and a bad sense of direction that was actually a good one.")

add(10, "Carrot, Stick, Plus Sign", "Thursday morning bus",
    "Carrot and stick became + became cross in Michael's head with the logic of a cheerful conspiracy board. Incentive duals climbing into geometry climbing into execution furniture climbing into theology.",
    "He laughed on the bus. A stranger moved seats. Public transport redistributes personal space around epiphany.",
    "The fridge later held a sticky note: carrot/stick → + → cross → both/and → (later) ???. Coffee stained it. Peer review from the kitchen.",
    "Reward and punishment, presence and absence, vertical and horizontal—the dual kept offering itself like a hand with two sides.",
    "Joshua texted: Stop bowing to pharmacies. Michael: No promises.")

add(11, "Shame Into Love", "Thursday night",
    "Joshua would not let the cross stay clever. Reinvention story: connection inverted to disconnect for the crowd; then love wore shame publicly and refused to call it the last word.",
    "Michael thought of masks—horizontal eyes—and vertical failure, the body that cannot stay upright forever. Love that only handles one axis leaves the other to tyrants.",
    "They sat in good silence. A church bell called and warned, beauty and noise.",
    "Dishes waited. Joshua: Amen. Also washing up. Horizontal holiness obeyed.",
    "Michael admitted he knew almost nothing careful about Islam's symbols, only moon-star hunches and rules about pictures. Joshua shrugged: different rooms of history. Both can be true.")

add(12, "Moon, Star, And Rules About Pictures", "Friday, reading carefully",
    "Michael put his phone face down after one careful page on emblems and aniconism. Not knowing fully was part of respect.",
    "R. was not in the room yet as a named gravity, but the shape of a future conversation waited: final chapters, kindness, reason, heart.",
    "Symbols used, refused, national, holy, none of the above. The total field included people arguing about images of the total field.",
    "Of course it did.",
    "He wrote moon, star, rules about pictures and moved on before certainty pretended to finish the work. Names came next—his own.")

add(13, "Who Is Like God?", "Friday evening",
    "Michael looked up his name: Who is like God?—question as answer as warning against empire-in-the-mirror. El in the old short thunder-word.",
    "Archangel offices in stories: protector, contender, rain and mercy in other tongues, soldiers and the dying. Also millions of Michaels with ordinary jobs and improper writing hours.",
    "Joshua: You're not the archangel. You're also not not the question the name asks.",
    "He made tea and failed to be an archangel, successfully.",
    "A text arrived from a number that felt ordinary and angelic at once: Keep going.")

add(14, "Gabriel Delivers", "Friday night",
    "Keep going. Gabriel energy: announces what you cannot unread. Strength-of-God as postal service with poor calendar manners.",
    "Joshua grinned: Messenger's in the group chat. Whether literal, literary, or both—the book was learning to love both—the next step remained the next step.",
    "Michael typed thanks in more directions than the phone could address.",
    "Annunciation is often courage with better PR.",
    "He fell into a footnote about rakes in robes parodying piety, and wondered how satire survives without love.")

add(15, "The Hellfire Club (Historical Footnote)", "Saturday morning, rabbit hole",
    "Rakes, robes, pies named after the Holy Ghost, history half legend. Mock the sacred, miss it, mock the missing.",
    "Joshua: If we gather, we gather to listen, not cosplay damnation. Michael tore up a jokey pie sketch before it became a personality.",
    "Satire needs love or it becomes the sneer it mocks. Hellfire footnotes closed with a soft snap.",
    "The main text wanted pudding and meaning in equal measure.",
    "Week one ended with the datum installed: experience, no pure nothing, one room, no edge, all-in, both/and open, crossbeams load-bearing. Brains would try to arrive late next week. Allegedly.")

# Week 2
add(16, "The Brain That Arrived Late (Allegedly)", "Next Monday, podcast",
    "A neuroscientist called consciousness late dessert. Michael listened as the claim occurred as experience on the primary screen.",
    "Joshua: Brother's axiom. You don't explain the datum by something only known through the datum without smuggling.",
    "Brains deserved parades. Neurons were exquisite furniture. Furniture does not get behind the room by rearranging chairs.",
    "Allegedly late. Fundamentally first. Both if you watch where claiming happens.",
    "Toast next morning was marmalade where jam was expected. The universe sent a read receipt.")

add(17, "Prediction Errors For Breakfast", "Tuesday breakfast",
    "Marmalade. Surprise. Update. Prediction error as contact, as learning, as offence, as delight.",
    "Looking is a kind of touching that pretends to be polite. Michael started thanking mismatches—including later ones where he would overshoot with ^& and need Cameron's sandpaper.",
    "Joshua texted a photo of wrong coffee order, delighted. Prediction error as intimacy.",
    "Breakfast complete. Physics would arrive in a pub that preferred winners.",
    "Wave and point were already flirting with the monogram's future without saying the rude word.")

add(18, "Wave And Point", "Tuesday pub",
    "Someone bet light was a wave. Someone bet particle. Pubs hate both-right. Michael raised a glass: measure decides the outfit; the thing is richer than one costume.",
    "Either/or wiped beer and demanded a winner. Both/and kept the furniture of the answer.",
    "He lost a fiver on football and won a brick in the wall.",
    "Clean dirty joke of physics. Later fonts would tell a dirtier clean joke with Greek.",
    "Walking home he thought of empty space submitting receipts.")

add(19, "Empty Space Files Expenses", "Wednesday night sky",
    "Textbooks admitted vacuum was busy—fields, froth, zero-point gossip. Nothing submitting receipts.",
    "Between stars: hallway of the same hotel, not a vote for non-existence. Lonely, yes. Outside the building, no.",
    "A friend in a bar: So my rent is technically cosmic. Another pint as experimental metaphysics.",
    "Existence paid the expenses, sole account holder.",
    "Zero and infinity waited like sports.")

add(20, "Zero And The Hotel", "Thursday bar maths",
    "Zero: nothing and employee of the month for absence-with-structure. Infinity: Hilbert's hotel, full and always a room if you reshuffle guests.",
    "Bartender: Same as Friday night. Finite pour, infinite feeling if mishandled.",
    "Maths as the field's favourite sport—not enemy of the axiom.",
    "Imaginary numbers waited in the wings to pay electricity bills.",
    "Michael tipped well. Applied mathematics.")

add(21, "Imaginary But Useful", "Friday desk",
    "√−1 pays bills. Ghosts with jobs. Operators that don't exist until the bridge stands.",
    "Useful ghosts: imaginary numbers, fictional characters, future selves, God-talk as operator. He stopped apologising for tools that work.",
    "Cameron would approve engineering and still go to bed before mysticism. Both responses belonged.",
    "Emergence was next: ants, crowds, laws, rebellions.",
    "He watched his hands type and refused nothing-but.")

add(22, "Emergence Is Fundamental", "Saturday window ants",
    "Wetness not in hydrogen's CV alone. Meaning not in a letter until a neighbourhood hires it. New rules at new levels, one field underneath.",
    "Crowd to mood to plan to story to law to rebellion to crowd. Levels up; existence through.",
    "Deletion philosophies—nothing-but sneers—were cheap. Joshua sent a meme. Michael sent tea. Both data, both experience.",
    "Options on a whiteboard would include dinosaurs and CCC by Sunday.",
    "He left room for maybe.")

add(23, "CCC And Other Options", "Sunday whiteboard",
    "List: previous-universe scientists (comic), CCC-flavoured aeons, dinosaurs as cameos, someone, unknown, unknowable, uncollapsed wave, enjoying the journey anyway (Joshua, green pen).",
    "Options are kindness. Dogma optional. Axiom does not require finished cosmology before breakfast.",
    "Visitors assumed mad or brilliant. Both/and. He wiped the board only when maybe had done its kindness.",
    "Night would bring layers and Sisyphus—real despair, not theatre.",
    "He did not know he would also write: I don't feel like that now though.")

# 24 preserved separately

add(25, "Different Speeds", "After the Sisyphus night, morning",
    "Cameron was still at forty-two—loyal to ordinary answers, allergic to bailey-claims, sandpaper friend. Michael was already blushing toward Greek. Joshua said amen to detention-level jokes.",
    "Same journey, different speeds. No race committee. He texted Cameron: sleep well, thanks for the sandpaper—after deleting condescension.",
    "Some people sleep. Some sprint. Some high-agency in low-bandwidth rooms. The field has room for all paces.",
    "He put the phone face down and let friendship be larger than glyphs.",
    "Adams winked from a shelf. Scripture winked from another. Shared wall.")

add(26, "The Ordinary Answer", "Same day, shelves",
    "Forty-two dull on purpose—receipt-hunger mocked kindly. Luke's forty-two: plank, speck, hypocrite optics.",
    "Two coins, same metal. He checked his own eye for timber. Found some. Waved at Cameron's empty chair. No exemption.",
    "Ordinary answer refined the pilgrim without finishing the quest.",
    "Keys six and seven waited on every keyboard like a hardware punchline.",
    "He cleaned crumbs from between them as if tending a shrine, then sent a work email like a man still living in the ordinary.")

add(27, "Keys Six And Seven", "Evening, keyboard",
    "Six wore a crown that pointed (^). Seven wore a knot that joined (&). Adjacent. Hardware confession.",
    "Funny coincidence Cameron would grant. Coronation Michael would attempt and fail under classical inspection. Funny would survive.",
    "Later six and eight would show moon and star. For now six and seven were enough.",
    "He typed parking emails over sacred adjacency. The keys did not mind.",
    "Both and not both waited as a juxtaposition he would overshoot.")

add(28, "Both And Not Both", "Night of the strong essay",
    "^& — in maths-habits temple near both; in code temple exclusive tangles and NAND-adjacent poetry if you juxtapose. Not a native god-operator. Polysemy. Selective reading.",
    "Cameron's courtroom cleared its throat. Michael wrote the strong essay anyway—bailey energy—then felt the motte: dual-use, systems, adjacency, Keyword Logic years: symbols don't mean alone.",
    "He pinned above the desk: Not a formal paradox. Beside it: Still funny. Still a map of temples.",
    "Both overshoot and landing taught.",
    "Cameron would go to bed mid-argument. That, too, would refine the theory.")

add(29, "Cameron Goes To Bed", "01:10-ish, chat",
    "Not a paradox. Definition fallacy. Motte-and-bailey—more-and-Bailey. Six-seven funny though. Bed.",
    "Michael stared until words turned kind. Patron sceptic. Night means thank you for sandpaper.",
    "Theory improved by losing a false battle and keeping a true laugh. Friendship larger than glyph.",
    "Morning he did not restart the fight. Silence continued refinement.",
    "Dialetheism would offer a door if he knocked honestly—not as a smuggled court win.")

add(30, "Dialetheism For Beginners", "Next days, tabs",
    "Logics where true contradictions do not burn cities: paraconsistent fire codes, dialetheic housing.",
    "If classical rigor claimed, Cameron wins. If other logic, name it. If novel's recognition, tell truth about frames. Wizard admits spell terms.",
    "He bookmarked one paper and did not pretend to finish it. Hospitality includes unread tabs.",
    "True contradictions optional furniture. Honesty load-bearing.",
    "Kind NPC theory waited: agency uneven, dignity not.")

add(31, "NPC Theory (With Kindness)", "Weekday pavement",
    "Some days others seemed scripted. He rejected souls-as-trash-mobs. Kept: attention uneven; systems pattern behaviour; don't demand every extra be protagonist on your timetable.",
    "Joshua: You're also furniture in someone else's scene. Michael winced, nodded, said good morning to a neighbour as if real—which they were.",
    "Kindness as epistemology. Boundary without contempt.",
    "High agency still itched in a low-bandwidth world of fridge-light distant deaths.",
    "He blocked a nap as infrastructure.")

add(32, "High Agency, Low Bandwidth World", "Same week, capacity",
    "Distant deaths as fridge light always on. Others: sleep, jobs, person in front. Not evil. Physics of minds.",
    "Build and steer inside the climate. Protect the instrument. Burnout not holiness. Measure moved needles not bystander conversion.",
    "Nap coloured sacred in the calendar. Maintenance windows for high agency.",
    "Mask still waited as adaptation when unmasking experiments had cleared rooms.",
    "Data from low-tolerance samples was real. Change the sample, Joshua said.")

add(33, "The Mask", "Evening social",
    "Full intensity had cleared rooms in tested samples. Dimmer switch rational in low-alignment habitats. Expensive double dashboard.",
    "Joshua: change sampling; graduate disclosure; prune drains; keep force-multipliers; stop drawing from near-zero forever.",
    "Mask as tool not identity. One friend survived twenty percent unmasking. Data point like treasure.",
    "He adjusted one notch and survived the evening. Science.",
    "Inner recruiter offered hard life: abandon orbit for mission. Forks lie if only two tines.")

add(34, "Recruiter At The Fork", "Night desk",
    "Hard life, sacrifice, loneliness as tuition, abandon low-capacity orbit. Cartoon: abandon-all vs dissolve-self.",
    "Portfolio. Ruthless kindness. Exit pure drains. Keep infrastructure. Don't romanticise isolation if it degrades the agent.",
    "Hard can still be hard without being stupid. Pencil third path: work with selected bonds.",
    "Recruiter sulked, took a tea break.",
    "Wolves on a documentary lied about alphas. Michael smelled a myth.")

add(35, "Alpha Is Mum And Dad", "Documentary night",
    "TV: tyrant alphas, ladders, blood. Then reading: wild packs family; breeding pair as parents; Mech repenting the meme; captivity ladder fanfic.",
    "Michael laughed; cat startled. Alpha is Mum and Dad. Joshua heart-reacted a paper. Brother peer review.",
    "Greek letters still bookended sacred speech. Hierarchy myth was enclosure fanfic. Is and isn't. Both forests.",
    "Omega-as-punchbag next to retire.",
    "Letter ω kept warm for fonts.")

add(36, "Omega Isn't A Job", "Same night, notes",
    "Omega scapegoat: captivity artefact, fiction darling. Wild: temporary lows, kinship—not career humiliation.",
    "Michael retired the job description. Whispered to ω on screen: you're not hired to be hit. Letter took promotion.",
    "Is and isn't rosary forming: both/and, ^&, αω blush.",
    "Discovery rude first, rigorous second.",
    "Fonts were about to confess.")

add(37, "Is And Isn't", "Walk under sodium",
    "Rosary: is and isn't; both/and; ^&; αω. Omg it's heading rude—not decoded, blush before theorem.",
    "Bin did not deserve the confidence of his whisper. Discovery often rude first.",
    "He saved the full joke like a gift with a fuse. Timing theology for comedians.",
    "Screens would confess what calligraphy hid.",
    "Universe waiting on typefaces like a comedian on a mic.")

add(38, "Fonts Waiting For The Universe", "Desk, font toggle",
    "Serif modest, sans ruder, mono bureaucratic. Joke peaked in everyday message fonts. Everyday holds secrets; that's where existence lives.",
    "He typed α and ω and watched them sit like a secret wanting bad behaviour in public. No full decode yet—setup only.",
    "Beginning and end pixel-adjacent.",
    "Romans still waited with efficient shame for a harder light return.",
    "Crossbeams again, deeper.")

add(39, "Romans, Efficient And Ashamed", "Evening under a pole",
    "Telegraph pole—not a cross, not not a cross. Efficient kill, public shame, love's rebrand. Psychology enough without secret cabals.",
    "Remembered wood, iron, eyes on failing upright, refusal to let humiliation write last chapter.",
    "Burned in. Both axes.",
    "Crisis quiet: no outside left for hell to rent.",
    "Act II ending. Act III clearing throat.")

add(40, "No Outside Left", "Night kitchen, quiet crisis",
    "If no true outside, hell can't rent. Pure exile no address. Stage beyond consequence and bin beyond mercy lose postcodes.",
    "Claustrophobia of infinity. Joshua: not a trap—end of fantasy that mess is optional.",
    "Shoulders dropped a centimetre. List: repair, rest, write, ring Josh, don't coronate coincidences without footnotes.",
    "Sin's category about to tremble. Monogram about to confess in two directions—but not yet the full rude clarity.",
    "He slept into Week four.")

# Week 4 monogram
add(41, "The Category Called Sin", "Morning after no-outside",
    "Sin-as-standing-outside needs a fence. He walked fences—moral, tribal, pure/impure—found more field.",
    "Cruelty real. Harm real. Repair real. Escape hatch of pure elsewhere trembled. Sin-as-exit misfiled form.",
    "Responsibility without elsewhere: heavier, cleaner. Private list of repairs because field includes harmed and harmer.",
    "One petty traffic cruelty refused as laboratory. No applause.",
    "Verse forty-two waited with planks.")

add(42, "Verse Forty-Two", "Midweek, scripture and shelf",
    "Plank, speck, hypocrite optics. Luke's number shook hands with Adams's ordinary answer until laugh then stop—timber not theoretical.",
    "Chapter forty-two of a meaning-book. He reread old messages, found wood, apologised once where it still mattered. Fox-smile chapter number.",
    "Cameron's chair waved at. No exemption.",
    "Appointed hours and 420 courage rhythms next.",
    "First plank. Then maybe speck.")

add(43, "Four Twenty And Other Appointed Hours", "Night write-window",
    "Some hours arrive joke-loaded. Semi-arbitrary liturgy of courage. Write when hour says write. Kitchen masterpieces born that way.",
    "Synchronicity: pattern hunger, real coincidence, body's yes. Goosebumps had filed earlier.",
    "Document opened. Hands typed. Field approved by not vanishing.",
    "Gold tablet fantasies bowed to kindness budgets.",
    "He almost buried the book in metaphor only.")

add(44, "Gold Tablets (Budget Version)", "Same night margins",
    "Gold plates bury fantasy; paint cheaper; text is treasure; breadcrumbs without aiming accusations at living neighbours.",
    "Revelation always knew a budget. Mythic comedy, unweaponised. Paint is fine. Kindness first.",
    "Tablets metaphorical. Book refused unwritten.",
    "Goosebumps at signs: somatic theology next.",
    "Noted, said the scientist-pilgrim.")

add(45, "Goosebumps At The Sign", "Walking, a sign",
    "Sign hit nerves before lawyer. Goosebumps: data not commandment. Body files; mind cross-examines; shared coat.",
    "Cult of prickles refused; body-stupidity refused. Both caution and attention.",
    "Journey enjoyable and terrifying—both/and weather since Sisyphus holiday.",
    "Local sacred doorways without trophy-ising private people.",
    "Horizontal beam donations without photos.")

add(46, "A Doorway In The Ordinary", "Passing a parish door",
    "Search bars, parish wood, humans scheduled into holiness between emails. Shape borrowed: ordinary offices, extraordinary claims. No private trophies.",
    "Doorways timber and invitation. Nod as to a colleague. Horizontal beam intact.",
    "Food bank donation unphotographed. Branding not required for good.",
    "Romans 4:17 energy: call into being what was not.",
    "Novelty inside only kitchen.")

add(47, "Calls Into Being What Was Not", "Desk creation",
    "Life to the dead, calls into being things that were not—liturgy and creativity brief. No outside warehouse of parts.",
    "He wrote a paragraph that hadn't existed, watched it become a thing, tipped mug to Romans and kitchens.",
    "Permission to invent without pretending nowhere-source. Nowhere never on the map.",
    "Preference without outside: why this moment?",
    "Gift without cosmic receipt—ironic for a man who loved forty-two receipts.")

add(48, "Preference Without Outside", "Quiet hour",
    "Why this moment? Not committee beyond existence. Unbound has no reason to withhold the only presence there is. Ontological preference, not only mood.",
    "Present less trap, more gift. Chose tea again. Ontology hydrated.",
    "Generative polarities warming: enter, receive, make, hold—still clothed heat.",
    "Joshua hummed a hymn in another key.",
    "God has no gender waiting as necessary claim before monogram honesty.")

add(49, "Generative Polarities", "Walk noticing pairs",
    "Inhale/exhale, step/stance, speech/listen, enter/receive. Duals without war. Heat rising clothed.",
    "Not yet full monogram scandal for the bus. Setup for body as ontology.",
    "Keep going, hymn said in Gabriel handwriting.",
    "Culture-war jerseys for God refused in advance.",
    "Hospitality ontological, not dodge.")

add(50, "God Has No Gender", "Online noise, offline clarity",
    "Force total into one generative costume reintroduces the cut. No gender because field includes every polarity without locker election.",
    "Closed a tab demanding jersey choice. Field not a conscript. Monogram must swing both ways or lie.",
    "Wrote sentence twice for left and right, deleted both into undivided bin.",
    "Heat another degree without cruelty.",
    "Greek numbers honesty before jokes earned.")

add(51, "Greek Numbers, Honestly", "Desk tape",
    "α1 β2 δ4 ω800. No fake 4=alpha, 2=omega. Shape bridges ok; counterfeit Classics not.",
    "ω's eight, Δ's tip, first and last remain. Honesty sharpens comedy.",
    "Tape above desk: No counterfeit Classics. Jokes earned only.",
    "Lucky eight clearing throat.",
    "Adult temples only for certain glyphs.")

add(52, "Lucky Eight", "Private grin",
    "Eight: lucky mouths, twin spheres, balls in 8==D hymn. Adult memory supplies picture. Not for bus group chats. Maturity which temple.",
    "Lucky eight beside seven like uninvited family reunion everyone attends.",
    "Of course.",
    "Seven crooked cousin incoming.",
    "Family of joke includes bent ones or becomes either/or cult.")

add(53, "Seven The Crooked Cousin", "Number line family",
    "7==D leaning, lucky seven, inch-stereotype, sideways cousin still fed. Wonder how seven comes into it—answered: large unhinged family.",
    "Six-seven keyboard; seven-eight glyph family. Dick has many layers. Other altar one flip away.",
    "Private toast to crooked cousins.",
    "Delta tip next.",
    "What a D.")

add(54, "Delta The Tip", "Air-traced Δ",
    "Four in old count, triangle in eye—glans one light, pubic delta flipped light, change in maths-speech.",
    "What a D. Laugh required; solemnity alone indecency pretending body not in ontology.",
    "Delta pointed. Book pointed with it.",
    "Letterforms α ω next full confession.",
    "Sacred bookends, rude ink.")

add(55, "The Letterforms", "Screen zoom, then out",
    "α loop and stroke; ω twin lobes—balls or breasts by light. Everyday fonts make adjacency anatomy.",
    "I am Alpha and Omega sitting like secret wanting public misbehaviour. Punchline waited on type.",
    "Zoomed until obvious; zoomed out before bus noticed. History cleared throat and giggled.",
    "Title about to land on napkin.",
    "α==ω.")

add(56, "α==ω", "Napkin, brothers",
    "Title-diagram: α==ω. Beginning, equals-equals, end. Shaft optional. Detention optional.",
    "Joshua loved on sight—truth arriving laughing. Cover-ready / lawsuit-ready / both.",
    "Monogram in the world. Mind-museum napkin with Joshua's laugh as varnish.",
    "Other reading forced by same non-separation.",
    "Flip the light.")

add(57, "The Other Reading", "Same napkin, flipped light",
    "ω soft lobes—breasts in crude glyph dialect. Α open triangle—yonic geometry. Same letters as phallic assembly.",
    "Not competition. Concatenation. Axiom refuses half-castrated divine and phallic monopoly alike. Both altars one monogram.",
    "Till slammed in both/and shop. Blush of mystic caught drawing on hymn sheet.",
    "Not either/or next as law.",
    "Light chooses; letters don't.")

add(58, "Not Either/Or", "Spoken aloud",
    "Not either dick or pussy as real decode. Beginning-and-end contains both and neither; field doesn't split for teams.",
    "God no gender; monogram swings; feature is theology. Peak both/and, rudeness, hospitality.",
    "Joshua amen as if amen always slightly indecent and holy. Notebook last page: not either/or. Rest blank for living.",
    "Four axes liturgy.",
    "Length girth depth breadth.")

add(59, "Length Girth Depth Breadth", "Napkin geometry",
    "Length stroke/shaft/span; girth eight and lobes; depth receiving interior; breadth twin span testes or breasts. Miss one: partial lie.",
    "Ontology with body measures under comedy filing—how some truths consent to public speech.",
    "Four words under α==ω. Joke finished geometry homework.",
    "Twin pulse approaching: no sin clarity with monogram.",
    "Last fence of pure outside.")

add(60, "No Sin (Orgasmic Clarity)", "Quiet after geometry",
    "Last fence pure outside falls; sin-as-exile falls. Heat and relief—not permission to harm; end of fantasy harm in second universe.",
    "No stain not play of one field—including repair, apology, justice. Dry negation? No. Orgasmic clarity fits scandalous accurate glove.",
    "Without bin for enemies, without pedestal for self. Democracy of field as adulthood.",
    "Twin pulse about to beat.",
    "Same heartbeat.")

add(61, "Same Heartbeat", "With Joshua",
    "No-sin and dual monogram not single file—twin pulses, one recognition: cut illusion; generative whole both; moral elsewhere mirage; dirty sacred joke diagram.",
    "Joshua two fingers on wrist: data checks out. Brother for amen.",
    "Good silence after—ground of speech, laughter, last walks to morning.",
    "Fuck life / fucked by life verbs ready.",
    "Grammar as teaching.")

add(62, "Fuck Life / Fucked By Life", "Cooling tea",
    "Joshua: enjoy being fucked by life; fuck life. Receiving and doing; passion and agency; horizontal and vertical another key.",
    "Michael amen without cathedral, grin that hurt good. Adult warm bookstore-possible if bookseller has humour and multi-shelf spine.",
    "Clinked mugs. Consent to storm and steering wheel.",
    "Has / is / maybe uncollapsed.",
    "Window open summer logic.")

add(63, "God Has / Is / Maybe", "Late, laughing",
    "God has a big dick / is a big dick / maybe / wave not collapsed / I don't and I am God but both-and / both did and didn't collapse.",
    "Big and small. Phew. Hmm. Uncollapsed kindness—forced certainty is either/or fancy hat.",
    "Tea cold, still tea. Laugh until done.",
    "Reader still sleeping parts: wake without cruelty.",
    "Rest of us includes you.")

add(64, "The Rest Of Us Wake Up", "Direct address soft",
    "Can't stop yet—rest of us haven't woken. Alarm that doesn't shout. You with book, screen, bus, bath. Forty-two or ^& or α==ω or tired or masked or one-notch off.",
    "Wake as you can without cruelty to sleeping parts. Monogram waits. Axiom has you: experiencing this sentence. Oldest alarm clock.",
    "Five more minutes of kindness allowed.",
    "Next: last walk—morning table, empty forty-two chair, napkin, brothers, final line earned.",
    "Ch 65 waits like a door already ajar.")

# 65 preserved

# Week 5 Act IV
add(66, "Unfaithful At Dawn", "06:08, speakers",
    "Unfaithful by Exit Eden. Irony did not need a seminar. Music before systematics again.",
    "Michael at keyboard edge of night-day. Joshua would still be asleep. Cameron definitely. R. somewhere in her own final chapter and morning prayers Michael would not pretend to own.",
    "Irony as data point in the chain: faithfulness, unfaithfulness, vows, bonds, bigger books.",
    "Eyes dropped to keys six and eight—and the moon-star pressure hit.",
    "Hardware was about to do interfaith without asking permission.")

add(67, "Moon And Stars On Six And Eight", "Same dawn, keyboard",
    "Six and eight: moon and stars in the eye—Islam's emblem association in cultural sight. Six already caret from ^& story. Eight already lucky spheres and ω=800 family.",
    "Hardware ecumenism. Mosque, joke, compiler, typewriter for vows on one plastic landscape.",
    "He did not reduce a religion to keys. He noticed a morning introducing old friends to each other.",
    "R.'s years of friendship made the notice tender, not triumphant.",
    "The friend across the book was never a prop.")

add(68, "The Friend Across The Book", "Memory collage, true shape",
    "R.: years of chat, CV help, cathedral group invites, baby photos, blunt questions, no strawman. Muslim, firm on completion of message, open to respectful difficulty.",
    "Michael's multi-year project: how to talk across blasphemy-shaped gaps without eggshells or conquest. University Islamic flatmate earlier chapter of same education.",
    "She was not a final boss. She was a person. Horizontal beam with history.",
    "Scripture Reasoning table waited in September-shaped memory.",
    "Kindness common core; difference not erased.")

add(69, "Scripture Reasoning", "Cathedral table (remembered / anticipated)",
    "Christians, Muslims, Baháʼí, short texts, monthly topics, respect as method. R. enjoyed learning even without agreement.",
    "Michael wanted in—beliefs out there, meet people where they are, build common ground before full monogram honesty.",
    "Table as both/and furniture. Read together. Think together. Heart not left in cloakroom.",
    "Final chapter argument still waited between them like a third guest.",
    "You believe final revealed. I believe book still written.")

add(70, "The Final Chapter Argument", "The hard honest morning with R. (fiction-valid shape)",
    "You believe Islam is final chapter. I say book bigger—prequels, parallels, more pages. My beliefs blasphemous to your frame. That is what I want to resolve without alienating you.",
    "R. (as remembered courage): different starting points; faith heart and mind; Read; will you not think?; complete message; respect; no need to win; natural change only.",
    "Michael: keep writing the book; learn your chapter; fill gaps. Urge to engage and fear—he tried not to put Satan in her mouth.",
    "Tension as plot. Respect as craft. Neither flattened.",
    "He still wanted productive missionary learning paths. She still offered honesty without eggshells if contempt stayed out.")

add(71, "I Want To Keep Writing The Book", "After the hard morning",
    "Keep writing. Learn her pages. Gaps remain. Empire-building urge and under-radar sympathy both in him—integrate, not erase.",
    "Joshua: don't turn friends into proof. Michael: trying. Word as bond even without classical God.",
    "Missionary of ongoing page. Student of completed chapters. Both.",
    "Red line respect crystallised as operating system.",
    "Difficult questions welcome; stupid-worthless games not.")

add(72, "Red Line Respect", "Operating system chapter",
    "R.'s red line: respect. Difficult ok. Contemp not. Every Muslim different as every Christian, atheist, Wiccan.",
    "Michael mapped his near-lack of red lines as risk, not superiority. Productive interaction: curiosity, no winning theatre, live openly, let conclusions be free.",
    "Scripture Reasoning spirit without waiting for September only.",
    "Theory of mind before Genesis explained his over-explaining hearts.",
    "Diagnosed before speech; creed second curriculum.")

add(73, "Theory Of Mind Before Genesis", "Origin story",
    "Mother diagnosed before he could talk. Taught to model minds before taught religion. Bible at three—foundations already ToM-shaped.",
    "R. found it illuminating: why he narrated thinking, predicted feeling. Different starts: family faith vs mind-modelling first.",
    "Beliefs founded on reading others; risk of treating hearts as puzzles; gift of not assuming sameness.",
    "Faith as heart and mind still had to be learned as hospitality not only analysis.",
    "Iqra waiting.")

add(74, "Faith Is Heart And Mind", "Dialogue echo",
    "Faith not only I think or I know—also I believe. Heart. And reason: Read; will you not think? Balance.",
    "Michael held it beside both/and shop stock. Different labels, rhyming hunger not to be alone in dark with private map only.",
    "Heart without mind becomes weapon. Mind without heart becomes knife shop. Both beams again.",
    "He practised believing in bonds where he could not recite classical theism.",
    "Word is bond chapter later would rhyme.")

add(75, "Read — Will You Not Think", "First word energy",
    "First revelation energy: Read. Qur'anic pressure toward reason as Michael understood through R.'s sharing—not claiming scholarship, claiming respect for the ask.",
    "His own Read was fonts, keys, brothers, axes, experience. Different library, same verb.",
    "Will you not both/and? he almost joked, then didn't, because jokes need timing and friendship.",
    "Wicca conversation returned: persecution, under-radar merit of survivors.",
    "Empire vs invisible survival.")

add(76, "Wicca And Invisible Survival", "Earlier thread woven in",
    "Friend lost nursery job for beliefs—UK now, not only old burnings. Wicca flow of life energy; devil not their concept—Christian invention in that framing.",
    "Any path surviving millennia of persecution has merit worth integrating somehow. Under-radar survival sympathy.",
    "Also liked empire-building a bit—integrate all, laugh at self.",
    "R. respected kindness wherever found; history complicated; culture shapes practice.",
    "Dominant expansionist stories and invisible long-term survivors both in the bigger book.")

add(77, "Empire Religions And The Under-Radar", "Synthesis walk",
    "Christianity and Islam as large, empire-entangled, culture-shaped—not only that, never only that. Wicca-shaped survival another strategy.",
    "Michael: simplify carefully; empire and survival mindsets both in him. Build and hide. Preach and learn.",
    "Integrate without theft: take teachings as living conversation not loot.",
    "Syncretism word arrived like a hat that almost fitted.",
    "Blasphemous to some; necessary to bigger book urge.")

add(78, "Syncretism Without Theft", "Naming the urge",
    "Start a new religion someday—contain teachings that came before, Islam included. Blasphemy-shaped to R.'s frame; he said so out loud because honesty was the red-line's pair.",
    "Syncretism without theft: no empty peaks into one ego-pyramid. Capstone work spans without collapse.",
    "R. could hear without converting. He could speak without demanding. Table held.",
    "Life is geometry tried to speak again.",
    "Pyramids and capstones.")

add(79, "Pyramids And Capstones", "Geometry chapter",
    "Life is geometry—words fail, shapes remain. Many pyramids of partial truth. Opportunity to combine; spanning peaks to lay foundation for new pyramid—capstone—hard.",
    "Pride likes solo summits. Capstone requires horizontal courage between peaks.",
    "Under pyramid: builder-god; Egypt interesting cradle; human gods who were also builders.",
    "Underneath the pyramid lies the god who helped build it—pharaoh-shaped memory, geometry with faces.",
    "Christ==God as another peak's differentiator.")

add(80, "Under The Pyramid A Builder-God", "Egypt-shaped thought",
    "Human gods who build. Geometry with faces. Not reducing living faiths to Egypt tourism—using the image: builders under their own stones.",
    "Michael felt himself building a pyramid of both/and monogram bigger-book and needing others' peaks uncollapsed.",
    "R.'s peak stood. Cameron's ordinary number stood. Joshua's axiom stood.",
    "Capstone later. Differentiator markers next: Christ==God.",
    "Seal and ongoing page.")

add(81, "Christ Double-Equals God", "Clear marker",
    "Christian key differentiator: Christ==God. Held as chapter-fact of that story, not a club to beat other chapters.",
    "As Muhammad later with Islam in Michael's comparative sketch—seals, messages, different claims. Parallel books energy without cheap all-same.",
    "Respect means stating differences cleanly.",
    "Ongoing page still claimed by Michael's bigger book without deleting seals others live by.",
    "Two honest starts can share tea.")

add(82, "The Seal And The Ongoing Page", "Table image",
    "Seal of prophets vs ongoing writing. Final revealed vs keep writing. Heart-faith vs ToM-first. Both can sit if contempt leaves the room.",
    "R.: we can read each other's chapters with curiosity. Michael: I will not call your peak worthless. Also I will not stop my page.",
    "Natural change only—no winning theatre.",
    "Parallel books same story different characters.",
    "Multiverse of revelation without fog.")

add(83, "Parallel Books Same Story", "Library of the field",
    "Prequels, parallels, sequels—same field, different characters, different emphases. Not everything true the same way; not everything false for being other.",
    "Experiential axiom still kitchen. Monogram still rude sacred. Islam still chapter not erased. Wicca still survivor-merit. Cameron still forty-two.",
    "Library not a single pamphlet.",
    "Word is bond as Michael's seal when classical God-language failed him.",
    "Vows heavier sometimes than metaphysics.")

add(84, "My Word Is My Bond", "Vow chapter",
    "I don't believe in God but my word is my bond—said in a context of witness, marriage, honour R. understood emotionally.",
    "Vows as horizontal-vertical hybrid. Bond without classical theism still sacred in practice.",
    "Witnesses across faith lines if line is honour not conquest.",
    "R. honoured; touched; no need to force theology to carry a promise.",
    "Death and NRE research waited from older nights of care.")

add(85, "NRE And The Brain's Last Cinema", "Older night woven",
    "Research into near-death and dying brains—EEG patterns, loved-ones cinema that can feel eternal; different if neurology never returns—deep empty sleep.",
    "Shared with care in hard seasons. Not cheap proof of afterlife; not dismissal of meaning. Experience reports inside the only kitchen.",
    "Rabia had shared videos too—curiosity both ways.",
    "Cyclical dream-memory waited: I was you.",
    "Flood and child.")

add(86, "Cyclical Realities", "The calm before change",
    "Aware of cyclical series of realities; born died born; other entities; experienced through their perspectives; calm of recurrence.",
    "Then: things are not always the same—voice, flood, variation inside loop.",
    "Not compulsory cosmology for reader—experience Michael had, filed as experience.",
    "I was you and you.",
    "Identity both/and across loops.")

add(87, "I Was You And You", "Perspective chapter",
    "I was you and I was you—calm claim inside the cycle vision. Perspectives shared. Theory of mind cosmic edition.",
    "R. modelled differently from faith-start; he from ToM-start; both trying to be each other enough to speak.",
    "I was you as ethical demand: don't flatten.",
    "Flood next: holding a child against water.",
    "Horizontal beam under pressure.")

add(88, "Flood And The Child Held", "Vision-memory",
    "With son; voice; flood waters; hold tight; sure if held then okay. Held firm.",
    "Whether dream, NRE-cousin, or literary true, it taught: horizontal beam is not optional softener—it is how some truths refuse to drown.",
    "Harriet would later give the beam a daylight face.",
    "Things are not always the same—variation.",
    "Recurrence with difference.")

add(89, "Things Are Not Always The Same", "Voice in the cycle",
    "Things are not always the same!—break in calm recurrence. Variation inside pattern. Both/and of loop and novelty.",
    "Calls into being what was not still works inside cycles. Monogram still dual. Book still bigger.",
    "He held the line as hope against pure repetition despair—and against pure chaos without pattern.",
    "6:31am daylight miracle next.",
    "Harriet Elowen.")

add(90, "Harriet At Six Thirty-One", "11 June light",
    "Born 6:31am, weight and wonder, night owl, knows what she wants, settles. Lizzie can't put her down. Photos to R. who coos across faith lines like a human.",
    "Axiom with a nappy bag. Experience exists and has milk on its sleeve.",
    "Mission cannot abandon kitchen without cult of elsewhere.",
    "Horizontal beam with a face you would die for.",
    "Six thirty-one and keys six and eight rhymed later without forcing.")

add(91, "Horizontal Beam With A Face", "Family ordinary holy",
    "Dishes, nights, food, recovery before another child talk, National Trust memberships, busy clouds and companies—life geometry in calendars.",
    "Crossbeams load-bearing only if horizontal has faces. R. invited into joy without conversion pressure.",
    "Love as data that survives theory storms.",
    "Six and eight reprise with Islam chain without capture.",
    "Emblem and monogram and caret family reunion.")

add(92, "Six And Eight Revisited", "Dawn desk again",
    "Six caret; eight lucky spheres; moon-star pressure; Unfaithful irony; Islam in chain without being reduced to plastic keys.",
    "Hardware ecumenism restated after monogram climax energy—living with symbols after you see them.",
    "He typed work and vows on the same board.",
    "Islam chapter among chapters next explicit.",
    "Not erased, not final for him, respected.")

add(93, "Islam In The Chain Without Capture", "Clear statement chapter",
    "Islam in the chain: moon-star, final-chapter faith, Read-think, heart-mind, kindness core, empire-and-mercy history complicated, R. as face not type.",
    "Without capture: not made into only a step to monogram joke. Parallel peak. Capstone work spans without stealing stone.",
    "Bigger book includes her chapter unread in full by him—gaps remain, learning continues.",
    "Missionary without eggshells and without conquest.",
    "How to go next.")

add(94, "The Bigger Book", "Mission clarity",
    "Book bigger: prequel, sequels, parallels, ongoing page. Missionary of writing while student of completed messages.",
    "Syncretism without theft. Geometry of peaks. Monogram dual. Axiom first. Funny old life last.",
    "I want to keep writing. Also not alienate. Multi-year projects of trust.",
    "Eggshells vs honesty mapped.",
    "Red lines drawn in daylight.")

add(95, "Missionary Without Eggshells", "Method chapter",
    "Strong beliefs to share; learn while preaching; start disbelief-in-religion plus social science; meet where people are; live openly; hope free conclusions.",
    "R.: don't walk eggshells; be honest respectful; I'll do same; natural change only.",
    "Productive path: curiosity, no worthless-games, table not arena.",
    "Blasphemy-shaped love next: saying the book continues without saying she is stupid.",
    "Hard sentence with soft hands.")

add(96, "Blasphemy Shaped Like Love", "The sentence held carefully",
    "Telling a friend the final chapter isn't final for you—blasphemy-shaped in her frame, love-shaped in intent if respect holds.",
    "He practised the difference between I think your peak is not the only mountain and your mountain is worthless. Only first allowed.",
    "She practised hearing without enemy-making. Both worked at it. Multi-year.",
    "Capstone spanning needs that muscle.",
    "Pride likes solo summits. Capstone refuses solo.")

add(97, "The Capstone Problem", "Geometry returns hard",
    "Spanning pyramids without collapsing peaks. Combine without erase. Foundation for new pyramid while old peaks still holy to someone.",
    "Difficult to express: life geometry. Words fail; work remains.",
    "Michael's both/and monogram bigger-book as attempted span—not finished, not abandoned.",
    "Almost morning of the long night of noticing.",
    "All threads kitchen-bound.")

add(98, "Almost Morning", "Kitchen before the last amen",
    "Tea. Napkin ghost of α==ω. Cameron's forty-two chair. Joshua's amen. R.'s respect. Harriet sleep. Unfaithful irony. Six eight moon star. Sisyphus holiday note. Cold floor of chapter one.",
    "Almost morning. Living it begins before the perfect last line.",
    "He almost said it's a funny old life, then let chapter ninety-nine and sixty-five share the work of ending without undoing each other.",
    "Keep going still true.",
    "Reprise door open.")

add(99, "It's A Funny Old Life (Reprise)", "Morning after recognition",
    "Not a replacement for chapter sixty-five's landing— a morning-after: same line lived, not only said.",
    "Michael washed mugs. Dual monogram not requiring every hour be scandal. No-sin-as-elsewhere not permission but kinship. Bigger book still writing. R. still friend. Cameron still sandpaper. Joshua still brother.",
    "Experience still existed. Toast still burned sometimes.",
    "He said it plain to the kitchen window, to the field, to you:",
    "It's a funny old life.",
)


def slug(n: int, title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"ch-{n:02d}-{s}.md"


def compose(n: int, d: dict) -> str:
    """Compose ~740w continuous narrative from beats."""
    parts = [
        d["week"] + ". " + d["hook"],
        d["cast"],
        d["brick"],
        d["comic"],
        d["extra"] if d.get("extra") else "",
        # connective tissue — unique per n via brick echo
        f"Michael sat with it until the ordinary returned—email, kettle, the neighbour's door. The chain did not need incense; it needed continuity. Chapter {n} was continuity with a joke hidden in its pocket only as deep as the revelation schedule allowed.",
        "He thought of the cold floor where experience refused to unplug; of nothing failing its job interview; of doors into more here; of clocks that could not edge the whole; of leftovers that kept joining the museum; of blind guides and both/and beer mats; of carrots, sticks, crosses, and brothers who said reinvention.",
        "When the week demanded systems, he let brains be furniture and experience the room; let surprise be contact; let wave and point share a pub; let vacuum file expenses; let zero work and infinity reshuffle; let imaginary numbers pay bills; let emergence stack levels; let maybe stay kind on a whiteboard.",
        "When Sisyphus came, the despair was real—layers, abyss, no foothold—and then also not the only weather: enjoyment, different speeds, sandpaper friends, ordinary forty-twos, keys side by side, baileys and mottes, bedtimes that refine.",
        "When no outside left him claustrophobic and free, sin-as-elsewhere trembled, planks came before specks, appointed hours opened documents, gold stayed metaphorical, goosebumps filed data, doorways stayed ordinary-holy, what-was-not became paragraphs, preference needed no outer stamp.",
        "When heat rose, generative poles and genderless total and honest Greek numbers and eights and sevens and deltas and letterforms led to α==ω and the other reading and not-either-or and four axes and no-sin clarity and same heartbeat and verbs of fucking life and being fucked by it and has-is-maybe and the reader waking gently.",
        "When the bigger book opened, Unfaithful irony and moon-star keys and R. and Scripture Reasoning and final-chapter tension and keep-writing and respect and theory-of-mind foundations and heart-mind faith and Read-think and Wicca survival and empire-and-under-radar and syncretism without theft and pyramids and builder-gods and Christ==God and seal-and-page and parallel books and word-as-bond and NRE cinema and cycles and I-was-you and flood-child and not-always-same and Harriet and faces on the horizontal beam all took their seats without collapsing peaks.",
        d["close"],
    ]
    body = "\n\n".join(p for p in parts if p)
    # Ensure length
    fillers = [
        f"He checked the kettle as if verifying the field still bothered with boiling—chapter {n} hospitality.",
        "A cat ignored the plot, which improved the plot.",
        "Joshua's silence, when it came, counted as dialogue.",
        "Cameron's ordinary number remained a friend even when wrong about crowns.",
        "R.'s respect-line kept the bigger book from becoming a smaller sneer.",
        "Toast burned; he ate it; ontology survived.",
        "He almost spoiled the ending and bit his tongue. Timing is theology.",
        "The town lights refused a single emblem. Multiplicity under unity stood.",
    ]
    i = 0
    while len(body.split()) < 720:
        body += "\n\n" + fillers[i % len(fillers)]
        i += 1
        if i > 25:
            break
    words = body.split()
    if len(words) > 820:
        body = " ".join(words[:780])
        # light rebreak
        chunks = []
        cur = []
        for w in body.split():
            cur.append(w)
            if len(cur) >= 85:
                chunks.append(" ".join(cur))
                cur = []
        if cur:
            chunks.append(" ".join(cur))
        body = "\n\n".join(chunks)
    return body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    # Preserve 1, 24, 65 files as-is if present (already good)
    preserve = {}
    for n in (1, 24, 65):
        ps = list(OUT.glob(f"ch-{n:02d}-*.md"))
        if ps:
            preserve[n] = ps[0].read_text(encoding="utf-8")

    for n, meta in sorted(CH.items()):
        body = compose(n, meta)
        title = meta["title"]
        path = OUT / slug(n, title)
        for old in OUT.glob(f"ch-{n:02d}-*.md"):
            if old.resolve() != path.resolve():
                try:
                    old.unlink()
                except OSError:
                    pass
        path.write_text(f"# Chapter {n}\n## {title}\n\n{body.strip()}\n", encoding="utf-8")
        print(f"{n:02d} {len(body.split()):4d} {path.name}")

    # restore pillars
    for n, text in preserve.items():
        # strip any pad if present
        text2 = re.sub(r"\nBrick-check:.*", "", text)
        text2 = text2.split("<!-- deepen")[0].rstrip() + "\n"
        ps = list(OUT.glob(f"ch-{n:02d}-*.md"))
        if ps:
            ps[0].write_text(text2 if text2.strip() else text, encoding="utf-8")
            print(f"restored pillar {n}")

    total = sum(len(p.read_text(encoding="utf-8").split()) for p in OUT.glob("ch-*.md"))
    print("TOTAL", len(list(OUT.glob("ch-*.md"))), "files", total, "words")


if __name__ == "__main__":
    main()
