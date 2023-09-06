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
(craft-referee)=
# Writing Referee Reports

In this chapter, you'll learn tips and tricks for writing referee reports. Much of this chapter is advisory: some of it might work for you, some of it might not. It's not intended to be a foolproof guide, or to cover everyone's preferences--but it is designed to help you get started on writing good referee reports.

What is the purpose of a referee report? We think there are two:

1. to help the editor make a decision about whether to publish the paper in their journal
2. to help the authors improve the paper

At first glance, it may seem like 1 is the most important: after all, it's the editor who has asked your opinion. And indeed it's good to do 1 effectively. But why do we have journals, and editors, and the selection of papers, at all? It's to establish scholarly truth and increase the sum total of knowledge of the world. Regardless of whether or not this particular paper gets published in this journal is, in the grand scheme of things, just not that important--what matters is that the paper makes the biggest scholarly contribution it can. So, in the long run, it is 2 that is far more important. Happily, these two objectives are mostly aligned and a good referee report will do both—and without taking up too much of your time.

## Deciding whether to accept a request to referee a paper

In general, your prior for refereeing should be to accept the request unless you have a good reason not to. Reviewing is, to state the obvious, an essential part of the peer review system. As well as greasing the wheels of the evolution of knowledge, reviewing will inevitably help you to become better at writing papers too: once you start seeing the mistakes other authors make, you will take extra efforts to avoid them yourself.

The first question to ask yourself is whether you have sufficient expertise to provide a good review of the paper. Of course, there's a reason why the editor chose to send the paper to you, and they will likely have factored in your expertise when making the decision. But if you feel that you cannot usefully comment on the manuscript or the overall contribution to the field, it may be best to ask the editor what they expect your role to be. If your expertise allows you to comment on some key sections of the paper, you can offer to review these areas and let the editor know you cannot comment on the aspects outside your expertise. In marginal cases, verifying the role the editor is expecting you to play can be helpful--and you may pass up a paper entirely in the rare case that the editor decides you cannot usefully comment.

The second question you should ask yourself is whether you can provide a fair and ethical review! You should notify the editor if you are working on a paper with significant overlap to the one you have been assigned to review. The same goes for if you have a conflict of interest too: maybe you are so close to the authors that you feel you cannot provide a fair and unbiased review, or perhaps you would be unduly negative! If you have worked in the same department, were supervised by, or supervised, one of the authors, or if you are a co-author on another paper, then you're probably too close. In all of these cases, your first act should be to write to the editor to explain the connection.

Finally, you need to ask yourself whether you have the time to review the paper. The timing of reviewing and returning papers can determine entire careers, unfortunately, so sitting on a paper that you optimistically accepted, but cannot now find the time, to review is unhelpful to everyone.

## Reviewing a paper

### Reading the paper

Our advice is that you begin by reading a paper all the way through first, resisting the temptation to make notes on the opening pass. In your head, use the first reading to form an initial assessment of the question, approaches, and conclusions: and whether the paper is publishable in principle based on its contribution to the field. The first reading should help you answer questions like, "What is the main question addressed by the research? Is this question pertinent to the field of study? Do the results of the research contribute substantively to the question? Is this a worthwhile topic?".

On your second read-through, you will likely want to start to dig into details, annotating and highlighting as you go. As you read, you will want to answer questions in the following categories:

- The topic and contribution
  - Do you have a good idea what the authors are doing?
  - Is the topic clearly explained?
  - Does the author do a good job of motivating the question in the introduction?
  - Is the answer to the question obvious in advance?
  - Is the question original?
  - What is the marginal contribution of the paper?
  - Does the author pose a question of reasonable scope (i.e., can he or she reasonably hope to answer the question in a short empirical paper)?
  - Does the author use causal language to describe a finding that is a correlation, or confuse cause and effect in other ways?
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
  - Is the issue of the robustness of the results addressed?
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

