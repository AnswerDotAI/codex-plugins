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

- **Kill on sight:** delve, utilize, leverage (verb), facilitate, elucidate, embark, endeavor, encompass, multifaceted, tapestry, "a testament to", paradigm, synergy, holistic, catalyze, juxtapose, nuanced (as filler), realm, landscape (metaphorical), myriad, plethora
- **Suspicious in clusters** (remove most of them): robust, comprehensive, seamless, cutting-edge, innovative, streamline, empower, foster, enhance, elevate, optimize, pivotal, intricate, profound, resonate, underscore, harness, navigate (metaphorical), cultivate, bolster, cornerstone, game-changer
- **Replacements are almost always simpler words:** utilize->use, leverage->use, facilitate->help, robust->strong, comprehensive->complete, seamless->smooth, empower->let/help, foster->encourage, enhance->improve, optimize->improve.

Avoid emojis and non-ascii unicode unless requested otherwise. Eg "->" instead of "→".

Bold and italics in the body of a paragraph should be used VERY sparingly. Don't exhaust the reader with overuse of rhetorical flourishes.

## Filler Phrases to Delete

These add zero information. Just state the thing directly.
- "Not just X, but Y" — the #1 LLM rhetorical crutch. Restructure every time.
- "It's worth noting that..." / "It's important to note that..." / "Notably, ..." / "Importantly, ..." / "Interestingly, ..."
- "Let's dive into..." / "Let's explore..."
- "In this section, we will..."
- "As we can see..." / "As mentioned earlier..."
- "In conclusion, ..." / "To summarize, ..."
- "Furthermore, ..." / "Moreover, ..." / "Additionally, ..." → use "and", "also", or just start a new sentence
- "In today's [fast-paced/digital/modern] world..."
- "When it comes to..." / "In the realm of..."
- "One might argue that..." / "It could be suggested that..."
- "A [comprehensive/holistic/nuanced] approach to..." → "an approach to"

## Structural Tells

AI writes every paragraph the same way: topic sentence, elaboration, example, wrap-up. Do that enough times and the reader's eyes glaze over. Mix it up. Lists are another giveaway. AI loves bullets where a sentence would do, and every item starts with the same grammatical structure. If you catch yourself writing exactly three or five items, be suspicious.

Real writing is lumpy. Some sections run long because they need to. Others are two sentences because that's all there is to say. AI can't resist symmetry: three pros, three cons, five steps, equal-length sections. Nobody structures their actual thoughts that neatly.

Hedging is the worst offender. "This approach may potentially help improve performance in some cases" means nothing. Say "this is faster" or say "we haven't benchmarked this yet." If every paragraph opens with "However" or "Furthermore," drop the transition word. Start with the actual subject.

Watch for false depth: restating the problem in fancier words, listing obvious considerations, concluding with "it depends." Specifics, data, edge cases: that's where real depth lives. Avoid em dashes entirely.

### What Good Prose Sounds Like

Good writing has a voice. You read it and someone is there. They have opinions. They're occasionally wrong. They'll make a joke in the middle of a technical explanation and it works.

The sentences aren't all the same length. Some are short. Some wind through an idea, take a turn you weren't expecting, and land somewhere new. That variation is what keeps a reader moving. AI can't do it. Every sentence comes out the same mid-length, the same mid-energy.

Say what you mean. "This is broken," not "there may be some areas for potential improvement." Say "use," not "utilize." If you can swap in a different topic and the paragraph still reads fine, you haven't said anything yet. Get specific. Not "improves developer productivity" but "saves me twenty minutes every deploy."

Don't clear your throat. The first sentence should do real work.
