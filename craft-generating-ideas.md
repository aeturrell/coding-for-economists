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

This chapter very much stands on the shoulders of giants. This includes Twitter advice by the likes of [EmilybyNight](https://x.com/EmilybyNight), [Anthony Lee Zhang](https://x.com/alz_zyd_), [Syon Bhanot](https://x.com/spbhanot), [Brad Shapiro](https://x.com/btshapir), and [Julia Bauma](https://x.com/JuliaBauman2). Additionally, this chapter draws on the writings of [Don Davis](https://www.artsrn.ualberta.ca/econweb/landon/Davis%20PhD%20Thesis%20Research%20Where%20to%20Start%202001.pdf), [Paul Niehaus](https://medium.com/@paul.niehaus/doing-research-18cb310529e0), [Marco Tulio Rubiero](https://medium.com/@marcotcr/coming-up-with-research-ideas-3032682e5852), [Paul Graham](https://paulgraham.com/greatwork.html), and Pranav Rajpurkar's course on [AI Research Experiences](https://docs.google.com/document/u/0/d/15pnUpD47S6mAM-g4fwQvc2klYIb-GKgWex1oOlmNjvg/mobilebasic).

## Generating Ideas

It all starts with an idea. But where does that initial spark come from and how do you create it? You can probably do more than you realise to kick off the creativity that you need to start generating research ideas.

### Improving your own luck when it comes to ideas

#### You can improve your own luck

One useful way to think about making your own luck is 'increasing your serendipity surface area'. Sure, you work in a field, and you know, more or less, what's going on. But there are practices you can indulge in that will stir the pot of thoughts about your topic in your head and help to create new ideas from them.

It's perhaps useful to pause and think about what luck really is for a moment, because it will help to outline how you can give your own luck a nudge in the direction you want when it comes to ideas. In his 1978 book "Chase, Chance, and Creativity", James Austin talks about four kinds of luck in the context of creativity:

- blind luck, which falls out of the sky—think about being born wealthy
- persistent tinkering luck: stirring up existing thoughts, ideas, models, and other assets of research naturally leads to new combinations that are themselves valuable
- prepared mind luck: where you use your expertise and knowledge to apply judgement to see the value in what others might dismiss. You might latch onto a puzzle that others would ignore as an irrelevance. Louis Pastuer captured this well when he said "Chance favours the prepared mind".
- perfect storm luck, where you are the undoubted expert on a topic and are one of the few who is in the right place, at the right time, with the right knowledge to bring together everything that is required to create a brilliant new idea or approach.

While this can be a useful framework to think about what strategy might work best for you right now, the important point here is that blind luck is just one type of luck, and there is a LOT you can do to put yourself in a better position to generate ideas.

So what are the actions you can take to start improving your idea-generating powers?

#### Goals vs systems and serendipity


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

### Finding content to throw into the brain mixer

INCLUDE SOMETHING ON MANAGING NOTES etc

INCLUDE MAKING CONNECTIONS

### Improving what others have done

### Failures, puzzles, and annoyances

### Analogies
