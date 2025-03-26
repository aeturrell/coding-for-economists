(craft-technical-reports)=
# Writing Technical Reports

In this chapter, you'll find guidance on writing *technical reports*. It is mildly opinionated about what technical reports are and should be: the idea is to give you an easy to follow recipe that will produce a pretty strong technical report. As ever with writing, and especially with an output format that is so heterogeneous, there may be good reasons to take a different approach to the one outlined below.

This chapter has benefitted from The Institution of Engineering and Technology's guide on [Technical Report Writing](https://www.theiet.org/media/5182/technical-report-writing.pdf) as well as numerous other sources.

Technical reports are fundamentally different to research papers (covered in {ref}`craft-writing-papers`) or research blog posts (covered in {ref}`craft-research-blogs`). In a research blog post or a research paper, the analytical finding (and the narrative around it) is the star of the show; in a technical report, processes and methods are the stars, even though findings may be included. Technical reports are about documenting, well, technical details. They should have enough detail for the reader to understand and perhaps even reproduce the methods under discussion (or know where to start with it).

Another way that technical reports may differ from a research paper is that they *can* contain the less exciting bits of methodology and process that shouldn't make it into a paper. This can very much include dead ends, and, in fact, technical reports are as important for what they say about what *doesn't* work as what they say about what does.

## Tips for Writing Technical Reports

{cite:t}`zinsser2006writing` and {cite:t}`white1972elements` are two excellent general resources on writing. Perhaps the first and most important tip is to read one or both of these and take on board their lessons.

Let's go through some tips that are more specific to technical reports:

- Keep the report as short and as concise as possible (while conveying the relevant information). A technical report is not an excuse to waffle and anyone reading it will only be too grateful if they can extract the information without having too wade through too many words.

- Organise and signpost the report for the convenience of the reader. That means hyperlinks, decimal numbered sections (for example "1.2.1 Methods") with clear titles, figure captions, and a structure that follows a logical order. See the next section for a suggested structure.

- Include references so that further information is easy to find.

- Put charts, tables, and diagrams next to the point in the text where they are first mentioned. If you refer back to them, use a reference, preferably with a hyperlink.

- Use vector graphics for pretty much all figures except for photographs. In practice, this means using svg or pdf figures over ones in jpg or png file types. Most visualisation packages will export to multiple file formats, including svg. Later in the chapter, you'll see how to automate the inclusion of svg charts in a wide range of document formats (yes, even Microsoft Word).

- What output format you need to use (docx, markdown, HTML, PDF) will depend strongly on your particular context.

- Put the reader first. Do not digress into details that are not relevant to achieving a similar technical outcome. Likewise, although you can include more detail than you would in a paper, you needn't give the comprehensive history of you have arrived at your knowledge, just the knowledge itself.

- Signpost other outputs related to the same project, and do it early. If there's an accompanying code repository, paper, dataset, or software package, the introduction is probably the place to mention them (you can always give more detail on those additional outputs later in the report if needed).

## Structuring a Technical Report

This is only a suggested structure, and even then only at a high level of detail. To ensure the reader gets sufficient signposting and can quickly and efficiently navigate your technical report, you will probably need to have multiple numbered sub-sections within the sections suggested below.

- Title: hopefully this is self evident but if you're putting multiple outputs in one place (eg on the same landing page of a website), you may wish to warn visitors to your site that this is a technical report by putting 'Technical Report' in the title.

- Executive Summary: An as-short-as-possible few paragraphs on what, why, who, how, when, outcomes, and where to find further assets (code, data). Having read this, and only this, a reader should have a complete picture of what's in the rest of the technical report. An executive summary can be longer than an abstract would be for a paper, but the shorter you can make it while conveying the necessary information, the better.