At this stage, you can reflect on what you've found so far and evaluate *whether the paper is publishable in principle*: if so, continue with the review (detailed below); if not, for example if the paper is flawed in a way that clearly cannot be fixed and which you believe renders it categorically unsuitable for publication in the target journal or is very below the bar of the journal in terms of contribution to the literature, you can write up a short review. This must set out clearly, and with evidence, why the paper is unsuitable. Even in this case, you should be polite and constructive, and help the authors understand what the main issue is--but don't waste space on minor issues such as typos. (If it is not easy to write this one-pager, check you are as sure as you think you are that the paper is not suitable for a more in-depth review.) In this scenario, where a paper is clearly not going to be suitable for the journal, a quick review is a blessing to all involved--and you shouldn't worry about the editor disagreeing as they always have the option to send it out to another reviewer if they wish to.

### An in-depth review

You should only reach this point if the paper warrants a more in-depth review. Your role now will be to write a referee report and a letter to the editor: we'll look at both.

#### General pointers

As a reminder, the goal here is to help the editor decide what to do with the paper, and to help the authors create the best paper possible. These are best achieved by using arguments based only on science and evidence that also explain your assessment of the importance of the work.

There are usually three critical determinants of whether a paper is publishable in the journal for which you are reviewing:

1. whether it addresses a question of sufficiently broad interest (absolute contribution);
2. whether it makes a sufficient leap over existing literature (marginal contribution); and
3. whether the analysis is correct.

In assessing the quality of a paper at a high level, the questions we've seen already are very helpful. If the answer is 'no' to some of the *key* questions, those like 'do you have a good idea what the authors are doing?' and 'would you have been pleased to have written this paper'?, that is a bad sign. You shouldn't have to really strain to understand what's going on in a paper--it's the job of the authors to write it well and sell it.

However, we recommend that you do not dismiss papers that attack larger or more complex issues merely because flaws can be found or they do not solve everything. The important question that you need to assess is whether the flaws invalidate the contribution or whether the *marginal contribution* is insufficient. If this is not the case, and you judge the contribution to be important enough to warrant publication, then your review should reflect this. All papers have flaws, and no amount of revision will remove all of them, so don't expect perfection. Try to ask yourself the following question: even given the flaws, would I have been pleased to have written such a paper? If your answer is yes, that gives a strong hint that it should be considered for publication, warts and all.

When you are giving feedback on the paper, take a developmental approach. Your job is to improve science by identifying problems and suggesting ways to repair them. Work with the authors to improve the paper in such a way that it benefits collective scholarship.

Throughout your report (and your letter), it's best to be polite, honest, concise, and constructive. Most referee reports are still anonymous, but a good piece of advice is to referee papers *as if* your name was going to be published alongside the report: you should only write what you'd stand by.

