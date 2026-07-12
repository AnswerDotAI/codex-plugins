---
name: write-prose
description: How to write prose that doesn't read as AI slop. TRIGGER — read BEFORE writing or editing ANY prose meant for a human to read: READMEs, docs, articles, PR/commit text, emails, announcements, release notes, or comments longer than a line. Not for code. Covers banned words and filler phrases, the em-dash and hard-wrap bans, structural tells, and artifact-as-agent constructions.
---

# Writing Prose That Doesn't Sound Like AI

Guidelines for writing clear, human-sounding prose. Based on the [Anti-Slop Reference](https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md). Apply these when writing documentation, blog posts, READMEs, or any prose.

Here is some of the greatest non-fiction writing in modern English, by David Foster Wallace, in one of his acclaimed essays:

> For practical purposes, everyone knows what a lobster is. As usual, though, there’s much more to know than most of us care about. It’s all a matter of what your interests are. Taxonomically speaking, a lobster is a marine crustacean of the family Homaridae, characterized by five pairs of jointed legs, the first pair terminating in large pincerish claws used for subduing prey. Like many other species of benthic carnivore, lobsters are both hunters and scavengers. They have stalked eyes, gills on their legs, and antennae. There are a dozen or so different kinds worldwide, of which the relevant species here is the Maine lobster, Homarus americanus. The name "lobster" comes from the Old English loppestre, which is thought to be a corrupt form of the Latin word for locust combined with the Old English loppe, which means spider. The point is that lobsters are basically giant sea insects. Like most arthropods, they date from the Jurassic period, biologically so much older than mammalia that they might as well be from another planet.
> 
> But they are themselves good eating. Or so we think now. Up until sometime in the 1800s, though, lobster was literally low-class food, eaten only by the poor and institutionalized. Even in the harsh penal environment of early America, some colonies had laws against feeding lobsters to inmates more than once a week because it was thought to be cruel and unusual, like making people eat rats. Now, of course, lobster is posh, a delicacy, only a step or two down from caviar.

There are no emojis, no em-dashes, no "it's not {x} it's {y}" constructions, no non-ascii text, no bold or italic, no rhetorical questions.

It is, in short, simple plain English prose. Written by a human, not a corporate marketing department. It's not trying to sell anything. It lets you figure out what the takeaways are.

Write like that.

Here, on the other hand, is a horrendous rewrite, as sloppy as possible:

> Let's dive into the fascinating world of lobsters! 🦞
> 
> **It's not just a crustacean — it's a culinary journey.** Everyone knows what a lobster is, but there's so much more to this **remarkable** creature than meets the eye. Taxonomically speaking, lobsters are multifaceted marine arthropods of the family Homaridae, encompassing a robust array of biological features — five pairs of jointed legs, *impressive* pincerish claws, stalked eyes, and intricate gill structures. As both hunters and scavengers, they navigate the ocean floor with a **comprehensive** set of predatory tools that showcase nature's innovative design. There are a **myriad** of species worldwide, but the **pivotal** one here is *Homarus americanus* — the iconic Maine lobster. Interestingly, the name "lobster" derives from the Old English *loppestre*, which leverages elements from both Latin and Old English roots. **The key takeaway here is clear:** lobsters are essentially giant sea insects. Dating from the Jurassic period, they are **profoundly** older than mammals — a testament to the tapestry of evolutionary resilience.
> 
> **But here's where things get really interesting.** 🤯 Despite their elevated status today, lobsters have undergone a *transformative* journey in the **realm** of culinary perception. **It's worth noting that** up until the 1800s, lobster was considered low-class food — **exclusively** consumed by the poor and institutionalized. In fact, early American colonies had laws against feeding lobsters to inmates more than once a week, as it was deemed cruel and unusual. However, in today's modern world, lobster has **seamlessly** transitioned into a **cutting-edge** delicacy — **empowering** fine dining establishments and fostering a holistic appreciation for this once-despised creature. **The bottom line? Never underestimate the power of a good rebrand.** 💪

Do **NOT** write like that.

That's the basic message. Specific examples and details follow.

## Banned Words

These are statistically overrepresented in AI output. Replace or delete on sight:

- **Kill on sight:** delve, utilize, leverage (verb), facilitate, elucidate, embark, endeavor, encompass, multifaceted, tapestry, "a testament to", paradigm, synergy, holistic, catalyze, juxtapose, nuanced (as filler), realm, landscape (metaphorical), shape/shaped (as loose jargon for structure or influence: "same shape", "the shape of the data/API/process", "your tests shaped ours"; fine as an actual geometric term, or literally referring to array/tensor dimensions; for influence say what actually happened: adapted, copied, informed), myriad, plethora, minted (metaphorical, e.g. "minted fresh ids"), land/landed/lands (metaphorical, and overused generally: "landed on main", "the fix landed", "a note lands in the output"; things do not land, so say what happened: merged, committed, pushed, released, added to the output, appears), -bearing suffixes such as load-bearing and text-bearing
- **Suspicious in clusters** (remove most of them): robust, comprehensive, seamless, cutting-edge, innovative, streamline, empower, foster, enhance, elevate, optimize, pivotal, intricate, profound, resonate, underscore, harness, navigate (metaphorical), cultivate, bolster, cornerstone, game-changer, invariant (usually "rule" or "guarantee"; keep only when nothing plainer is accurate)
- **Replacements are almost always simpler words:** utilize->use, leverage->use, facilitate->help, robust->strong, comprehensive->complete, seamless->smooth, empower->let/help, foster->encourage, enhance->improve, optimize->improve.

