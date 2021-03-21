# Preliminaries

In this chapter, you'll find out how to install and setup everything you need to get coding.

## Computational environment

### Operating system

Almost all of the code you'll see can be run on all three of the major operating systems: Windows, MacOS, and Linux.

However, if you haven't yet decided which operating system to use, I strongly recommend that you choose either Linux or MacOS because, in a small number of cases, your code, third party packages and libraries, and coding related tools like Docker, either won't work at all on Windows or will be *much* more difficult to set up. (Don't panic if you have Windows already: we'll come to a workaround in a moment.) Although it is rare that you run into a case like this, it's just often enough for it to be a real pain. Furthermore, if you ever need to scale up your work to the cloud, you'll find that it's more cost effective to use machines that have use an operating system closer to Linux (which MacOS is). While Macs are famous for being expensive, most Linux distributions are free, so you should be able to find a code-friendly operating system to satisfy any budget constraint. Linux used to have a reputation as being fearsomely difficult for beginners. But modern Linux distributions, such as Ubuntu, are pretty user-friendly.

If you are using Windows, then a good workaround for some of these issues is to use the [*Windows Subsystem for Linux*](https://pbpython.com/wsl-python.html). It's essentially a Linux operating system that installs alongside and integrates with your existing Windows operating system. This allows you to run code as if you were using Linux. You can get WSL [for free from Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

### Choice of programming language

This book uses Python, which is usually ranked as the first or second most popular programming language in the world and, just as importantly, it's also one of the easiest to learn. It's a general purpose language, which means it can perform a wide range of tasks. This combination of features is why people say Python has a low floor and a high ceiling. It's also very versatile; the joke goes that Python is the 2nd best language at everything, and there's some truth to that (although Python is 1st best at some tasks, like machine learning). But a language that covers such a lot of ground is also very useful; and Python is widely used across industry, academia, and the public sector. Python is the main 'dynamic' language used at [Google](https://google.github.io/styleguide/pyguide.html) and the [most demanded language](https://insights.dice.com/2020/12/01/7-programming-languages-popular-at-apple-that-could-land-you-a-job/) in jobs for Apple. It is used for everything from computer games to websites, data science to software applications: it's even being used to help [fly a helicopter on Mars](https://github.com/nasa/fprime). As an economist, you will know that this means Python benefits from strong positive network externalities. As such, learning Python has a lot of value and, once you have, learning more specialised languages like C++ or R is much easier; many of the basic programming concepts you'll see in this book are useful in almost any programming language. Because of their similarities, however, readers will find that they can follow even more of the content of the book in some specific other languages, especially Julia and R.

![xkcd-python](https://imgs.xkcd.com/comics/python.png)

Different languages have different strengths and weaknesses. Python and Julia are so-called high-level languages that are easier to write code in. C++ and Fortran are more low-level languages and much more fussy and labour-intensive to write code in; but, once the code is written (and 'compiled'), it runs *fast*.

Another big difference between languages is the extent to which users have created software that extends the base functionality of the language. The ecosystem of other users, and what they're using the language for, is really important for determining how useful a language is. For example, Python and R have vibrant data science communities producing extensions (called libraries or packages) that are what really make those languages so useful for data science (far more than the base functionality of either).

Programming languages come in versions, which can be quite different, and some of the most important functionality of programming languages is provided by add-ons called packages or libraries, which themselves have versions. To make matters worse, not all versions of packages and languages will work together, and the combinations that work may depend on your operating system (Windows, Mac, etc)!

The combination of the language and its version (eg Python 3.6.1), the packages and their versions (eg numpy 1.19), and the operating system the code is being run on (eg MacOS Catalina) is called the computational environment.

To programme, you will need two things on your computer:

- an installation of the programming language

- a way to write and run scripts, using an integrated development environment (IDE)

### Installing Python

Download the individual edition of the [Anaconda distribution](https://www.anaconda.com/) of Python for your operating system and install it (on Anaconda's website, this is currently found under Products -> Individual Edition). This will provide you with a Python installation and a host of the most useful libraries.

Anaconda might ask whether you want to add Anaconda to your PATH environment variable. Your PATH variable is a list of where programmes are located on your computer that *other* programmes can see. By adding Anaconda to your PATH, you will be able to more easily launch applications that make use of Python.

You can confirm that you've set up Anaconda correctly by following the [verify installation instructions](https://docs.anaconda.com/anaconda/install/verify-install/) on the Anaconda website.

Python and Anaconda are available on all major operating systems.

### Installing an integrated development environment (IDE)

An integrated development environment is a software application that provides a few tools to make coding easier. The most important of these is a way to write the code itself! IDEs are not the only way to programme, but they are perhaps the most useful. If you have used **Stata** or **Matlab**, you may not have realised it, but these package up the language and the IDE together. But they are separate things: the language is a way of processing your instructions, the IDE is where you write those instructions.

Here are some of the useful features an IDE might have:

- a way to run your code interactively (line-by-line) or all at once

- a way to debug (look for errors) in your code

- a quick way to access helpful information about commonly used software packages

- automatic code formatting, so that your code follows best practice guidelines

- auto-completion of your code

- automatic code checking for basic errors

People have strong feelings about which IDE they prefer. I strongly recommend [Visual Studio Code](https://code.visualstudio.com/), a free and open source IDE from Microsoft that is available on all major operating systems. Just like Python itself, Visual Studio can be extended with packages, and it is those packages, called extensions in this case, that make it so useful. Visual Studio Code is available on all major operating systems.

Download and install Visual Studio Code. If you need some help, see this [very short tutorial](https://code.visualstudio.com/docs/python/python-tutorial) on setting it up from Microsoft (ignore the bits about debugging and installing packages).

Once you have Visual Studio Code installed and opened, navigate to the 'extensions' tab on the left hand side navigation bar. You'll need to install the following extensions, which you can search for by using the text box:

- Python
- Pylance
- Jupyter

If you have installed these and Python then you are ready to run your first script!

## Running your first code: Hello World!

Now you will run your first code. Create a new folder for your work (perhaps named 'codingforeconomists', no white space), open that folder with Visual Studio Code and create a new file, naming it `hello_world.py`. The file extension, `.py`, is very important as it implicitly tells Visual Studio Code that this is a Python script. In the Visual Studio Code editor, add a single line to the file:

```python
print('Hello World!')
```

Hit save. If you now select/highlight this text and right-click you should seem some options, including 'Run Selection/Line in Terminal' and `Run Selection/Line in Interactive Window'. Because VS Code is a richly featured IDE, there are lots of options for how to run the file. Let's try both of the main ways: the terminal and the interactive window.

To run the code in the **terminal**, right-click and select 'Run Python file in terminal'. This will bring up a new panel (called a terminal) *within* Visual Studio Code that runs your entire script from top to bottom-and you should see 'Hello World!' pop up!

The other way of working, with the interactive window, will be much more familiar to anyone who has used Stata or Matlab and is much more suited to the way economists tend to work because it doesn't require you to write the whole script, start to finish, ahead of time. Instead, you can jam, changing code as you go, (re-)running it line by line. To run the code in an interactive window, **right-click and select 'Run Selection/Line in Interactive Window'**. This should cause a new 'interactive' panel to appear within Visual Studio Code, and only the selected line will execute within it.

At this point, you may see a message about Visual Studio Code's default behaviour when you press shift+return; for this book, it's good to have shift+return default to running a line in the interactive window.

```{admonition} Making code run in the interactive window by default
:class: dropdown

Open up Visual Studio Code and go to settings (click on the cog in the bottom left-hand corner, then click settings).

Type 'python send' into the search box. Depending on your configuration and Visual Studio Code version, you will either see 'Python › Data Science: Send Selection To Interactive Window' or 'Jupyter: Send Selection To Interactive Window'. Make sure that there is a tick in the box.

This will ensure that when you hit shift+enter on code scripts, it will execute your code in Visual Studio's interactive window (starting a new window if necessary).

```

Let's make more use of the interactive window. At the bottom of it, there is a box that says 'Type code here and press shift-enter to run'. Go ahead and type `print('Hello World!')` directly in there to achieve the same effect as running the line from your script. Also, any variables you run in the interactive window (from your script or directly by entering them in the box) will persist.

To see how variables persist, type `hello_string = 'Hello World!'` into the interactive window's code entry box and hit shift-enter. If you now type `hello_string` and hit shift+enter, you will see the contents of the variable you just created. You can also click the grid symbol at the top of the interactive window (between the stop symbol and the save file symbol); this is the variable explorer and will pop open a panel showing all of the variables you've created in this interactive session. You should see one called `hello_string` of type `str` with a value `Hello World!`.

This shows the two ways of working with the interactive window--running (segments) from a script, or writing code directly in the entry box.

## Packages, environments, and the terminal

### The terminal in brief

In the section above, I mentioned the *terminal*. This is a text-based way to issue all kinds of commands to your computer (not just Python commands) and knowing a little bit about it is really useful for coding (and more) because managing packages, environments (which we haven't yet discussed), and version control (ditto) can all be done via the terminal. We'll come to these in due course, but for now, a little background on what the terminal is and what it does.

Firstly, everything you can do by clicking on icons to launch programmes on your computer, you can also do via the terminal, also known as the command line. For many programmes, a lot of their functionality can be accessed using the command line, and other programmes *only* have a command line interface (CLI), including some that are used for data science. If you have installed the Anaconda distribution of Python, your terminal should look something like this as your 'command prompt':

```bash
(base) your-username@your-computer current-directory %
```

on Mac, and the same but with '%' replaced by '$' on linux, and

```bash
(base) C:\Users\YourUsername>
```

on Windows. If you don't see the word `(base)` at the start of the line, you may need to type `conda activate` first.

The `(base)` part is saying that your current Python environment is the base one (later, we'll see how to add others for reproducibility and to isolate projects). Unfortunately, and confusingly, the commands that you can use in the terminal on Mac and Linux, on the one hand, and Windows, on the other, are different. This won't be much of an issue in practice.

For now, to at least try out the command line, let's use something that works across all three of the major operating systems. Use Visual Studio Code to open a terminal window by clicking Terminal -> New Terminal on the list of commands at the very top of the window. You should see the command prompt for your system. Now type `python`. If you installed Python, and put it on your PATH, you should see information about your installation of Python appear, including the version, followed by a Python prompt that looks like `>>>`. This is a kind of interactive Python session, in the terminal. It's much less rich than the one available in Visual Studio Code (it can't run scripts, for example) but you can try `print('Hello World!')` and it will run, printing your message. To exit the terminal-based Python session, type `exit()` to go back to the regular command line.

If you're using a bash or zsh terminal, there are a couple of commands that are so essential it would be remiss *not* to mention them. One is to list the contents of the current directory, for which the command is `ls`. The other is to move directory, for which the command is `cd`. If you find that you've opened a terminal you can always get a sense of where you are from `ls` and move to where you need to be using `cd directory/`. One of the advantages of opening a folder in Visual Studio Code and then opening a terminal with Code using 'New Terminal' is that the terminal will open in the folder you're working in (which is usually where you want to be).

### Installing packages

The default installation of Anaconda comes with many of the packages you'll need, but it won't be long before you'll need to install some extra ones. Extra packages, for example for regression, deliver a lot of the value of a programming language. You may sometimes hear that Python is a 'batteries included' programming language, meaning that the base language is very rich. This is definitely true! But even so, for economics, we'll extend it further in numerous ways.

To install extra Python packages, there are two options, and both use the command line. You'll need to have conda activated before installing a package--if you don't see the name of an environment, eg `(base)`, at the start of your terminal's line, use the `conda activate` command first. Once you have activated the conda environment, you install packages using another command.

For very widely used packages, you can often use `conda install packagename`. Anaconda provide pre-built packages that are convenient for a host of reasons. If there isn't a pre-built Anaconda version of the package available, you can fall back on installing via pip using

```bash
pip install packagename
```

In true programming-humour style, pip is a recursive acronym that stands for 'pip install packages'. By default, packages are installed into your `base` Python environment.

Here's a full example of the commands used to install the **pandas** package into the base environment:

```bash
your-username@your-computer current-directory % conda activate
(base) your-username@your-computer current-directory % conda install pandas
```

### (Advanced) Working with Python environments and Anaconda

You can get by just fine using the base Python environment to follow this book. However, it's always good practice to *use a new environment for every project* because, for reproducible research, we want to know what packages were used and be able to export them to a file that others can use too. For example, if you're following this book by running the code yourself, it's a good idea to create a new environment using the following command:

```bash
conda create -n codeforecon python=3.8
```

This will create a brand new Python 3.8 environment called 'codeforecon'. It will only have the barebones packages in; you can install extras as outlined above. At a minimum, you will want jupyter, matplotlib, numpy, and pandas.

To activate and use the new Python environment on the command line, type `conda activate codeforecon`. This should change `(base)` to `(codeforecon)` on the command line. Likewise you can switch back with `conda activate base`. Note that this only changes the environment on the command line, what we really want to do is use the new environment in our IDE.

To install a package into a *specific* environment, the easiest way is to activate that environment first by running `conda activate environmentname` followed by installing the package with `conda install packagename` or `pip install packagename`. Here's a full example:

```bash
your-username@your-computer current-directory % conda activate environmentname
(environmentname) your-username@your-computer current-directory % conda install pandas
```

To use your new environment in Visual Studio Code, you may need to restart it. Open up a Python script, for example, 'hello_world.py'. Then, in the bottom left-hand corner of Visual Studio Code, you will see what Python environment that you are using. You can click on this to bring up a dropdown menu of all Python environments on your system and just choose whichever you want to use for this project. Visual Studio Code configuration settings for individual folders can be saved as 'workspaces', which remember which Python environment you were using for which folder.

Installing packages one-by-one is very tedious. Fortunately, there's a better way. You can install an entire Anaconda environment from a file. Here's an example 'yaml' (this stands for "YAML Ain't Markup Language") file that would be saved as 'codeforecon.yml' and which includes a good standard set of packages for doing economics:

```yaml
name: codeforecon
channels:
  - conda-forge
  - defaults
dependencies:
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - pip
  - python=3.8
  - pyyaml
  - scikit-learn
  - scipy
  - seaborn
  - statsmodels
  - tqdm
  - yaml
  - pycodestyle
  - autopep8
  - pyarrow
  - pip:
    - jupyter-book
    - pandas-profiling
    - pandas-datareader
    - sympy
    - plotnine
    - altair
    - stargazer
    - linearmodels
```

Note that most of these packages will be installed by conda, with just a few being installed by pip. The entire environment can be installed on the command line by running (from the same directory as the environment file):

```bash
conda env create -f codeforecon.yml
```

This saves the tedium of installing packages one-by-one, and it gives you a nice separate environment for going through 'coding for economists'. Remember, to use the new environment, use the button in Visual Studio Code or `conda activate codeforecon` on the command line. You can find much more details of how to use environments--including deleting them--over on Anaconda's [guide to managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## (Advanced) Fine-tuning your integrated development environment

If you just want to get on with some coding, feel free to skip this section.

Once you've downloaded *Visual Studio Code* and installed some basic extension - Python, Pylance, and Jupyter - you'll have enough to get going but VS Code can do a whole lot more with some extra add ons. You can install these using the extensions tab on the left hand side of VS Code. Here are the ones I recommend and why:

- Markdown extensions - markdown is a simple text language that is often used to provide readmes for code repositories. It comes with the file extension .md
  - *Markdown All in One*, to help writing Markdown docs.
  - *Markdown Preview Enhanced*, to view rendered markdown as you type it (right click and select 'Open Preview...').
- Coding extensions
  - *Bracket Pair Colorizer 2*, which allows matching brackets to be identified with colours. Very useful when you have nested methods!
  - *indent-rainbow*, gives different levels of indentation different colours for ease of reading.
  - *Path Intellisense*, autocompletes filenames in code.
- Version control
  - *Git History*, view and search your git log along and show a graph of git commits with details.
  - *GitLens*, helps to visualise code authorship at a glance via 'Git blame' annotations, navigate and explore Git repositories, and more.
  - *Code Spell Checker*, does exactly what it says, really useful for avoiding mangled variable name errors. To ensure it uses 'British English', change the 'C Spell: Language' text from 'en' to 'en-GB' in VS Code's settings. Other languages are available as separate extensions.
- General
  - *Rainbow CSV*, uses colour to make plain old CSV files much more readable in VS Code.
  - *vscode-icons*, intelligent icons for your files as seen in the VS Code file explorer, eg a folder called data gets an icon showing a disc drive superimposed onto a folder.
- LaTex - it's a bit of surprise, but VS Code is one of the best LaTeX editors out there: if not *the* best. You will need LaTeX installed already though and initial setup of a compilation 'recipe' is a bit fiddly (though, once it works, it's dreamy).
  - *LaTeX Workshop*, provides core features for LaTeX typesetting with Visual Studio Code.
  - *LaTeX Preview*, both in-line and side-by-side previews of LaTeX code. A really fantastic extension.

As well as adding extra extensions, you can customise the default settings of VS Code. As mentioned before, you'll probably want to change the `jupyter.sendSelectionToInteractiveWindow` setting to True. The easiest way to do this is to go to Settings (the cog icon) and type in 'Jupyter: Send Selection', and you should see a tick box come up; make sure it's ticked.

Another useful one for coding is to change the 'Editor: Render Whitespace' setting, aka `editor.renderWhitespace` from 'selection' to 'boundary'. This will now show any boundary whitespace, or more than one instance of whitespace contiguously, as a grey dot. This might seem odd but it's really useful because the wrong amount of whitespace can create problems with code.

## Review

If you have:

- ✅ installed Python, using the Anaconda distribution of Python;
- ✅ installed Visual Studio Code, and its Python and Pylance extensions;
- ✅ written and saved 'hello_world.py' with `print('Hello World!')` in it; and
- ✅ run 'hello_world.py' both in the terminal and in the Visual Studio Code interactive window, then

you are ready to move on to the next chapter!