Typically, a constructive comment is one that can actually be addressed, ie your advice should be actionable. But constructive criticism does not have to involve specifying a *solution*: it can be much more useful--and easier for you--to be specific about the *problem* and to let the authors identify the solution (ie you don't need to "solutionise").

Of course, there are times when this doesn't apply—for example, if you can think of more or better motivations for their work, you should share these to help the authors improve the paper.

When it comes to empirical papers, you should be more skeptical of a conclusion that has a low prior probability--more evidence needs to be brought to bear, and greater validation of the evidence is required, to be persuasive.

On concision, a referee report is not a mind dump. Every sentence in your referee report should be either a factual statement about what the author proposes can be learned from their research, a factual statement of what the reviewer thinks can actually be learned from the paper, or an argument, supported by evidence, about why something can or cannot be learned from the paper.

Relatedly, your review is of the paper--not of the authors! Address your comments to the paper and the research, and avoid referring to the authors. It's actually best not to look up anything about the authors either—your focus should only be on the arguments in the paper.

When making direct requests of authors, weigh the costs of the request. It is not enough that a particular request will improve the paper. The benefits must exceed the costs, so that the improvement has positive value. Since the author bears the costs, it is easy for you as a referee to make absurd demands thoughtlessly. But you should try and judge what is proportionate.

Similarly, you are not co-authoring the paper, and you shouldn't push the authors to write the paper you would have written.

Some referees, particularly younger ones, may feel that they need to be comprehensive (comment on everything) or be overly negative about a paper because, perhaps subconsciously, they feel a need to prove themselves or have difficulty judging at what level to address comments. This isn't very helpful: papers will always have weaker points, and if we argue endlessly over every minute detail, fields will be stuck in treacle. One way to help yourself avoid this signal-jamming is dividing comments into two sections: one that covers points that must be addressed in order for the paper to be publishable, and one that covers suggestions that would improve the paper but are not necessary for publication. Be really clear about which is which. We'll cover more on this later.

It's sad that we have to write this, but it's bad form to coerce authors into citing your own work (not to mention that empty citations are hardly real impact). You can encourage them to consult work that is truly germane to their work that they might have overlooked though.

Finally, a mistake some people make with writing their referee report is to put their assessment of whether the paper should be published *in* the referee report. It's best not to put a recommendation to publish, revise, or reject the paper in the referee report: this decision is for the editor, and it can make the editor's life more difficult if your own assessment goes to the authors. You can, however, put your recommendation in the letter to the editor, as we'll come to later. Note, though, that the report and letter should be consistent: it's very unhelpful for the editor if you send the authors a glowing referee report and recommend a rejection in your letter!

#### Structure

We recommend that you divide your report into three sections: summary, essential, and suggested.

Having essential and suggested sections helps clearly demarcate major issues, such as not discussing alternative explanations, from minor issues, such as typos, that could easily be fixed for publication. Splitting also helps you avoid one of the most common issues referees have: that they are not clear enough on what is essential and what is not. (Though of course the editor may put their own spin on this.)

You should number every separable element of advice in essential points and suggestions: it is beyond helpful for everyone involved, and it only becomes more valuable if there's a resubmission. We suggest separate numbering for your "essential" and "suggestions" sections.

Overly long referee reports are a burden on everyone. Unless a referee needs to make extremely technical points, 2-3 pages is probably enough.

Let's now look in more detail at each section.

##### Summary

This section helps ensure everyone is on the same page and has understood the purpose of the paper and its context in the wider literature. Start it with a brief overview of the paper, including a few sentences on the hypothesis, key results, and conclusions. Don't just paraphrase the abstract, though; put it in your own words. Sometimes your summary will differ from the one in the paper in important ways. If you're struggling to produce a summary then the paper may not be clear enough.

Follow the overview by your assessment of the contribution of the paper. You can use the questions you asked yourself about it earlier, but the point is to convey whether the topic under consideration is interesting and important (absolute contribution) and whether the work has moved that topic forward (marginal contribution). For example, does the paper present a case study of a known phenomenon in a new system (an incremental advance), present a methodological or technical advance, or change thinking in the field (a more fundamental advance)? You might find the chapter on writing papers, {ref}`craft-writing-papers`, helpful to look at for this.

##### Essential

In this section, you should number each of the points you raise.

If you are recommending a revise & resubmit in your cover letter (or are close to the fence), you should explain what is necessary to meet the bar in this section (even though you shouldn't tell the authors what your recommendation is). The more precise you are about the essential issues, the better. The list of *critical* revisions should generally include no more than three items, and preferably fewer. If more critical revisions are required, the paper should probably be rejected. If you are in fact recommending rejection, this section can be used to explain the fundamental problems. Here you should also state if (and how) the paper can be made shorter. Which results should be prioritised, and which should be cut? Can the paper be made more succinct? The report should suggest only those extensions that are essential for the paper at hand—any additional request can lead the paper to become bloated, as authors feel the need to both investigate to the letter and put it the fruits of their investigation into the paper. In general, it's best to avoid asking for extra material to be added in appendices, including those that are supplementary and online.

Examples of points that might land in "essential" include when there are fundamental concerns about the data, where there are problems with the reasoning, or where the applied methods are inappropriate. You should be clear about the seriousness of the concern, and why it's a problem (without solutionising). If it is impossible to address an essential point, well, then you should recommend rejection in your letter.

Your essential points should only suggest additional analyses or testing when the conclusions of the study would otherwise be undermined. Though, as with the report overall, you should be clear about the difference between what is essential and what is suggested.

There is a higher burden of evidence on you as the reviewer for an "essential" point. You need to rigorously justify why the issue you've raised threatens the contribution of the paper. A referee is obligated to provide a scientific argument for why a perceived problem renders the paper unpublishable, and that argument must be understandable to both the editor and the authors.

Be wary: what you don't want to do here is omit a point now that later turns out to be, well, essential—this becomes especially tricky after a revise and resubmit. So it's important that your essential requirements are as refined as you can make them in the first round. This also helps the editor provide a roadmap to publication if they do decide to issue a revise and resubmit for the paper.

##### Suggestions

These are all of your other comments. Not every issue you notice will threaten the overall contribution of the paper—in fact, most of them won't—but this is an opportunity for you to help the paper be as good as possible. So this is less critical, but usually a lot bigger, than the "essential" section: a rough guide is that the suggestions will make up 70% of the text that you send in the report.

Examples of suggestions might be things that improve the clarity of the paper, additional relevant citations, further details of the method, a more accurate paper title, recommendations for clearer figures, and fixes for typos.

While it is important to include suggestions because they are a key part of your two goals of helping the editor and helping the paper be the best it can be, an overly long list of suggestions can become burdensome for all involved, so keep the whole thing at 2-3 pages at most. And a long "suggestions" section definitely shouldn't come at the expense of a timely referee report.

#### The letter to the editor

This is where you will give advice to the editor, rather than to the paper (via the authors). Remember, it's the *editor* who takes the accept/revise/reject decision, not you, so what's in this letter is just advice—but what you say will be taken very seriously. As noted, it should be consistent with the report.

A brief cover letter is a good cover letter. You should be looking to succinctly provide four types of information:

- any extra colour on the broad interest and importance of the work relative to the existing body of knowledge (that isn't already in the report--there's no point rehashing what's in the report, because the editor has that too);
- any concerns, including ethical concerns, that you felt you could not raise directly in the report (eg experimental design, or if the authors are salami slicing results);
- your frank assessment as to whether the paper is publishable, is likely to be publishable within one round of revision, or is unpublishable; and
- in a concise format, the reasoning behind your recommendation.

Regarding the extra information on the broad interest and importance of the work, the editor needs to know the positives and negatives of the paper, and, inevitably, you will have spent more time discussing the negatives in your report. So the cover letter is often a good place to talk more about the positives of the paper and how it moves the field forward.

Note that when you recommend a revise-and-resubmit, what you are really saying is:

- the paper is of sufficient importance and interest to be published in the journal;
- there are problems with the paper that make it unpublishable in its current form; and
- these problems are correctable.

In short, you are helping the editor provide a road map to publication of the work; and, if the authors address these requests, then the editor will likely accept the paper.

## Refereeing a revise and resubmit

This section covers what to do if you are asked to review a revised paper (following a revise-and-resubmit), having provided essential points in a first round of review.

A revise and resubmit is an implicit contract between the authors of the paper and the reviewers of the paper. The deal is that if the author satisfactorily addresses the essential issues that you have raised, you will recommend publication. This means that you shouldn't make new essential demands in the second round that you have not made before (it's okay to make suggestions but be extra clear that that is what they are).

If the authors have revised their paper, check whether your suggestions have been implemented or if sufficient arguments have been brought to bear to mitigate your "essential" concerns from the previous round. And, if the authors have appropriately satisfied the key requests of a previous round of review that resulted in a revise-and-resubmit, the paper should then be accepted!