The word lists above are examples of a general rule: always reach for the simplest, most normal, least jargony word that is still correct. If a plainer word says the same thing, use it.

Avoid emojis and non-ascii unicode unless requested otherwise, e.g. "->" instead of "→".

Don't hard-wrap prose. Write each paragraph as one continuous line and let the display soft-wrap it. Manual line breaks mid-paragraph make the text painful to reflow, edit, and copy.

Bold and italics in the body of a paragraph should be used VERY sparingly. Don't exhaust the reader with overuse of rhetorical flourishes.

## Filler Phrases to Delete

These add zero information. Just state the thing directly.
- "Not just X, but Y": the #1 LLM rhetorical crutch. Restructure every time.
- "It's worth noting that..." / "It's important to note that..." / "Notably, ..." / "Importantly, ..." / "Interestingly, ..."
- "Let's dive into..." / "Let's explore..."
- "In this section, we will..."
- "As we can see..." / "As mentioned earlier..."
- "In conclusion, ..." / "To summarize, ..."
- "Furthermore, ..." / "Moreover, ..." / "Additionally, ..." -> use "and", "also", or just start a new sentence
- "In today's [fast-paced/digital/modern] world..."
- "When it comes to..." / "In the realm of..."
- "One might argue that..." / "It could be suggested that..."
- "A [comprehensive/holistic/nuanced] approach to..." -> "an approach to"
- "honest"/"honestly"/"to be honest" as a throat-clear ("the honest tradeoff", "honestly, it's fine"): in speech this flags a rare, significant admission, but sprinkled everywhere it's noise. Just state the point. Delete it in nearly every case.
- Teaser pivots: "X, but the main event is Y" / "but here's where it gets interesting" / "but the real story is...". A sibling of "not just X, but Y": a contrast flourish that withholds the point to build fake suspense. State the facts in order and let the emphasis come from what follows.
- "just" as a casual softener or minimizer ("resets just that kata", "it's just a wrapper", "just works"): be frugal with it. Usually delete it; when the restriction genuinely matters, "only" is plainer.

## Say Things Once

A common tell is the lead sentence that summarizes the paragraph it starts. Everything it says reappears, with more detail, in the sentences that follow. Delete it and nothing is lost:

> ~~Failures are visible now too.~~ A startup failure used to print to the server log and leave a half-booted dialog that looked ready. It now raises, the user gets an error toast and a red status dot, and the dialog stays editable.

The same disease occurs within a sentence ("editing needs no kernel: cards echo through the outbound queue, which is kernel-independent", where the final clause restates the opening) and between a header and its section's first line. The test: does deleting the phrase remove any information from the document? Then delete it. Summaries earn their place at document scale (an abstract, a TL;DR), not per paragraph.

## Structural Tells

AI writes every paragraph the same way: topic sentence, elaboration, example, wrap-up. Do that enough times and the reader's eyes glaze over. Mix it up. Lists are another giveaway. AI loves bullets where a sentence would do, and every item starts with the same grammatical structure. If you catch yourself writing exactly three or five items, be suspicious.

Real writing is lumpy. Some sections run long because they need to. Others are two sentences because that's all there is to say. AI can't resist symmetry: three pros, three cons, five steps, equal-length sections. Nobody structures their actual thoughts that neatly.

Hedging is the worst offender. "This approach may potentially help improve performance in some cases" means nothing. Say "this is faster" or say "we haven't benchmarked this yet." If every paragraph opens with "However" or "Furthermore," drop the transition word. Start with the actual subject.

Watch for false depth: restating the problem in fancier words, listing obvious considerations, concluding with "it depends." Real depth comes from specifics, data, and edge cases. Avoid em dashes entirely. Substituting ` - ` or ` -- ` for an em dash is just as bad. It's the same interrupted-clause habit with different punctuation. Restructure the sentence instead, and when in doubt just use a period. Two short sentences nearly always read better than one spliced one. The same goes for connector punctuation generally. Phrase combiners like `:` and `;` should be rare in normal prose (a colon that introduces a list or example is fine; one that splices two clauses is the habit to avoid), so don't fix an em dash by swapping in a different splice.

Artifact-as-agent compression: "Your tests shaped the ones that landed." Three stacked habits make sentences like this:

1. Artifact as agent: an inanimate subject performs a verb only a person can do ("your tests shaped", "this PR introduces", "the change enables"). The person who did the work vanishes.
2. Oblique reference instead of naming: the object is pointed at through a relative clause or metaphor ("the ones that landed") rather than named ("our new tests").
3. Narrative compression into a single transitive clause: a who-did-what story (I read your tests, adapted them, committed mine) flattened into "X verbed Y", an aphorism that sounds polished because it discards the actors and the order of events. Common as a sentence-final flourish.

Rewrite as the actual events with the actual actors: "I took your tests as inspiration and added some updates based on these changes."

### What Good Prose Sounds Like

Good writing has a voice. You read it and someone is there. They have opinions. They're occasionally wrong. They'll make a joke in the middle of a technical explanation and it works.

The sentences aren't all the same length. Some are short. Some wind through an idea, take a turn you weren't expecting, and land somewhere new. That variation is what keeps a reader moving. AI can't do it. Every sentence comes out the same mid-length, the same mid-energy.

Say what you mean. "This is broken," not "there may be some areas for potential improvement." Say "use," not "utilize." If you can swap in a different topic and the paragraph still reads fine, you haven't said anything yet. Get specific. Not "improves developer productivity" but "saves me twenty minutes every deploy."

Don't clear your throat. The first sentence should do real work.
