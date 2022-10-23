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
(wrkflow-version-control)=
# Version Control

In this chapter, you're going to learn about version control. This will enable you to keep track of any code you write, down to the lin, following best software development practices. It can be a challenging topic as it requires a different mindset to the one you're probably used to where you just save a file. But I promise you that it's worth it---and it will really help you ensure that your analysis is reproducible, and easily packaged up into a replication packet.

This chapter has benefitted from a wide range of sources, including [Research Software Engineering with Python](https://merely-useful.tech/py-rse/), the free online book [Pro Git](https://git-scm.com/book/en/v2), and the Alan Turing Institute's [Research Software Engineering with Python](https://alan-turing-institute.github.io/).

## What is version control?

Version control means keep tracking of the versions of the assets (code, data, models) that you are working with to produce analysis. In this chapter, we'll mainly be looking at version control for code (and text such as latex), but if you're working with data or models that are changing a lot, there are technologies for version control of data and models (for example, [DVC](https://dvc.org/) and [pachyderm](https://www.pachyderm.com/)) too.

When coders talk about version control though, they're usually referring to the ability records changes to a file or set of files over time. Furthermore, they're usually talking about a specific technology for version control---a programme called git, that we'll see more of later in the chapter.

You should also know right up front that there's a distinction between git---the tool that can do version control, and GitHub---a central repository that can save the record of your version history on the cloud.

Version control as we'll see it in this chapter works at the project-folder level, keeping everything you need for one project in one structure called a *repository*.

One of the most important things to get your head around with version control is that it offers **much more** than Dropbox or Google Drive. Those do not offer you:

- comments, commit messages, issues, or labels
- a complete version history
- the ability to compare any version with any other version
- the ability to "branch"
- the ability to resolve merge conflicts

We'll find out more about these abilities later in the chapter.

Version control *doesn't* do some things that Dropbox and Google Drive do though: it doesn't automatically save your files, or even sync them, automatically; you have to manually say when you wish to lodge a more recent version of a file.

The point about reproducibility applies to future you (if your computer gets busted), to your co-authors (who can "clone" your repository), and perhaps even to the world at large (if you open source your code). By putting your repository under version control at the project-folder level, you make it *much* easier for others to work with it and make changes. (As an example of this, the guidelines for contributing to "Coding for Economists" can be found [here](https://github.com/aeturrell/coding-for-economists#dev).)

Finally, version control is the de facto standard for managing code. It's a very important part of coding, so if you can learn even a little bit, it's well worth it

### Why do you need version control?

There are plenty of benefits to using version control. Ultimately it will allow you to be a better analyst, researcher, and economist because your work will be better recorded, more reproducible, and easier to expand.

Version control solves lots of problems in research. Ever had a file called "final_final_v3.doc"? Yeah, I bet you have.

![PhD Comics "Final".doc](https://phdcomics.com/comics/archive/phd101212s.gif)

Version control aims to remove the problems associated with trying to have an individual track all the different versions. It gets even worse when multiple people are involved, emailing around spreadsheets or code with the same file names but different contents.

Version control gives you many benefits and abilities:
- save changes that you've made to code, text files (eg latex files), and to small amounts of data;
- access a complete organised revision history of your work;
- revert selected files back to a previous state;
- revert the entire project back to a previous state;
- compare changes over time;
- go back and forth between many different versions of the same file;
- safely experiment with changing things (on a different *branch*)
- concurrently collaborate on the same code base with others;
- merge changes from multiple authors together;
- see who last modified something that might be causing a problem down to the individual line and time it was added; and
- much more.

Modern version control systems let you easily answer questions like who wrote this line and when? They also let you attach a message to every change you make. This feature is particularly useful when revising papers; you can have a commit per referee comment that you deal with and know *exactly* what you changed in the code and paper for it.

Of course, your git commit messages do need to be informative...

![XKCD comic 1296](https://imgs.xkcd.com/comics/git_commit.png)

You may wonder who uses version control. It's researchers, software developrs, analysts, data scientists; anyone who has plain text files that they need to track.

There are some files you *wouldn't* or shouldn't put under version control:

- passwords and other files with secrets in
- larger data files
- binary (non-text) files
- 

### Git, the most popular version control tool

By far the most popular technology for version control of plain text files (which includes code, latex, notebooks, and markdown) is *git*. Git is a system for lodging changes, tracking them, and backing them up to a central repository. It is the industry standard and ubiquitous for coding.

Once you've installed it (which we'll come to), git is a programme that is available on your computer's console (aka the command line, covered in {ref}`wrkflow-command-line`). Some people use it directly from the command line, but there are also good Graphical User Interfaces (GUIs) around for it, including [Visual Studio Code](https://code.visualstudio.com/), which this book recommends for coding.

Git is a *distributed version control system*. This means that the complete codebase, including its full history, is mirrored on every developer's computer (including the central repository).

It's fair to say that git has a steep learning curve, as immortalised by the below XKCD comic.

![XKCD comic 1597](https://imgs.xkcd.com/comics/git.png)

There are two main ways to use git:

- The command line.[^a]
- A graphical user interface, eg Visual Studio Code

[^a]: Some 'shells' that provide a command line, like Oh My Zsh---which this book recommends, come with git integration and will show information about the repository of the current folder.

In this chapter, we'll try to equip you with:

1. a knowledge of the basics, enough to use git productively; and
2. how to use git on the command line and with a GUI.

## Version control with git

Let's get started with version control. 

### Installing git

If you're working through this book on Google Colab, Github Codespaces, or other prepared systems, then you're likely to find that git is already installed. You can check this by running

```bash
git --version
```

on the command line.

```{admonition} Tip
If you are using a Jupyter Notebook, or other notebook environment like Google Colab, you can access the command line in a cell by pre-fixing the command with an exclamation mark, eg `!git --version`
```

If you need to install git, head over to the [git website](https://git-scm.com/) and download the version for your operating system then follow the install instructions. Again, once installed, you can check it's worked by opening up the command line in Visual Studio Code ("Terminal" -> "New Terminal") and typing `git --version`.

### Configuring git

The first thing you'll want to do with git is configure it so that you are recognised as you when you track a change. You can do this via the following commands:

```bash
git config --global user.name "YOUR NAME HERE"
git config --global user.email "yourname@example.com"
```

You can check this worked by running the following in your command line:

```{code-cell} ipython3
%%bash
git config --get user.name
```

You can check other settings with `git config --list`.

### How git works locally

Git works at a project-folder level. This should be the root folder (aka the *working directory*) for your project. In git terminology, this folder is called a *repository*.

Git works by creating a hidden folder within your project folder, or repository, called `.git`. Inside this folder, the changes to your repository are tracked.

The typical workflow for git done locally involves three stages:

1. checking out the repository (for example, by pulling it down from the internet). The command is `git clone url-of-repository-name`. Alternatively, creating a new repository using `git init repository-name`.
2. add changes to the staging area using `git add file-name` for any files you wish to track.
3. use `git commit -m 'commit message'` to commit the changes to version control.

![Diagram showing the three different stages involved in version control with git.](https://git-scm.com/book/en/v2/images/areas.png)

*The three different stages involved in local version control*

## Using git for version control on the command line: a walk through

### Creating a new repository

Okay, open up a folder on your computer and your favourite command line tool.

Create a new folder called "test-repo", and move into it on the command line:

```bash
mkdir test-repo
cd test-repo
```

To create a new repository (inside "test-repo"), hit

```bash
git init --initial-branch=main
```

Now, to check it's all worked run

```bash
git status
```

```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Adding files

Let's now put a file under tracking by version control.

First we need a file to track! We'll create a markdown file that you often find in a code repository, `README.md`. This tells others (and future you) about what's in the project and how to use the code in it. (For an example, look at the `README.md` of the [skimpy package](https://github.com/aeturrell/skimpy#skimpy).) We can create this file on the command line.

```bash
echo "# my test repo" > README.md
```

You can check this has worked by looking at the file in the file explorer, or by running `ls -lah` (which shows files including hidden files) on the command line:

```bash
ls -lah
```

```text
Permissions Size User          Date Modified Name
drwxr-xr-x     - username 23 Oct 17:35  .git
.rw-r--r--    15 username 23 Oct 17:43  README.md
```

So, we've created a file but it's not yet being tracked by version control: for that, we need to add it.

```bash
git add README.md
```

Running `git status` now shows

```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

This means we have "staged" the file, but not committed it.

By the way, you can stage lots of files at once. For example, you can add all files in the directory with `git add .`, though this may not be a good idea: there are some files you may not want to track because they are very large.

So we have staged, but not committed, our new file. Let's now commit it, with a suitable message.

```bash
git commit -m "Add readme; first commit"
```

```text
[main (root-commit) 0dc5442] Add readme; first commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

`git commit` takes everything that was staged using `git add` and stores a copy permanently inside the repository's .git directory. This permanent copy is called a commit or a revision. Git gives it a unique identifier, and the first line of output from git commit displays its short identifier 0dc5442, which is the first few characters of that unique label.

The diagram below gives a flavour of the process we're going through here.

![Diagram of how assets become tracked, from Research Software Engineering in Python.](https://merely-useful.tech/py-rse/figures/git-cmdline/staging-area.png)

### Reviewing changes

We can now look at the git log to see all of the changes we made:

```bash
git log
```

```text
commit 0dc54420a7d606c643f9a254939f82a2dc8df968 (HEAD -> main)
Author: USERNAME
Date:   Sun Oct 23 18:02:09 2022 +0100

    Add readme; first commit
```

Now if you run `git status`, you'll see a message saying that there's nothing to commit (because every tracked file has no new changes since the last commit).

There's some really nice features for looking at what's been committed, even at the command line. For example, here's an excerpt (simplified) from running `git log --graph` on the "Coding for Economists" git repository:

```text
*   commit 2f89dd3517dad054f57bdabda693e370da21cb36
|\  Merge: f1d132c 4c4aa29
| | 
| | Date:   Sat Aug 20 23:50:48 2022 +0100
| | 
| |     Merge pull request #24 from aeturrell/pyfords_improvemnets
| |     
| |     Pyfords improvemnets
| | 
| * commit 4c4aa29398fd4724e8e3c2a0b53a6378ef7b1bd4
| | 
| | Date:   Sat Aug 20 23:50:11 2022 +0100
| | 
| |     major update structure
| | 
| * commit e46e6e46e40b1bd4c59ae035bc9348f99064be77
| | 
| | Date:   Sat Aug 20 14:06:52 2022 +0100
| | 
| |     basic content re-org
| | 
| * commit c2fa840e60791f47f202e43f6acac7f88ad85364
| | 
| | Date:   Tue Aug 16 10:35:52 2022 +0100
| | 
| |     cutting back content in data-advanced
| | 
| * commit fbb69a342a61a1ebc374b7c04a650bd7766839fd
|/  
|   Date:   Tue Aug 9 21:43:15 2022 +0100
|   
|       python4ds additions / changes 1st round
```

You can see it's not a single straight line; that's because two branches of the code co-existed and were merged at some point.

#### Looking at differences

Let's now make another change and add a simple Python script:

```bash
echo "print('hello world')" > script.py
```

Now we'll do:

1. `git add script.py`
2. `git commit -m 'python script to print out hello world'`

To track our new script file.

Say you made a mistake: you really wanted the script to say `print('hello world!')`, with an exclamation mark. But you want to track this change. Use a text editor to make the change to an exclamation mark but don't stage the file.

Now run

```bash
git diff
```

```text
diff --git a/script.py b/script.py
index 75d9766..0ab9637 100644
--- a/script.py
+++ b/script.py
@@ -1 +1 @@
-print('hello world')
+print('hello world!')
```

Here "diff" is short for difference and allows you to review exactly what changed between the previous commit and the unstaged files.

Let's stage this change, `git add script.py`, and commit it, `git commit -m 'adding exclamation mark to printed message'`.

We'll now use `git diff` again but to compare two historic commits against each other. We can use the shorthand for two commits in the form of their first few digits

```bash
git diff 46fe57 d0f60e3
```

(If you're following along, you'll need to change these codes to the ones that your computer generates.) What you should see is the same output before with minus signs and plus signs showing the differences.

You can also use `git diff HEAD HEAD~1` to look at the differences between the two most recent commits.

#### Reverting to a previous commit

Let's say we decided we *didn't* actually want an exclamation mark in our script! Now, in this simple case, you'd probably just be tempted to edit the file directly, but what if it's more complex than that and you have many lines that changed?

git gives you a way of restoring files from a particular commit. This command is called `git checkout`. Let's use it to revert our script to the version without the exclamation mark. The last pre-exclamation mark commit was d0f60e3, so we'll use that:

```bash
git checkout d0f60e3 script.py
```

Now, running `cat script.py` yields

```python
print('hello world')
```

You will need to commit this reversion if you want to keep it though (it's automatically staged).

Now, if you want to temporarily go back to a previous commit, fool around, then come back to where you are later, all you have to do is check out the desired commit:

```bash
git checkout d0f60e3
```

To go back to your latest commit, it's

```bash
git checkout main
```

(Or whatever branch you were on, we're assuming here it was the "main" branch.)

However, if you want to make commits while you've temporarily got an old version checked out, you will need to make a new branch (we haven't seen branching yet, so this is a preview):

```bash
git checkout -b old-state d0f60e3
```

The new branch will have the name "old-state".

#### What's in a commit?

You may wonder when to make your commits; how much work should you do between commits? Usually, a single commit reflects a discrete task: a collection of changes, possibly over multiple files, that achieve one change. A good guide is that you should be able to fit the information about your commit into the (fairly short) commit message.

#### Summary of the git workflow

So let's summarise the git workflow after you've created your repository.

1. Do work in your project directory
2. Add changes you want to preserve to your staging area using `git add`
3. commit a snapshot of those changes, `git commit -m 'commit message'`
4. If you have a remote repository, push your commit to the remote repository (we haven't seen this yet); `git push`

#### Tracking what commands you've used

Given all the possible options to move around your commits, it can be useful to see what you've done in the past! That's where the `git reflog` command comes in. Here it is as applied to the `test-repo` that was set up above.

```bash
git reflog
```

```text
46fe574 (HEAD -> main) HEAD@{0}: checkout: moving from d0f60e3f3b55f20f16e27c55e620a72c2d4308ca to main
d0f60e3 HEAD@{1}: checkout: moving from main to d0f60e3
46fe574 (HEAD -> main) HEAD@{2}: commit: adding exclamation mark to printed message
d0f60e3 HEAD@{3}: commit: python script to print out hello world
0dc5442 HEAD@{4}: commit (initial): Add readme; first commit
```

### Other files you may want to include under version control

As well as your project files, there are some really useful files you can put under version control:

- `.gitignore`, which tells git *not* to track certain files (eg large data files; more on this below)
- a `LICENSE`, which tells others under what terms they can use your code. This book uses the permissive [MIT License](https://github.com/aeturrell/coding-for-economists/blob/main/LICENSE).
- a `README.md`, which, as noted, explains what's in the repository and may have instructions on how to use the code in it. If you need a reminder on how to write an `.md`, or markdown, file, look back at {ref}`wrkflow-markdown`.

#### .gitignore

A .gitignore file tells git what to ignore.

This is especially useful if you want to exclude whole folders or a class of files. For example, any proprietary data files should be ignored from the beginning if you intend to make a repo public at some point.

You should ignore any very large individual files (>100 MB) as these exceed GitHub's maximum allowable size. Generally, it's a good idea not to use version control with git for data unless those data are very small and in plain text, though people (including the authors of this book), frequently break this rule a bit.

Then there are files that are associated with the code having run, but which aren't actually necessary for the code *to* run. There's no point tracking these. As examples, the `.gitignore` file for this book contains some entries like:

- `_build/*`, which says to ignore any (this is what `*` does) file in the `_build` directory
- `coverage.xml`, which is an automatically generated file that tracks how much of a code base is covered by tests, but which doesn't need to be tracked as part of the project.

You can create a `.gitignore` file by running `touch .gitignore` on the command line and then adding contents with a text editor. Or, if you're using Github to initialise a repository, then it will suggest `.gitignore` files from a big roster of templates.

A typical `.gitignore` file for a Python project, that excludes some files that get generated when Python runs but don't contain the code from your scripts, can be found [here](https://github.com/github/gitignore/blob/main/Python.gitignore). This is what Github will offer if you choose their Python template.

These are the rules for ignoring files; they should be written on different lines in the `.gitignore` file:

- To ignore a single a file: `FILE-I-WANT-TO-IGNORE.csv`
- To ignore a whole folder (and all of its contents, subfolders, etc.): `FOLDER-NAME/**`
- The standard shell commands and special characters apply:
  * Ignore all CSV files in the repo: `*.csv`
  * Ignore all files beginning with "test": `test*`
  * Don't ignore a  particular file: `!somefile.txt`

One trick we recommend is, if you want to keep a folder but not its contents, add these two lines:

```text
foldername/*
!foldername/.gitkeep
```

and run `touch foldername/.gitkeep`. This preserves the structure but doesn't track anything in the folder---highly useful for folders containing data.

## Remote and local

![](https://merely-useful.tech/py-rse/figures/git-cmdline/git-remote.png)

### GitHub

