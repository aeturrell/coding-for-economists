(code-preliminaries)=
# Preliminaries

Congratulations on starting your coding for economics journey! In this chapter, we're going to help you install or access the tools you need. This chapter is unlikely to be as fun as subsequent ones, but we recommend that you read and follow it because it's key to being able to run code. First, we're going to give you some background on key concepts for coding. Then, we'll give you an option to either follow instructions to start coding on your own computer or use a popular online cloud service for coding. Either way, by the end of this chapter, you will be running code!

## Choice of programming language for the book

This book uses Python, which is usually ranked as the first or second most popular programming language in the world and, just as importantly, it's also one of the easiest to learn. It's a general purpose language, which means it can perform a wide range of tasks. This combination of features is why people say Python has a "low floor and high ceiling". It's also very versatile; the joke goes that Python is the 2nd best language at everything, and there's some truth to that (although Python is 1st best at some tasks, like machine learning). But a language that covers such a lot of ground is also very useful; and Python is widely used across industry (eg at Google and Apple), academia, and the public sector, and is often taught in school computer science classes too. It is used for everything from computer games to websites, from data science to [flying a helicopter on Mars](https://github.com/nasa/fprime). And, of course, it's behind innovations like large language models too!

As an economist, you will know that this means Python benefits from strong positive network externalities. As such, learning Python has a lot of value and, once you have, learning more specialised languages like C++ or R is much easier; many of the basic programming concepts you'll see in this book are useful in almost any programming language. One other benefit of Python if you plan to do any work on the cloud is that it is extremely well supported.

![xkcd-python](https://imgs.xkcd.com/comics/python.png)

*Python*, from [xkcd](https://xkcd.com).

Different languages have different strengths and weaknesses; Python's strengths are being easy to write; having depth and flexibility; being ubiquitous; and having an amazing line-up of packages for doing just about anything in analysis, plus tons of other fields too. You may hear that Python is slow; and indeed it is compared to compiled languages like C++, Fortran, or Rust, but the trade-off we make here is that Python is *far* easier to write, and is "dynamic", meaning we can see results right away. For analysis, this trade-off is a no-brainer, and you will rarely run into speed issues (and, when you do, it will likely be solvable with structuring the code differently). I think Python's two greatest weaknesses currently are actually that there are too many different ways to manage packages, and that there are too many different ways to install it.

Overall, Python is a brilliant language to code in, especially for analysis, data science, and economics, and it's no wonder that it's one of the world's most popular languages!

## Concepts

In this section, we're going to help you understand the key elements of a computational environment for coding. The combination of the version of the language you're using (eg Python 3.10), the packages (add-ons to the language) and their versions (eg pandas 2.1.0), and the operating system the code is being run on (eg MacOS Catalina) is called the computational environment. So, to create a computational environment to run code, you'll need:

- a computer with an *operating system*. This could be your computer or one on the cloud.
- an installation of *Python*, so that the computer can interpret and execute Python code
- an *integrated development environment*, or IDE, a place to write and run code
- *packages*, which extend the functionality of Python in all kinds of useful ways

Let's talk through each of these in a bit more detail.

### Operating System

Almost all the code you'll see can be run on all three of the major operating systems: Windows, MacOS, and Linux, so it doesn't matter much what operating system you're using. Almost all cloud services use Linux.

If you haven't yet decided which operating system to use, this book recommends either Linux or MacOS because, in a very small number of cases, you'll find it easier to run the most advanced code on them rather than on Windows. Don't panic if you have Windows already though—most things will work just fine and it tends to be power users who run into this problem. (If you're not familiar with Linux, it's a free operating system that is also widely used for cloud services and, while it used to have a reputation as being fearsomely difficult for beginners, some modern Linux distributions, such as Ubuntu, are pretty user-friendly.)

If you have Windows and you want to use Linux or Mac but don't want to shell out for a new computer, there are a couple of options. One is to use the [*Windows Subsystem for Linux*](https://pbpython.com/wsl-python.html). It's essentially a Linux operating system that installs alongside and integrates with your existing Windows operating system. This allows you to run code as if you were using Linux. You can get WSL [for free from Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Another option (easier but can be more expensive) is to use an online cloud service, an option we'll return to shortly.

### Python interpreter

Python is both a programming language that humans can read, and a language that computers can read, interpret, and then carry out instructions based on. For a computer to be able to read and execute Python code, it needs to have a Python interpreter installed. There are lots of ways to install a Python "interpreter" on your own computer, this book recommends the Anaconda distribution of Python for its flexibility, simplicity, and large community. Cloud services often come with a Python interpreter installed, and we'll see shortly how to install one on your own computer.

### An Integrated Development Environment, or IDE

An integrated development environment (IDE) is a software application that provides a few tools to make coding easier. The most important of these is a way to write the code itself! IDEs are not the only way to programme, but they are perhaps the most useful. If you have used **Stata** or **Matlab**, you may not have realised it, but these analytical tools bundle the interpreter and the IDE together. But they are separate things: the interpreter is a way of processing your instructions, the IDE is where you write those instructions.

There are a lot of integrated development environments (IDEs) out there. This book strongly recommends Microsoft's Visual Studio Code, which works on all major operating systems and is one of the most popular. Here are some of the most useful features that Visual Studio Code provides:

- a way to run your code interactively (line-by-line) or all at once
- a way to debug (look for errors) in your code
- a quick way to access helpful information about commonly used software packages
- easy ways to initiate automatic code formatting, so that your code follows best practice guidelines
- auto-completion of your code when you hit <kbd>TAB</kbd>
- automatic code checking for basic errors
- colouring your brackets in pairs so you can keep track of the logical order of execution of your code!

### Packages

A Python package is a collection of functions, data, and documentation that extends the capabilities of an installed version of Python. Using packages is key to most data science because most of the functionality we'll need comes from extra packages. You'll see statements like `import numpy as np` at the start of many Python code scripts—these are instructions to use an installed package (here one called **numpy**) and to give it a shortened name (`np`, for convenience) in the rest of the script. The functions in the **numpy** package are then accessed through syntax like `np.`; for example, you can take logs with `np.log(x)` where `x` is a variable containing a number. You need only install packages once, but you must import them into each script you need to use them in. We'll see more on how to both install and use packages in subsequent chapters.

### Typical workflow

The typical workflow for analysis with code might be something like this:

- Open up your integrated development environment (IDE)
- Write some code in a script (a text file with code in) in your IDE
- If necessary for the analysis that you're doing, install any extra packages
- Use the IDE to send bits of code from the script, or the entire script, to be executed by Python and add-on packages, and to display results
- (once the project is complete) ensure the script can be run from top to bottom to re-produce your analysis

We'll see two ways to achieve this workflow:

1. Installing an IDE, a Python interpreter, and any extra Python packages on your own computer
2. Using a computer in the cloud that you access through your internet browser. Cloud computers often have an IDE and Python built-in, and you can easily install extra packages in them too. However, you should be aware that the cloud service we recommend has a 60 hours / month free tier—beyond this, so you'll need to pay for extra hours.

You should pick whichever you're more comfortable with! Eventually, you'll probably try both.

## How to get started on your own computer

These instructions are for if you've decided to code on your own computer.

### Installing Python

To download and install Python, we'll use the Anaconda "distribution" of Python, which is available on all major operating systems. To install it, follow the instructions below or watch this video on *[how to install Python using the Anaconda distribution of Python](https://www.youtube.com/watch?v=ZWQwGR5ppnk)*.

<iframe width="700" height="394" src="https://www.youtube.com/embed/ZWQwGR5ppnk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Download the individual edition of the [Anaconda distribution](https://www.anaconda.com/) of Python for your operating system and install it. This will provide you with a Python installation and a host of the most useful libraries. If you get stuck, there are more detailed instructions available for installing the Anaconda distribution of Python [on Windows](https://docs.anaconda.com/anaconda/install/windows/), [on Mac](https://docs.anaconda.com/anaconda/install/mac-os/), and [on Linux](https://docs.anaconda.com/anaconda/install/linux/).

You can confirm that you've set up Anaconda correctly by following the [verify installation instructions](https://docs.anaconda.com/free/anaconda/install/verify-install/#conda) on the Anaconda website.

```{note}
If you're using Windows, you can check if Anaconda has installed properly by opening the 'Anaconda prompt' (a special text-based way to issue commands to your computer) and type `where python`. You should see a path rendered as text in the prompt that includes "Anaconda3", for example something like `C:\Users\<your-username>\Anaconda3\...`. On Mac and Linux you may need to run `conda init` on your command line to activate your Anaconda Python environment. You can check you've got the right Python with `which python`, which should result in a message back saying `/Users/<your-username>/opt/anaconda3/bin/python`.
```

### Installing your integrated development environment, Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a free and open source IDE from Microsoft that is available on all major operating systems. Just like Python itself, Visual Studio can be extended with packages, and it is those packages, called extensions in this case, that make it so useful. As well as Python, Visual Studio Code supports a ton of other languages.

Download and install Visual Studio Code. If you need some help, there is a video below that will walk you through downloading and installing Visual Studio Code, and then using it to run Python code in both scripts and in notebooks. We'll go through these instructions in detail in the rest of this chapter.

<iframe width="700" height="394" src="https://www.youtube.com/embed/1kKTYsQdaPw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*[How to install Visual Studio Code and use it to run Python code](https://www.youtube.com/watch?v=1kKTYsQdaPw)*

## Coding in the cloud

These instructions are for if you wish to code in the cloud rather than on your own computer. There are many ways to do data science in the cloud, but we're going to share with you the absolute simplest. For this, you will need to sign up for a [Github Account](https://github.com/). GitHub is an organisation that's owned by Microsoft and which provides a range of services including a way to back-up code on the cloud, and cloud computing. One of the services offered is *Github Codespaces*. A GitHub Codespace is an online cloud computer that you connect to from your browser window. It has a generous 60 hours free of computing per month.

```{note}
If you go over the free tier hours on Github Codespaces, your credit card will be charged for any further hours of GitHub Codespaces you use.
```

Once you've signed up for a Github account, head to [Github Codespaces](https://github.com/codespaces) and click on "Get Started for Free". You should see a menu of "quick start templates". Under where it says "Jupyter Notebook", hit "Use this template".

You will find that a new page loads with several panels in. This is an online version of Visual Studio Code that works much like if you had installed it on your own computer. It will already have a version of Python installed—you can check which one by running `python --version` in the terminal. The terminal is usually found in the lowest panel of Visual Studio Code, and, in Codespaces, will typically display a welcome message.

## Alternative ways to run the code from the book

As well as following this book using your own computer or on the cloud via Github Codespaces, you can run the code online through a few other options. The first is the easiest to get started with.

1. [Google Colab notebooks](https://research.google.com/colaboratory/). Free for most use. You can launch most pages in this book interactively by using the 'Colab' button under the rocket symbol at the top of most pages in this book. It will be in the form of a notebook (which mixes code and text) rather than a script (.py file) but the code you write is the same. Note that Colab doesn't use Visual Studio Code.
2. [Gitpod Workspace](https://www.gitpod.io/). An alternative to Codespaces. This is a remote, cloud-based version of Visual Studio Code with Python installed and will run Python scripts. Note that the free tier covers 50 hours per month.

```{admonition} Exercise
Try going to the {ref}`code-basics` chapter now, click on the rocketship symbol (🚀) and then select "Colab". When the Colab notebook opens, select the first code cell and hit shift + enter to run it.
```

## Running your first Python code

### Getting to grips with Visual Studio Code

Once you have Visual Studio Code installed and opened (either on your own computer or in the cloud), navigate to the 'extensions' tab on the left hand side vertical bar of icons (it's the one that looks like 4 squares). You'll need to install the *Python* extension, which you can search for by using the text box within VS Code's extensions panel. If you're using the cloud version, you may find that it's already installed.

There are some other extensions it's useful to have and install (if they aren't already):

- Jupyter
- Pylance
- indent-rainbow

Although you won't have any Python code to play with yet, or an interactive window to execute that Python code, it's worth us spending a brief moment familiarising ourselves with the different bits of a *typical* view in Visual Studio Code.

![A typical user view in Visual Studio Code](https://github.com/aeturrell/coding-for-economists/blob/main/img/vscode_layout.png?raw=true)

The figure above shows the typical layout of Visual Studio Code once you have a Python session running, and a Python script open. The long vertical panel on the far left-hand side changes what is seen in panels 1 and 2; it currently has the file explorer selected. Let's run through the numbered parts of the figure.

1. When the explorer option is selected from the icons to the left of 1 and 2, the contents of the folder that's currently open are shown in 1.
2. This is an outline of the key parts of the file that is open in 3.
3. This is just a fancy text editor. In the figure above, it's showing a Python script (a file that contains code and has a name that ends in `.py`). Shortly, we'll see how selecting code and pressing <kbd>Shift</kbd> + <kbd>Enter</kbd> ('Enter' is labelled as 'Return' on some keyboards) will execute code whose results appear in panel 5.
4. This is the command line or *terminal*, a place where you can type in commands that your computer will then execute. If you want to try a command, type `date` (Mac/Linux) or `date /t` (Windows). This is where we install extra *packages*.
5. This is the interactive Python window, which is where code and code outputs appear after you select and execute them from a script (see 3). It shows the code that you executed and any outputs from that execution—in the screenshot shown, the code has created a plot. The name and version of Python you're using appear at the top of the interactive window.

Note that there is lots of useful information arrayed right at the bottom of the window in the blue bar, including the version of Python currently being used by VS Code.

### Running Python code

Now you will create and run your first code. If you get stuck, there's a more in-depth tutorial over at the [VS Code documentation](https://code.visualstudio.com/docs/python/python-tutorial).

In Visual Studio Code, click on the "Explorer" symbol (some files on the left-hand side of the screen) to bring up a file explorer. Check you're in a good location on your computer to try things out and, if not, change the folder you're in using File -> Open Folder until you're happy.

Now, still with the explorer panel open, click on the symbol that looks like a blank piece of paper with a "+" sign on it. This will create a new file, and your cursor should move to name it. Name it `hello_world.py`. The file extension, `.py`, is very important as it implicitly tells Visual Studio Code that this is a Python script.

In the Visual Studio Code editor, add a single line to the file:

```python
print('Hello World!')
```

Save the file.

If you named this file with the extension `.py` then VS Code will recognise that it is Python code and you should see the name and version of Python pop up in the bar at the bottom of your VS Code window. (You can have multiple versions of Python installed—if you ever want to change which Python version your code uses, click on the version shown in the bar and select the version you want.)

Alright, shall we actually **run some code**? Select/highlight the `print("Hello world!")` text you typed in the file and right-click. You'll get a lot of options here, but the one you want is **"Run Selection/Line in Interactive Window"**.

This should cause a new 'interactive' panel to appear within Visual Studio Code, and, hey presto you should see:

```python
print("Hello world!")
```
```text
Hello world!
```

The *interactive window* is a convenient and flexible way to run code that you have open in a script or that you type directly into the interactive window code box. The interactive window will 'remember' any variables that have been assigned (for examples, code statements like `x = 5`), whether they came from running some lines in your script or from you typing them in directly. Working with the interactive window will feel familiar to anyone who has used Stata, Matlab, or R. It doesn't require you to write the whole script, start to finish, ahead of time. Instead, you can jam, changing code as you go, (re-)running it line by line.

It would be cumbersome to have to right-click every time we wanted to run some code, so we're going to make a *keyboard shortcut* to send whatever code is highlighted to the interactive window to be executed. To do this:

- Open up the Visual Studio Code configuration menu (the cog on the lower left-hand side)
- Go to Settings
- Type "jupyter send" in the box to make an entry "Interactive Window > Text Editor: Execute Selection" appear
- Ensure the box next to this entry is ticked

Now return to your script, put your cursor on the line with `print("Hello world!")` on, and hit <kbd>Shift</kbd>+<kbd>Enter</kbd>. You should see "Hello world!" appear again, only this time, it was much easier.

```{admonition} Running code in the terminal instead
:class: dropdown

The interactive window isn't the only way to run code; you can do it in the terminal too. This is less popular for data science, but it does occasionally have its uses. If you want to do this, right-click on the selected code and choose "Run Python -> Run Selection/Line in Terminal".
```

Let's make more use of the *interactive window*. At the bottom of it, there is a box that says 'Type code here and press shift-enter to run'. Go ahead and type `print('Hello World!')` directly in there to achieve the same effect as running the line from your script. Also, any variables you run in the interactive window (from your script or directly by entering them in the box) will persist.

To see how variables persist, type `hello_string = 'Hello World!'` into the interactive window's code entry box and hit shift-enter. If you now type `hello_string` and hit shift+enter, you will see the contents of the variable you just created. You can also click the grid symbol at the top of the interactive window (between the stop symbol and the save file symbol); this is the variable explorer and will pop open a panel showing all of the variables you've created in this interactive session. You should see one called `hello_string` of type `str` with a value `Hello World!`.

This shows the two ways of working with the interactive window--running (segments) from a script, or writing code directly in the entry box. It doesn't matter which way you entered variables, they will all be remembered within that session in your interactive window.

```{admonition} Start interactive windows and terminals within your project directory
:class: dropdown
In Visual Studio Code, you can ensure that the interactive window starts in the root directory of your project by setting "Jupyter: Notebook File Root" to `${workspaceFolder}` in the Settings menu. For the integrated command line, change "Terminal › Integrated: Cwd" to `${workspaceFolder}` too.
```

```{admonition} Exercise
Create a new script that, when run, prints "Welcome to Coding for Economists" and run it in an interactive window.
```

## Packages and how to install them

Packages (also called libraries) are key to extending the functionality of Python. The default installation of Anaconda comes with many (around 250) of the packages you'll need, but it won't be long before you'll need to install some extra ones. There are packages for geoscience, for building websites, for analysing genetic data, and, yes, of course, for economics. Packages are typically not written by the core maintainers of the Python language but by enthusiasts, firms, researchers, academics, all sorts! Because anyone can write packages, they vary widely in their quality and usefulness. There are some that are key for an economics workflow, though, and you'll be seeing them again and again.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Name a more iconic trio, I&#39;ll wait. <a href="https://t.co/pGaLuUxQ3r">pic.twitter.com/pGaLuUxQ3r</a></p>&mdash; Vicki Boykis (@vboykis) <a href="https://twitter.com/vboykis/status/1032631145035427840?ref_src=twsrc%5Etfw">August 23, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

The three Python packages **numpy**, **pandas**, and **maplotlib**, which respectively provide numerical, data analysis, and plotting functionality, are ubiquitous. So many scripts begin by importing all three of them, as in the tweet above!

Python packages don't come built-in (by definition) so you need to install them (just once, like installing any other application), and then import them into your scripts (whenever you use them in a script). When you issue an install command for a specific package, it is automatically downloaded from the internet and installed in the appropriate place on your computer.

We use the *terminal* or *command line* within Visual Studio Code to install additional Python packages. In the figure earlier in the Chapter, this is labelled as panel number 4.

To install extra Python packages, you issue install commands to a text-based window called the "terminal".

### The Terminal in Brief

The *terminal* is also known as the *command line* and sometimes the *command prompt*. It was labelled 4 in the screenshot of Visual Studio Code from earlier in the chapter. The terminal is a text-based way to issue all kinds of commands to your computer (not just Python commands) and knowing a little bit about it is really useful for coding (and more) because managing packages, environments (which we haven't yet discussed), and version control (ditto) can all be done via the terminal. We'll come to these in due course, but for now, a little background on what the terminal is and what it does.

```{note}
To open up the command line within Visual Studio Code, use the <kbd>⌃</kbd> + <kbd>\`</kbd> keyboard shortcut (Mac) or <kbd>ctrl</kbd> + <kbd>\`</kbd> (Windows/Linux), or click "View > Terminal".

Windows users may find it easiest to use the Anaconda Prompt as their terminal, at least for installing Python packages.

If you want to open up the command line independently of Visual Studio Code, search for "Terminal" on Mac and Linux, and "Anaconda Prompt" on Windows. 
```

Firstly, everything you can do by clicking on icons to launch programmes on your computer, you can also do via the terminal, also known as the command line. For many programmes, a lot of their functionality can be accessed using the command line, and other programmes *only* have a command line interface (CLI), including some that are used for data science.

```{tip}
The command line interacts with your operating system and is used to create, activate, or change python installations.
```

Use Visual Studio Code to open a terminal window by clicking Terminal -> New Terminal on the list of commands at the very top of the window. If you have installed the Anaconda distribution of Python on your own computer, your terminal should look something like this as your 'command prompt':

```bash
(base) your-username@your-computer current-directory %
```

on Mac, and the same but with '%' replaced by '$' on linux, and (using the Anaconda Prompt)

```bash
(base) C:\Users\YourUsername>
```

on Windows. If you don't see the word `(base)` at the start of the line, you may need to type `conda activate` first.

The `(base)` part is saying that your current Python environment is the base one (eventually, we'll see how to add others for reproducibility and to isolate projects).

You can find out more about the terminal in the chapter on {ref}`wrkflow-command-line`.

### Installing Packages

Install packages on the command line by typing

```bash
pip install package-name
```

and hitting return, where `package-name` might be `pandas`. If you have problems installing, make sure that you are connected to the internet, and that [PyPI](https://pypi.org/) (the Python package index) isn't blocked by your firewall or proxy.

In true programming-humour style, pip is a recursive acronym that stands for 'pip install packages'. You can see what packages you have installed by entering `conda list` into the command line.

## Review

You're ready to move on to the next chapter! 🚀

Well done if you made this far: starting is the hardest bit. (If you want to tweak your Visual Studio Code setup even more, there's some tips at the end of {ref`code-further-advanced`}.)
