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
  display_name: 'Python 3.8.12 64-bit (''codeforecon'': conda)'
  language: python
  name: python3
---
(craft-research-blogs)=
# Research Blog Posts

In this chapter, there are hints and tips for writing impactful blog posts that summarise research or analysis. To make the distinction with blogging more generally, the chapter is called 'research blog posts', but the advice could apply to any complete analytical project. As in other chapters on craft, although the text below may say 'do this' or 'don't do that', there are few universal rules in writing and what's appropriate for your project may be something completely different. But following these guidelines should give you a solid place to start if you need one.

## Introduction

Blogs are a really useful way of getting your work to a wider audience. It's helpful to think of how many people will engage with the dissemination outputs you create as following the *inverted pyramid of research dissemination*. Note that these are outputs you create, so don't count media articles about your work. At the top layer of the pyramid, you can draw a large number of people in via social media, including people who might not otherwise have ever thought about or seen what you're doing. At the next rung down, you get another opportunity to pull probably slightly fewer people into somewhat more detail with a blog post, the subject of this chapter. At the next layer down is the paper and, given a large number of papers go uncited, you may be lucky if tens of people read that front-to-back. Finally, right at the bottom—though no less useless for being so—is the code and/or replication packet, to be seen by a small number.

```{code-cell} ipython3
from craft_diss_pyramid import plot_pyramid
plot_pyramid()
```

Each stage of the inverted pyramid is valuable, but it's important to recognise that:

- without the bottom layers, the top layers might not be very solid, so be wary of putting out arguments and conclusions that don't rest on deeper analysis
- most people will only ever engage with the upper layers; they don't have time to read your paper but they might read a thread or blog post
- more people will know about your work if those upper laters exist, and they will push more people down to lower layers
- most people doing analysis or research want people to read it and be influenced by it

In this view of dissemination, you can think of a research blog post as a poster for your deeper analysis: it is a punchier, shorter, and likely more exciting version that can also signposts people to your paper should you catch their attention. Popular blog site VoxEU uses the description "research-based policy analysis and commentary".

## How to think about your Research Blog Post

Alongside the inverted pyramid of dissemination, above, there is another inverted pyramid that gives a suggested structure for research blog posts. This following the classic inverted pyramid of news as used by journalists. Just as with dissemination of research more broadly, more eyeballs will reach the top layer than the bottom, and more of the detail will emerge in the bottom layers.

If it is to effective, your blog post cannot be too long; 800 words a good target, and definitely no more than 1500. Many places that you would want to publish the blog will have limits anyway, but even if it's on your own website, if you're summarising a research project you probably want to make it *substantially* shorter than the paper.

Let's run over some other general tips for writing good research blog posts:

- The threshold is a lot lower than you think! A blog post that isn't perfect will still drive more traffic to your work than one that wins a Pulitzer. Also, experience is easily the best way to improve for next time.