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
(craft-referee)=
# Writing Referee Reports

In this chapter, you'll learn tips and tricks for writing referee reports. Much of this chapter is advisory: some of it might work for you, some of it might not. It's not intended to be a foolproof guide, or to cover everyone's preferences--but it is designed to help you get started on writing good referee reports.

What is the purpose of a referee report? We think there are two:
1. help the editor make a decision about whether to publish the paper in their journal
2. help the authors improve the paper

At first glance, it may seem like 1. is the more important: after all, it's the editor who has asked your opinion. And indeed it's good to do 1. effectively. But why do we have journals, and editors, and selection of papers at all? It's to establish scholarly truth and increase the sum total of knowledge of the world. Regardless of whether or not this particular paper gets published in this journal is, in the grand scheme of things, just not that important--what matters is that the paper makes the biggest scholarly contribution it can. So, in the long run, it is 2. that is far more important. Happily, these two objectives are rarely if ever at odds and a good referee report will do both without taking up too much of your time either.

## Deciding whether to accept a request to referee a paper

In general, your prior for refereeing should be to accept the request unless you have a good reason not too. Reviewing is, to state the obvious, an essential part of the peer review system. As well as greasing the wheels of the evolution of knowledge, reviewing will inevitably help you to become better at writing papers too: once you start seeing the mistakes other authors make, you will take extra efforts to avoid them yourself.

The first question to ask yourself is whether you have sufficient expertise to provide a good review of the paper. Of course, there's a reason why the editor chose to send the paper for you, and they will likely have factored in your expertise when making the decision. But if you feel that you cannot usefully comment on the manuscript or the overall contribution to the field, it may be best to ask the editor what they expect your role to be. If your expertise allows you to comment on some key sections of the paper, you can offer to review these areas and let the editor know you cannot comment on other aspects outside your expertise. In marginal cases, verifying the role the editor is expecting you to play can be helpful--and you may end up passing it up entirely in the rare case that a mistake has been made in offering it to you to review.

The second question you should ask yourself is whether you can provide a fair and ethical review! You should notify the editor if you are working on a paper with significant overlap to the one you have been assigned to review. The same goes for if you have a conflict of interest too: maybe you are so close to the authors that you feel you cannot provide a fair and unbiased review or perhaps you would be unduly negative!

Finally, you need to ask yourself whether you have the time to review the paper. The timing of reviewing and returning papers can determine entire careers, unfortunately, so sitting on a paper that you optimistically accepted but cannot now find the time for is unhelpful to everyone.

## Reviewing a paper

### Reading the paper

Our advice is that you begin by reading a paper all the way through and resist the temptation to start making notes or tut tutting under your breath. In your head, use the first reading to form an initial assessment of the authors’ question, approaches, and conclusions: and whether the paper is publishable in principle based on its contribution to the field. The first reading should help you answer questions like, "What is the main question addressed by the research? Is this question pertinent to the field of study? Do the results of the research contribute substantively to the question? Are you convinced that this is a worthwhile topic?".

