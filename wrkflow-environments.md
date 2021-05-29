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
  display_name: 'Python 3.8.6 64-bit (''codeforecon'': conda)'
  language: python
  name: codeforecon
---

# Environments

## Working with Python environments and Anaconda

You don't have to stick to just one Python environment, you can have as many as you like. Running `conda activate base` on the command line (or switching to `base` via the blue bar in VS Code) activates the base environment, but you can create and activate other environments as you like. For example, you could install a Python 3.9 environment alongside your Python 3.8 environment when 3.9 is released.

You can get by just fine using the base Python environment to follow this book. However, it's always good practice to *use a new environment for every project* because, for reproducible research, we want to know what packages were used and be able to export them to a file that others can use too. You might also find that you break environments occasionally, so isolating them into the minimum set of packages needed to produce a distinct set of results is helpful for this reason too. To create a new Python 3.8 environment you would use the following command in the terminal:

```bash
conda create -n newenv python=3.8
```

This will create a brand new Python 3.8 environment called 'newenv' (the part after `-n` is the name). It will only have the barebones packages in; you can install extras as outlined above. At a minimum, you will want jupyter, matplotlib, numpy, and pandas.

To activate and use the new Python environment on the command line, type `conda activate newenv`. This should change `(base)` to `(newenv)` on the command line. Likewise you can switch back with `conda activate base`. Note that this only changes the environment on the command line, what we really want to do is use the new environment in our IDE.

To install a package into a *specific* environment, the easiest way is to activate that environment first by running `conda activate environmentname` followed by installing the package with `conda install packagename` or `pip install packagename`. Here's a full example:

```bash
your-username@your-computer current-directory % conda activate environmentname
(environmentname) your-username@your-computer current-directory % conda install pandas
```

To use your new environment in Visual Studio Code, you may need to restart VS Code. Open up a Python script so that it has its own tab in Visual Studio Code, for example, 'hello_world.py'. Then, in the bottom left-hand corner of Visual Studio Code, you will see what Python environment that you are using. You can click on this to bring up a dropdown menu of all Python environments on your system and just choose whichever you want to use for this project. Visual Studio Code configuration settings for individual folders can be saved as 'workspaces', which remember which Python environment you were using for which folder.

Installing packages one-by-one is very tedious. Fortunately, there's a better way. You can install an entirely new Anaconda environment from a file. Here's an example 'yaml' (this stands for "YAML Ain't Markup Language") file that would be saved as 'codeforecon.yml' and which includes a good standard set of packages for doing economics:

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
    - pandas-profiling
    - pandas-datareader
    - sympy
    - plotnine
    - altair
    - stargazer
    - linearmodels
    - pingouin
    - jupyterlab
```

To install a new environment with these packages, you would need to create a new file called `codeforecon.yml` in Visual Studio Code and copy and paste the list of packages from above into it. Then, the entire environment can be installed on the command line by running (from the same directory as the environment file):

```bash
conda env create -f codeforecon.yml
```

The `-f` flag tells the `conda env create` command that the file with the packages in is to follow; here, that file is called `codeforecon.yml`. When you enter the command on the terminal, you will see packages begin to download and install. Note that most of these packages are installed by conda, with just a few being installed by pip. If you already have a environment with the same name (`codeforecon` in this case), the command will fail as you can't overwrite an existing environment-you'd need to remove it first.

This approach saves the tedium of installing packages one-by-one, and it gives you a nice separate environment for going through 'coding for economists'. Remember, to use the new environment, use the button in Visual Studio Code or `conda activate codeforecon` on the command line. You can find much more details of how to use environments--including deleting them--over on Anaconda's [guide to managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).