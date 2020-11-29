# Preliminaries

In this chapter, you'll find out how to install and setup everything you need to get coding.

## What is coding?

Computer programming, or coding, is the process of issuing a series of commands that a computer can understand and execute in order to perform a task. Given so much of economics is quantitative, coding is an essential skill for many economists.

As a skill, programming is incredibly useful in a wide range of domains. It can be hugely rewarding. It's worth saying at the outset though, that, *no-one*, and I mean no-one, memorises half of the stuff you'll see in this book. 80% or more of time spent programming is actually time spent looking up how to do this or that online, 'debugging' a code for errors, or testing code. This applies to all programmers, regardless of level. You are here to learn the skills and concepts of programming, not the precise syntax (which is easy to look up later).

![xkcd-what-did-you-see](https://imgs.xkcd.com/comics/wisdom_of_the_ancients.png)

## Notation

Greek letters, like $\beta$, are the truth. Modified Greek letters are an estimate of the truth, for example $\hat{\beta}$. Letters from the Latin alphabet denote the values of data, for instance $x$ for a variable or vector. Modified Latin alphabet letters denote computations performed on data, for instance $\bar{x} = \frac{1}{N} \displaystyle\sum_{i} x_i$.

## Computational environment

### Choice of programming language

This book uses Python, which is usually ranked as the first or second most popular programming language in the world and, just as importantly, it's also one of the easiest to learn. The joke goes that Python is the 2nd best language at everything, and there's some truth to that (although Python is 1st best in machine learning). But a language that covers such a lot of ground is also very useful; and Python is widely used across industry, academia, and the public sector. It is used for everything from computer games to websites, data science to software applications.
As an economist, you will know that this means it benefits from strong positive network externalities. As such, learning Python has a lot of value and, once you have, learning more specialised languages like C++ or R is much easier. Basic programming concepts can be found in almost any programming language. Because of their similarities, however, readers will find that they can follow even more of the content of the book in some specific other languages, especially Julia and R.

![xkcd-python](https://imgs.xkcd.com/comics/python.png)

Different languages have different strengths and weaknesses. Python and Julia are so-called high-level languages that are easier to write code in. C++ and Fortran are more low-level languages and much more fussy and labour-intensive to write code in; but, once the code is written, it runs *fast*.

Another big difference between languages is the extent to which users have created software that extends the base functionality of the language. The ecosystem of other users, and what they're using the language for, is really important for determining how useful a language is. For example, Python and R have vibrant data science communities producing extensions (called libraries or packages) that are what really make those languages so useful for data science (far more than the base functionality of either).

Programming languages come in versions, which can be quite different, and some of the most important functionality of programming languages is provided by add-ons called packages or libraries, which themselves have versions. To make matters worse, not all versions of packages and languages will work together, and the combinations that work may depend on your operating system (Windows, Mac, etc)!

The combination of the language and its version (eg Python 3.6.1), the packages and their versions (eg numpy 1.19), and the operating system the code is being run on (eg MacOS Catalina) is called the computational environment.

To programme, you will need two things on your computer:

- an installation of the programming language

- a way to write commands that can be executed, known as an integrated development environment (IDE)

### Installing Python

Download the individual edition of the [Anaconda distribution](https://www.anaconda.com/) of Python for your operating system and install it (currently found under Products -> Individual Edition). This will provide you with a Python installation and a host of the most useful libraries.

### Installing an integrated development environment (IDE)

An integrated development environment is a software application that provides a few tools to make coding easier. The most important of these is a way to write the code itself! IDEs are not the only way to programme, but they are the most useful. If you have used **Stata** or **Matlab**, you may not have realised it, but these package up the language and the IDE together. But they are separate things: the language is like a language, the IDE is the notebook that you write it in.

Here are some of the useful features an IDE might have:

- a way to run your code interactively (line-by-line)

- a way to debug (look for errors) in your code

- a quick way to access helpful information about commonly used software packages

- automatic code formatting, so that your code follows best practice guidelines

- auto-completion of your code

- automatic code checking for basic errors

People have strong feelings about which IDE they prefer. I strongly recommmend [Visual Studio Code](https://code.visualstudio.com/), a free and open source IDE from Microsoft that is available on all major operating systems. Just like Python itself, Visual Studio can be extended with packages, and it is those packages, called extensions in this case, that make it so useful.

Download and install Visual Studio Code and then navigate to the 'extensions' tab on the left hand side. You'll need to install the following extensions, which you can search for by using the text box:

- Python
- Pylance

If you have installed these then you are ready to run your first script!

## Running your first code: Hello World!

Now you will run your first code. Create a new folder for your work (perhaps named 'codingforeconomists', no white space), open that folder with Visual Studio Code ,and create a new file, naming it `hello_world.py`. In the Visual Studio Code editor, add a single line to the file:

```python
print('Hello World!')
```

Hit save. If you now select/highlight this text and right-click you should seem some options, including 'Run Selection/Line in Terminal' and `Run Selection/Line in Interactive Window'. Because VS Code is a richly featured IDE, there are lots of options for how to run the file. Let's try both of the main ways: the terminal and the interactive window.

To run the code in the **terminal**, right-click and select 'Run Python file in terminal'. This will bring up a new window terminal *within* Visual Studio Code that runs your entire script--and you should see 'Hello World!' pop up!

The other way of working, with the interactive window, will be much more familiar to anyone who has used Stata or Matlab and is much more suited to the way economists tend to work because it doesn't require you to write the whole script, start to finish, ahead of time. Instead, you can jam, changing code as you go, (re-)running it line by line. To run the code in an interactive window, **right-click and select 'Run Selection/Line in Interactive Window'**. This should cause a new interactive window to appear within Visual Studio Code, and the line to execute within it.

At this point, you may see a message about the default behaviour when you press shift+return; for this book, it's good to have shift+return default to running a line in the interactive window.

Let's make more use of the interactive window. At the bottom of it, there is a box that says 'Type code here and press shift-enter to run'. Go ahead and type `print('Hello World!')` directly in there to achieve the same effect as running the line from your script. Also, any variables you run in the interactive window (from your script or directly) will persist.

This shows the two ways of working with the interactive window--running from a script, or writing code directly.

## Packages, environments, and the terminal

### The terminal

In the section above, I mentioned the *terminal*. This is a text-based way to issue commands to your computer and knowing a little bit about it is really useful for coding (and more) because managing packages, environments (which we haven't yet discussed), and version control (ditto) is all done via the terminal. We'll come to these in due course, but for now, a little background on what the terminal is and what it does.

Firstly, everything you can do by clicking on icons to launch programmes on your computer, you can also do via the terminal, also known as the command line. For many programmes, a lot of their functionality can be accessed using the command line, and other programmes *only* have a command line interface (CLI), including some that are used for data science. If you have installed the Anaconda distribution of Python, your terminal should look something like this as your 'command prompt':

```bash
(base) your-username@your-computer current-directory %
```

on Mac, and the same but with '%' replaced by '$' on linux, and

```powershell
(base) C:\Users\YourUsername>
```

on Windows. If you don't see the word `(base)` at the start of the line, you may need to type `conda activate` first.

The `(base)` part is saying that your current Python environment is the base one (later, we'll see how to add others for reproducibility and to isolate projects). Unfortunately, and confusingly, the commands that you can use in the terminal on Mac and Linux, on the one hand, and Windows, on the other, are different. This won't be much of an issue in practice.

For now, to at least try out the command line, let's use something that works across all three of the major operating systems. Use Visual Studio Code to open a terminal window by clicking Terminal -> New Terminal. You should see the command prompt for your system. Now type `python`. You should see information about your installation of Python appear, including the version, followed by a Python prompt that looks like `>>>`. This is a kind of interactive Python session. It's much less rich than the one available in Visual Studio Code (it can't run scripts, for example) but you can try `print('Hello World!')` and it will run, printing your message. To exit the terminal-based Python session, type `exit()` to go back to the regular command line.

If you're using a bash or zsh terminal, there are a couple of commands that are so essential it would be remiss *not* to mention them. One is to list the contents of the current directory, for which the command is `ls`. The other is to move directory, for which the command is `cd`. If you find that you've opened a terminal you can always get a sense of where you are from `ls` and move to where you need to be using `cd directory/`. One of the advantages of opening a folder in Visual Studio Code and then opening a terminal with Code using 'New Terminal' is that the terminal will open in the folder you're working in.

### Installing packages

The default installation of Anaconda comes with many of the packages you'll need, but it won't be long before you'll need to install some extra ones. Extra packages, for example for regression, deliver a lot of the value of a programming language. You may sometimes hear that Python is a 'batteries included' programming language, meaning that the base language is very rich. This is definitely true! But even so, we'll extend it further

To install extra Python packages, there are two options, and both use the command line. Once you have activated the environment you'd like to install the package in, for instance with `conda activate environmentname`, you install packages using another command.

For very widely used packages, you can often use `conda install packagename`. Anaconda provide pre-built packages that are convenient for a host of reasons. If there isn't a pre-built Anaconda version of the package available, you can fall back on installing via pip using

```bash
pip install packagename
```

In true programming-humour style, pip is a recursive acronym that stands for 'pip install packages'. By default, packages are installed into your `base` Python environment.

### (Advanced) Working with Python environments and Anaconda

You can get by just fine using the base Python environment to follow this book. However, it's always good practice to *use a new environment for every project* because, for reproducible research, we want to know what packages were used and be able to export them to a file that others can use too. For example, if you're following this book by running the code yourself, it's a good idea to create a new environment using the following command:

```bash
conda create -n codeforecon python=3.8
```

This will create a brand new Python 3.8 environment called 'codeforecon'. It will only have the barebones packages in; you can install extras as outlined above. At a minimum, you will want jupyter, matplotlib, numpy, and pandas.

To activate and use the new Python environment on the command line, type `conda activate codeforecon`. This should change `(base)` to `(codeforecon)` on the command line. Likewise you can switch back with `conda activate base`. Note that this only changes the environment on the command line, what we really want to do is use the new environment in our IDE.

To use your new environment in Visual Studio Code, you may need to restart it. Open up a Python script, for example, 'hello_world.py'. Then, in the bottom left-hand corner of Visual Studio Code, you will see what Python environment that you are using. You can click on this to bring up a dropdown menu of all Python environments on your system and just choose whichever you want to use for this project. Visual Studio Code configuration settings for individual folders can be saved as 'workspaces', which remember which Python environment you were using for which folder.

Installing packages one-by-one is very tedious. Fortunately, there's a better way. You can install an entire Anaconda environment from a file. Here's an example which would be saved as 'codeforeconomists.yml':

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
  - pip:
    - jupyter-book
    - specification_curve
    - ghp-import
    - pandas-profiling
```

Note that most of these packages will be installed by conda, with just a few being installed by pip. The entire environment can be installed on the command line by running (from the same directory as the environment file):

```bash
conda env create -f codeforecon.yml
```

This saves the tedium of installing packages one-by-one, and it gives you a nice separate environment for going through 'coding for economists'. Remember, to use the new environment, use the button in Visual Studio Code or `conda activate codeforecon` on the command line. You can find much more details of how to use environments--including deleting them--over on Anaconda's [guide to managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Review

If you have:

- [x] installed Python, using the Anaconda distribution of Python;
- [x] installed Visual Studio Code, and its Python and Pylance extensions;
- [x] written and saved 'hello_world.py' with `print('Hello World!')` in it; and
- [x] run 'hello_world.py' both in the terminal and in the Visual Studio Code interactive window, then

you are ready to move on to the next chapter!
