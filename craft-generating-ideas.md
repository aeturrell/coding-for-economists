---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.5.0
kernelspec:
  display_name: 'Python 3.10.12 64-bit (''codeforecon'': conda)'
  language: python
  name: python3
---
(craft-generating-ideas)=
# Generating and Accepting Research Ideas

In this chapter, you'll learn tips and tricks for both generating, and accepting, research ideas. The chapter is mostly advisory: it's not intended to be a foolproof guide, the last word, or to cover everyone's preferences--but it is designed to help you get started with generating research ideas and then deciding which ones to pursue and which ones to ditch.

Many people struggle to come up with really great ideas—indeed, it's probably the hardest part of research. But in this chapter, we'll try and help you do just that because, and this is the good news, it's *not* the case that ideas simply arrive unbidden: you can get into habits, and a frame of mind, that encourages ideas generation.

This chapter very much stands on the shoulders of giants. This includes Twitter advice by the likes of [EmilybyNight](https://x.com/EmilybyNight), [Anthony Lee Zhang](https://x.com/alz_zyd_), [Syon Bhanot](https://x.com/spbhanot), [Brad Shapiro](https://x.com/btshapir), and [Julia Bauma](https://x.com/JuliaBauman2). Additionally, this chapter draws on the writings of [Don Davis](https://www.artsrn.ualberta.ca/econweb/landon/Davis%20PhD%20Thesis%20Research%20Where%20to%20Start%202001.pdf), [Paul Niehaus](https://medium.com/@paul.niehaus/doing-research-18cb310529e0), [Jason Roberts](https://www.codusoperandi.com/posts/increasing-your-luck-surface-area), [Marco Tulio Rubiero](https://medium.com/@marcotcr/coming-up-with-research-ideas-3032682e5852), [Paul Graham](https://paulgraham.com/greatwork.html), and Pranav Rajpurkar's course on [AI Research Experiences](https://docs.google.com/document/u/0/d/15pnUpD47S6mAM-g4fwQvc2klYIb-GKgWex1oOlmNjvg/mobilebasic).

## Generating Ideas

It all starts with an idea. But where does that initial spark come from and how do you create it? You can probably do more than you realise to kick off the creativity that you need to start generating research ideas.

### You can improve your own luck

One useful way to think about making your own luck is 'increasing your serendipity surface area'. Sure, you work in a field, and you know, more or less, what's going on. But there are practices you can indulge in that will stir the pot of thoughts about your topic in your head and help to create new ideas from them.

It's perhaps useful to pause and think about what luck really is for a moment, because it will help to outline how you can give your own luck a nudge in the direction you want when it comes to ideas. In his 1978 book "Chase, Chance, and Creativity", James Austin talks about four kinds of luck in the context of creativity:

- blind luck, which falls out of the sky—think about being born wealthy
- persistent tinkering luck: stirring up existing thoughts, ideas, models, and other assets of research naturally leads to new combinations that are themselves valuable
- prepared mind luck: where you use your expertise and knowledge to apply judgement to see the value in what others might dismiss. You might latch onto a puzzle that others would ignore as an irrelevance. Louis Pasteur captured this well when he said "Chance favours the prepared mind".
- perfect storm luck, where you are the undoubted expert on a topic and are one of the few who is in the right place, at the right time, with the right knowledge to bring together everything that is required to create a brilliant new idea or approach.

While this can be a useful framework to think about what strategy might work best for you right now, the important point here is that blind luck is just one type of luck, and there is a LOT you can do to put yourself in a better position to generate ideas.

So what are the actions you can take to start improving your idea-generating powers?

### Goals vs systems and serendipity

Many trained in research are used to be goals-oriented: you have a specific objective in mind, and you go out and do it. However, serendipity, by its very nature, is not something you can go out one day and complete like a chore. Unlocking serendipity is more about habits and systems for behaviours that increase the chances that you'll discover information that could form part of a new idea. It's worth stressing this: coming up with original ideas isn't something that you can make happen at will, nor is it a linear path.

It is the routines and habits, rather than specific actions, that you'll need to help you generate ideas. A very simple example of a habit that increases your luck surface area is attending the weekly external seminar: not only will you hear about research that is valuable enough for someone to have been invited to talk about it, but you'll get to make a new contact too. Another example would be arranging to meet other researchers in your area to just talk through what's going on—it's amazing what different people read between the lines of papers, or what additional contextual information they can bring.

While we will see more detailed examples shortly, the headline message for how to increase your luck surface area is that you should stop "doing" so much and start putting yourself out there a bit, ie start "communicating" more. In the figure below, you want to trade-off the "doing" and "communicating" to maximise serendipitous idea discovery.

```{code-cell}
:tags: ["hide-input"]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_inline.backend_inline


# Plot settings
plt.style.use(
    "https://github.com/aeturrell/coding-for-economists/raw/main/plot_style.txt"
)
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

fig, ax = plt.subplots(figsize=(5, 5))
min_val = 0
max_val = 100
xline = np.arange(min_val, max_val, 1)
yline = xline
ax.plot(xline, yline)
ax.set_xlim(min_val, max_val)
ax.set_ylim(min_val, max_val)
pos_text = (0.9*max_val, 0.8*max_val)
ax.annotate("Ideal line", pos_text,
            xytext=pos_text,
            rotation=45,
            ha="right",
            size=15)
ax.annotate("Not enough doing", xy=(0.5*max_val, 0.6*max_val), size=15, ha="right")
ax.annotate("Not enough communicating", xy=(max_val, 0.2*max_val), size=15, ha="right")
ax.set_ylabel("Communicating")
ax.set_xlabel("Doing")
for axis in ['bottom','left']:
    ax.spines[axis].set_linewidth(4)
plt.xticks([])
plt.yticks([])
plt.suptitle("Serendipity Surface Area")
plt.show()
```

Often, your "communicating" will be without a specific purpose in mind because you don't know yet what ideas or concepts will flow out of the interaction—that's the point! Of course, it's highly uncertain how useful any particular interaction will be, and so goal-oriented people find this very hard. Because of this, it can be helpful to be systematic about how you go about communicating more, and how much time you spend on it. But zero time on this is too little time if you're trying to find good ideas.

### Finding content to throw into the brain mixer

If your brain is a bubbling pot out of which great ideas will emerge, you need to be throwing high quality ingredients in to sustain it. This is about changing your practices and habits so as to absorb content that will allow you to create those great ideas. So where do you get those good ideas and how can you keep track of them in a systematic way?

Some top tier places to look include:

- research in your own field. We really recommend setting up notification emails for working papers and journals in your field. With so much published, keeping on top of the literature has become a giant task, so the more you can pinpoint or filter down to what you're specifically interested, the better. You can also periodically search for relevant content (for more on search, see {ref}`craft-search`). In particular, in your reading, you might want to note down what datasets are available that others have used. Do not disregard survey papers. Attending conferences is one of the most powerful ways to keep on top of what's happening, but it is expensive—if you can't do that, check out recordings of the same talks as a cheaper alternative (but you do miss out on the chance to ask questions in the coffee break).
- research in adjacent fields. New ideas tend to come from connections that reach out of the core of your knowledge and into a fizzing, fuzzy periphery. Research in similar fields is in the 'adjacent possible' of your current knowledge, and therefore could form useful connections to what you're doing. (Research in far flung fields could too, but the chances are smaller, so you'll want to spend proportionately more time on adjacent fields.) Again, survey papers can be your friend here.
- courses. Human capital deprecates quickly, and, simply by topping it up with the latest methods from new university courses, new ideas could be sparked.
- newspapers, magazines, newsletters, blog posts, and books. For economics, the Financial Times and Wall Street Journal are obvious ones, but there are others with a wider appeal that may deal with important issues faced by, for example, consumers. Newsletters such as [Construction Physics](https://www.construction-physics.com/) and [New Things Under the Sun](https://www.newthingsunderthesun.com/) explicitly point to untapped research questions.
- the publications of regulators and other government or public sector bodies. Public sector institutions always have thousands more questions outstanding than they have the ability to answer simultaneously, and they do talk about them through their publications. You can simply go and read some of this content to pick up on questions that have a direct relevant to policy. They tend to be a great untapped resource, so you may find ideas that others have missed too.
- older books in libraries. You can get a long way by going to the library, heading to the section relevant to your field, and just picking out stuff that's been forgotten, neglecting, or out of fashion and seeing if it's due a reboot because it can say something about the current state of the world or because methods can now tackle it more effectively.
- conversations with people, especially if they are more senior (and have a birds' eye view) or are extremely fresh and don't accept everything that the rest of the discipline takes for granted
- what's going on in the world and affecting people, especially if no-one else seems to be talking about it through the lens of your field.

With all of these, you run the risk of getting bogged down in reading every detail: don't. The point here is to look over lots of content quickly and bag anything that could be useful later on, or which seems interesting even though there's not an obvious way to use it straight away. Hoover up these tidbits on a regular, disciplined basis and do not abandon the practice simply because it does not immediately lead to a great insight. Instead, think of this process as a long-term investment: you are filling your memory and note buffers. The more you have at your fingertips, the easier it is to make connections that spawn ideas.

One way to impose some order on the information flow (be it notes, references, pictures, charts, puzzles, oddities, links, or any other media), is to use one of these two free note-taking tools:

- Microsoft [OneNote](https://www.onenote.com/)
- [Obsidian](https://obsidian.md/)

Both of these are rich with features, and these are not the only ones available. You can read more about setting up Obsidian with the Zotero reference manager [here](https://aeturrell.com/blog/posts/til-zotero-and-obsidian/).

### Creative thinking processes and connections

One way to think of creativity is as the ability to see connections between things. In the previous section, there were lots of suggestions of where to get the building blocks of ideas from. But you need to be able to see connections, links, and interesting features of these in order to capitalise on all that information gathering.

Here are some ideas for how to capitalise on collected thoughts:

- Use some kind of note taking system to record ideas, thoughts, concepts, methods, or whatever other asset you think is foundational to your research creativity. You cannot memorise everything you have seen. As noted above, we recommend Microsoft [OneNote](https://www.onenote.com/) or [Obsidian](https://obsidian.md/) for this. Both offer ways to link between topics, and the latter will display the literal connections between pages you have on different topics.
- Ask the big questions of the information you have gathered. You can fit these into, broadly, three categories: those about your field, those about the real world, and those about the assets (data, methods) that are available. Some examples of each of these are:
  - 1. The field: What questions are others asking? What are they *not* asking? What is widely believed and how strong is the evidence for it? Where are people making assumptions? What are the big challenges to further progress? What is important but relatively under-examined?
  - 2. Reality: What is actually happening in the real world as it relates to your field? What decisions are people making because of it? How is the environment changing and why? What facts, patterns, or puzzles exist that have been neglected or misunderstood? What techniques are state of the art?
  - 3. Assets: What datasets are being used by people? What changes / natural experiments might be available to use to answer questions? What partners might be interested in collaboration? What new methods have been developed that could give a better read on an old question?
- Investigate failures and annoyances. Often, when a line of enquiry fails, people are tempted to discard it... but before you do, is the absence of a relationship as interesting—or *more* interesting—than its presence? Such failures, and even annoyances, are fertile ground for new research ideas, if you are willing to the time into understand the problem and its causes. At the very least, it's useful to file these blips away so that you can come back to them in future. Maybe you don't have many failures to hand: one way of generating them is to take a popular framework and apply it in a new context: it likely won't work, and then you have a thread to pull on. An example would be using an AI model architecture to do something new.
- Investigate puzzles. As the great plasma physicist Malcolm Haines once said at a dinner in his honour, "bring me your mysteries". Humans feel a draw towards a mystery that is as powerful as it is pervasive: think of how detective novels dominate the best seller lists! Whenever you see a puzzle, log it. It could be that there's an interesting phenomena underlying it, or that others noticed it too and would be grateful to understand it better. Be slightly wary of well-known "puzzles" that have already attracted much attention from giants of the field as, unless you're bringing a new angle, you already know that others tried and failed to crack them, so a number of ideas will already have been exploited.
- Use analogies and mapping. Try to find analogies that map across from a solved problem over here to a tough problem over there. This goes beyond applying technique Y to problem X, which often ends up being boring incrementalism. A deeper example would be applying the idea of vector subspaces to realms beyond, say, natural language processing and applying it to firms as a starting point to a natural and data-driven, rather than top down, firm classification. In mathematics, seeing the analogies across sub-fields has been astonishingly fruitful.
- Improve on what others have done. This is an obvious way to generate research projects. But be wary! First, there's a big risk of incrementalism—where you make a slight improvement than inevitably ends up with only a slight impact too. How many papers have economists seen that add a single extra feature to a VAR or DSGE model? It's rarely exciting or worthwhile. A frightening number of papers would struggle to sell their value add relative to what has gone before. Second, be a bit wary of the 'future research' section of papers because it's likely the authors are already thinking of doing those extensions and have an advantage in doing them, and because, if they were straightforward, the authors would have probably included them in the original paper. When you see an idea appear in that section of a paper, it's typically already been selected as being low return on investment: otherwise the authors would have done it! That all said, if you're strategic about the improvements you're working on, this is one of the key ways to get traction within your own research community. Pretty much every idea you exploit should be improving on some existing work in some way. It's more a matter of using unbiased critiques of a paper to generate the ideas than falling in with the views of the author(s).
- Think about what would be useful. What does everyone in the field need a framework for? What blocker do they keep running into? What would allow for the biggest amount of progress by the most people? Generally, these will be big projects that you might not be able to tackle unless you have the luxury of time and other resources. But sometimes you'll find a niche that you can inhabit that ultimately helps out a lot of your peers.

## Which ideas should you take forward and develop further?

You'll need to dispense with most of your ideas, because they'll be bad. In fact, most ideas are terrible. A hit rate of one good idea in every hundred wouldn't be bad.

If you're looking for a barometer for which ideas are 'good', imagine the paper has been published and the results are out in the world. Think: would you feel proud to have published that paper? Will it have an impact? If the work is successful, will it be easy to answer the questions in the hook and motivation section of {ref}`craft-writing-papers`? If the answer is no, or just indifference, it's probably not a good idea.

Of course, this assumes some kind of foresight. I don't think you can predict which papers will take off and which will be unfairly unloved. But even though any creative process is inherently noisy, and you cannot predict how an idea will go down, you are likely to be able to rank ideas—and that's all that's needed to develop

Even so, this may be easier said than done. A first pass would be to group the ideas into broad categories of strong, intermediate, and weak. But we'll now turn to other strategies you can adopt to develop ideas a little so that ranking becomes easier.

### Only accept punchy work

Narrowing to a smaller number of ideas to take forward is really important because you're not going to get the opportunity to do many papers *in your entire lifetime*. Let's say you are an extremely productive economist and manage to publish five papers a year: over a 30-year career, that's only 150 papers.

Good papers and bad papers take more or less the same time. Some people have called a similar version of this idea, "Summers' Law", after Larry Summers, and it says that it takes just as much time to write an unimportant paper as an important one... so you may as well focus on an important one! Some bad papers take *longer* to get published.

Given the huge time commitment of each one, there's no point working on papers that don't pack a punch. Another reason is that we live in a world with many distractions and limited attention. Most scholars want their work to be read, used, and even enjoyed. Also, if you are in economics, the returns from getting into a higher ranked journal are disproportionate, so you'll want to focus on quality over quantity. Finally, it's also sadly true that research papers rarely surprise to the upside—it's much more common for them to surprise to the downside and be less impactful than you'd hoped. Most of us have optimism bias about our own work, and will overestimate the impact. If you set about to do a merely okay paper, that's going to be the upper bound for what comes out at the end. Again, the lesson is that it's best to aim high, and focus on the ideas that pack a punch, rather than waste your time on bad ideas.

You also have to ask yourself: do you want to improve the world or do you want to publish papers in nice journals? Most of us want the ideas we spend time on to make a difference! Which is by far the best argument to dispense with the less good ideas and focus on the ones that you genuinely think will move the dial.

### Put your effort into the stages of developing an idea that are cheap

The model that Pixar uses to be such a hit factory is instructive here: even though they work in a creative and uncertain industry, film-making, they have hardly ever missed. The core of Pixar's trick seems to be i) put effort into the cheap phases and ii) aggressively iterate and improve upon the idea.

Under i), what's cheap is thinking: it's getting data, transforming data, and running analysis that is expensive. Effort spent doing a project is minuscule compared to effort spent planning it. So this means doing a lot of thinking about the process, what could go wrong, and what could go right, up front. It means rejecting a lot of ideas before doing any analysis whatsoever because, for example, the data aren't there, the natural experiment isn't plausible, or you don't have the right skills. Famously, talk is cheap (even if many with analytical leanings find it painful). If you have the germ of an idea, find an expert, friend, or peer you trust to keep it to themselves and quickly get constructive feedback on it that will save you, potentially, months or years of wasted time otherwise. And if the work isn't appealing or inspiring or feasible, it can be adapted quickly—without too much wasted effort.

That leads neatly into ii), which is aggressively iterating and improving. Few ideas start out great. They can be improved, but you probably need a combination of thinking and discussing to do it. Keep going round with it, tweaking and perfecting, until it really stands up as a good idea that can go the distance and that you'd be proud to deliver.

### Gaze into the future for fatal weaknesses; try to fast fail

When you come up with an idea, it's very tempting to overlook any issues or weaknesses, and think 'I can cross that bridge when I come to it'. But you need to do the complete opposite. You must obsessively look for the weaknesses and focus on them, for they are what will hold back the work. As an example, suppose that a piece of work relies on three things to work; the first two will come off with probability 80%, while the third is only has a probability of 20% of working. All else equal, you should first try to figure out whether the third part will work or not. More than likely, it won't and once you've thought through it enough to realise this, you can discard the project and move on without wasting any more time.

The 'fast fail' or 'fast first cut' is another way of articulating the same philosophy: start to try something out, see if you can kill it easily because of some fundamental, unconquerable issue, and, if you can't, that's a good sign that it might have potential. Equally, your fast fail might quickly discover that the effect size must be bounded between zero and a small number, and you might know from the context that this will not interest many people, so you can break it off there (though null results can be *extremely* interesting depending on the context). The economist Steven Levitt recommends killing off projects very quickly, and puts his productivity partly down to this approach. However, do note that this has the potential to create distortions in the results that get published and it may not be good for the field as a whole is everyone does this aggressively, all the time. But there has to be some balance between personal pragmatism and theoretical best practice (until incentives become magically aligned by a better system for rewarding research).

The kinds of questions you should be asking yourself for both of these approaches involve some future-gazing. You want to know what the possible spectrum of outcomes looks like, and how likely it is that each part of the project succeeds or fails in its objectives, and whether—if some does fail—there is anything that would be recoverable. Some projects will have very spiky profiles, others are more defensible regardless of what they find—you can balance the overall risk by having a portfolio of projects. But even a very rough estimate will force you to think through the constraints around success. Specific questions might include: "What impact will this project have if it succeeds?" and "What is the shortest path to seeing if this idea works or not?" Again, you can't predict the future so you'll want to acknowledge there's some randomness you can throw into the mix here, and that the best you can do is get a rough sense (which is all you need to move forward).

### Choose work that is robust, including to changing circumstances