On your second read-through you will likely want to start to dig into details, annotating and highlighting as you go. (This book recommends [Zotero](https://www.zotero.org/) for this.) As you read, you will want to answer questions in the following categories:

- The topic and contribution
  - Do you have a good idea what the authors are doing?
  - Is the topic clearly explained?
  - Does the author do a good job of motivating the question in the introduction?
  - Is the answer to the question obvious in advance? 
  - Is the question original?
  - What is the contribution of the paper?
  - Does the author pose a question of reasonable scope (i.e., can she reasonably hope to answer the question in a short empirical paper)?
  - Does the author use causal language to describe a correlational finding, or confuse cause and effect in other ways?
- The data:
  - Does the author present a clear description of the data? Is there a summary statistics table?
  - Does the author's choice of a dataset seem well suited to answering the question posed?
  - If you had to replicate the author's study five years from now, is there sufficient information in the paper about the source of the data and sample used that you could do it?
  - Does the author discuss issues that may affect the data, for example "dark data" {cite:t}`hand2020dark` (see {ref}`craft-writing-papers` for more on the types of dark data)?
- The model, if there is one:
  - Is there a clear description of what it does and what its assumptions are?
  - Does the model incorporate those aspects of reality that the author seems to think are important?
  - Is it possible to answer the question posed by the author within the context of the model?
  - Is the model unnecessarily complex? Could the author attack the problem with a simpler model?
  - Is the model internally consistent?
  - Have alternative specifications been tried and compared, when necessary?
  - Is the issue of robustness of the results addressed?
- Results and Conclusion
  - Are the results clearly stated and presented?
  - Is it likely that typical statistical errors, such as mean reversion or selection bias, could explain the results?
  - Are there mistakes in causal reasoning, eg does the author control for or condition on variables that could be affected by the treatment of interest?
  - Does the author have sufficient statistical power to test the hypothesis of interest reliably?
  - Are the mechanisms plausibly explained?
  - Are they used in some interesting way (beyond quoting the value of the parameters and their standard errors)?
  - Are the results related back to the question?
  - Are appropriate caveats mentioned?
  - Are the conclusions reached by the author well supported by the evidence?
- Finally, would you have been pleased to have written this paper?

### The referee hot take

At this stage, you can reflect on what you've found so far and *evaluate whether the paper is publishable in principle*: if so, continue with the review (detailed below); if not, for example if the paper is flawed in a way that cannot be fixed and which you believe renders it categorically unsuitable for publication in the target journal or is very below the bar of the journal in terms of contribution to the literature, you can write up a short review. This must set out clearly, and with evidence, why the paper is unsuitable. Even in this case, you should be polite and constructive, and help the authors understand what the main issue is--but don't waste space on minor issues such as typos. (If it is not easy to write this one-pager, check you are as sure as you think you are that the paper is not suitable for a more in-depth review.) In this scenario where a paper is clearly not going to be suitable for the journal, a quick review is a blessing to all involved--and you shouldn't worry about the editor disagreeing as they always have the option to send it out to another reviewer if they disagree with you.

### Writing the referee report

You should only reach this point if the paper warrants a more in-depth review. Alongside the referee report, there will be a cover letter to the editor, which we will come to later.

### General pointers

As a reminder, the goal is to help the editor decide what to do with the paper, and to help the authors create the best paper possible. The way to do achieve both of these is using arguments based only on science and evidence that also explain your assessment of the importance of the work.

Do not make your recommendation of whether to publish, ask for a revision, or reject the paper in the referee report: this decision is for the editors and it's unhelpful for it to go to the authors (instead, put it in your cover letter to the editor). You should ensure that your cover letter and your report are consistent though!

A referee report is not a mind dump. Every sentence in your referee report should be either a factual statement about what the author proposes can be learned from their research, a factual statement of what the reviewer thinks can actually be learned from the paper, or an argument, supported by evidence, about why something can or cannot be learned from the paper.

It's best to be polite, honest, concise, and constructive. Most referee reports are still anonymous, but a good piece of advice is to referee papers *as if* your name was going to be published alongside the report: you should only write what you'd stand by.

Relatedly, your review is of the paper--not of the authors! Address your comments to the paper and the research, avoiding referring to the authors.

In assessing the quality of a paper at a high level, the questions we've seen already are very helpful. If the answer is 'no' to some of the *key* questions, those like 'do you have a good idea what the authors are doing?' and 'would you have been pleased to have written this paper'?, that is a bad sign. You shouldn't have to really strain to understand what's going on in a paper--it's the job of the authors to write it well and sell it.

There are usually three critical determinants of whether a paper is publishable in the journal for which you are reviewing (and which you will have to address):

1. whether it addresses a question of sufficiently broad interest;
2. whether it makes a sufficient leap over existing literature; and
3. whether the analysis is correct.

We recommend that you do not dismiss papers that attack larger issues merely because flaws can be found. The important question that you need to assess is whether the flaws invalidate the contribution. If the flaws do not rise to this level and you judge the contribution to be important enough to warrant publication, then your review should reflect this. All papers have flaws, and no amount of revision will removes all of the potential problems; there is always a need for further research. Try to ask yourself the following question: even given the flaws, would I have been pleased to have written such a paper? If yes, that gives a strong hint that it should be strongly considered for publication, warts and all.

When it comes to empirical papers, you should be skeptical of a conclusion that has a low prior probability--more evidence needs to be brought to bear, and greater validation of the evidence is required, to be persuasive.