- Background or Context: Cover the context of the work, as briefly as possible. Can have, at most, a couple of paragraphs on prior art (don't bother with a full literature review). If you need to give details on how the report was commissioned that goes beyond what is in the Executive Summary, this is the place.

- The sections that make up the body of the report: we now move on to the nitty gritty details. This is where you may wish to have one section or multiple sections, for example, you may want to cover "Methodology", "Data", "Data Linkage". What you will cover in the section and sub-section headings will depend on your project, but the key point is to be generous in providing them so that a reader who is skimming the report can find what they're looking for quickly.

- Conclusions: this is a summary of what you have said in the body sections *without* going over the same ground as the Executive Summary or Background. At the risk of stating the obvious, it is the place to provide, in prose, conclusions on the benefit/effectiveness/difficulty/etc of the methods or processes.

- Recommendations: if appropriate (it won't always be), this section is the place to boil down what you have learned into guidance that others can use. Be aware that some readers may only look at the executive summary and the recommendations. There is nothing wrong with providing your recommendations in a bulleted list to make them easier to digest.

- References: the full info on the citations you made in the main piece.

- Appendices: try not to have them at all (but sometimes they are necessary). They can sometimes be a good place to put things that aren't essential to the report but are needed for completeness, for example code showing how something was implemented that is so long it would break up the main report too much.

## A Template for Technical Reports

This section covers how to easily write your technical reports while following all of the best practice detailed in the previous sections. Some of the content is similar to what is in {ref}`quarto`.

One of the first choices you need to make when writing a technical report is what tech to use.

You can, of course, just write your technical report in Microsoft Word. This gives you useful features like tracked changes and, for a text heavy document, is not a bad choice. However, there are limitations such as formatting weirdness, difficulties with references, the lack of automation of any code-generated elements, and the lack of easy export to other formats.

The rest of this section introduces an alternative, *quarto markdown*. This approach is in the spirit of what some people call 'literate programming', which mixes code (and code-related approaches) along with writing. Below, there is a quarto markdown template to help you get started.

The advantage of an approach based around markdown is that code-generated elements, references, hyperlinks, formatting, export to other formats, and more, are taken care of, and you can use version control on your report. (These won't be necessary or even desirable for some reports, but being able to use them if you need is *very* handy.)

Quarto markdown files have a ".qmd" file extension and look a lot like markdown, or they can be written in a Jupyter Notebook. Vanilla markdown (with file extension ".md") is the subject of the chapter {ref}`wrkflow-markdown`, and if you haven't yet looked at that, you may want to have a quick skim before reading the rest of this chapter. Quarto markdown is a superset of the markdown syntax, the main difference being that quarto has executable code blocks in addition to the usual markdown features.

To create technical reports using quarto markdown, you will need Jupyter Lab (which can be installed using `pip install jupyterlab`), an installation of a programme called [Quarto](https://quarto.org/), and the other Python packages as used below or for your outputs. For some types of output, you’ll also need to have an installation of the typesetting language LaTeX, for which this book recommends the [MikTeX](https://miktex.org/) distribution. If you get stuck, the documentation on the Quarto website is very good. (Under the hood, quarto uses pandoc, so you may recognise some commands from pandoc in the below.)

The template below can be put into a Jupyter Notebook (.ipynb file) instead but, as technical reports tend to be text-heavy, we'll be using a quarto markdown file (with extension .qmd) as the template. To use the template, you can copy the contents below and paste them into a new, empty file called `technical_report.qmd` which you then open in VS Code.

Once you've written your technical report as a quarto markdown file, you can export it using

```bash
quarto render technical_report_template.qmd --to docx --wrap=none
```

on the command line. This will produce a Word document. Replace `--to docx` with `--to html` or `--to gfm` or `--to pdf` to produce HTML, Markdown, or PDF output, respectively. The `--wrap=none` keyword argument stops the exported markdown having a newline after every link.

Let's now run through the sections in the template below.

The bit delineated with three dashes is the "yaml" header. This provides various instructions as to how to compile the technical report from qmd to the various output formats. It's hopefully quite self-explanatory, but there are lines that control:

- the title
- the name of the Jupyter kernel you want to use to execute the code (run `jupyter kernelspec list` on the command line to get a list of these)
- the name of your bibliography file, using the .bib format
- the name of the citation style language file if you're using one. You can delete this line if you wish and it will just use the default one. If you wish to use the Nature one as in the template, you can find it [here](https://github.com/citation-style-language/styles/blob/master/nature.csl) but there are .csl files for lots of journals and styles [here](https://www.zotero.org/styles).
- whether to create citations with hyperlinks
- whether to have a table of contents
- how deep in sub-section titles the table of contents should go
- whether to number sections
- the format of any images that you are linking to with, for example, the `![alt-text](path/to/image)` syntax. SVG is a really strong default choice, so what's below assumes that images that are included in this way that do not have extensions are SVG files. You can also specify `![alt-text](path/to/image.svg)` though.

Next we hit the content, which uses the typical markdown syntax featured in {ref}`wrkflow-markdown`. In the template below are examples of some of the key features, including:

- a citation, `@zinsser2006writing` where the part after the `@` is the key for that entry in your .bib file. How it looks once exported will depend on whether and what csl file you used. 
- a link, `[Coding for Economists](https://aeturrell.github.io/coding-for-economists)`, which renders as [Coding for Economists](https://aeturrell.github.io/coding-for-economists)
- an equation, for example `$$ V(x)=\max_{c\in\Omega(x)} U(x,z)+\beta\left[V(x^\prime)\right] $$`, which renders as $$V(x)=\max_{c\in\Omega(x)} U(x,z)+\beta\left[V(x^\prime)\right]$$
- code blocks that are static (ie do not get executed), and that begin with backticks and the language, eg ` ```python `
- code blocks that get executed, with a toggle (`#| echo: true` or `#| echo: false`) for whether to include the input code as well as the output. These are deisgnated as ` ```{python}`, ie like the static ones but with the language in curly brackets. The output is typically a chart but it could also be a table (**pandas** dataframes get rendered as tables like you'd expect). Note that, by running the magic line `matplotlib_inline.backend_inline.set_matplotlib_formats("svg")` below, we ensure that the embedded charts are vector graphics *even when exporting to Microsoft Word* 🔥 🔥 🔥 .
- A bit of syntax that generates the bibliography—omitting this will still see a bibliography included, it will just be at the very end instead.

````markdown
---
title: "Technical Report: Title"
jupyter: python3
bibliography: references.bib
csl: nature.csl
link-citations: true
toc: true
toc-depth: 2
number-sections: true
format:
  html:
    default-image-extension: svg
  gfm:
    default-image-extension: svg
  word:
    default-image-extension: svg
---

# A top level section heading

## A sub-section heading

An example of a citation would be @zinsser2006writing, while an example of a link would [Coding for Economists](https://aeturrell.github.io/coding-for-economists).

## Another sub-section

To do equations, enclose latex with two dollar signs.

$$
{\displaystyle {\frac {\partial L}{\partial q^{i}}}(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))-{\frac {\mathrm {d} }{\mathrm {d} t}}{\frac {\partial L}{\partial {\dot {q}}^{i}}}(t,{\boldsymbol {q}}(t),{\dot {\boldsymbol {q}}}(t))=0,\quad i=1,\dots ,n.}
$$

Of course, you can give examples in (non-executed) code too:

```bash
quarto render technical_report_template.qmd --to docx --wrap=none
```

## Executable Code

To show the code and outputs, use

```{python}
#| echo: true

print("Hello World")
```

or 

```{python}
#| echo: false

print("Hello World")
```

for just the outputs. Note that instead of the usual `python` at the start of the blocks, it's `{python}` for executable code.

# Figures

To get the figures generated from executable code chunks to be in svg format automatically, you will need to include this code block before any that produce charts:

```{python}
#| echo: false

# This is a key line that ensures output plots generated in-line are svg and not png.
# Works with Word (but not Libre Office), HTML, and markdown outputs.
import matplotlib_inline.backend_inline
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")
```

And to give a code example that generates a figure (but doesn't show the code), it would be:

```{python}
#| label: fig-error
#| fig-cap: "A coefficient plots with standard errors"
#| echo: false

x = [2, 4, 6]
y = [3.6, 5, 4.2]
yerr = [0.9, 1.2, 0.5]

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr, fmt='o', linewidth=2, capsize=6)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()
```

We can refer back to this figure later using @fig-error.

# References

To generate your bibliography anywhere other than the end of the document, you'll need to use

::: {#refs}
:::

And this leaves you free to have your appendix separate.

# Appendix

And this is where that appendix material can then go.

````

That concludes everything you should need to start creating well-written and structured technical reports with vector graphics, reproducible charts and figures, clearly numbered and signposted sections, equations, code, references, links, a table of contents, and more!
