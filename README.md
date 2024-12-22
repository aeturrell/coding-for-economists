# Coding for Economists

[![DOI](https://zenodo.org/badge/316842103.svg)](https://zenodo.org/doi/10.5281/zenodo.10465358)  ![GitHub Release](https://img.shields.io/github/v/release/aeturrell/coding-for-economists)

To read or use the book, head to the [*Coding for Economists* website](https://aeturrell.github.io/coding-for-economists/intro.html).

The rest of this readme is intended to help those who are contributing to the book, rather than readers.

## Dev

These instructions are only for developers working on the book.

### Making Changes

Contributions to *Coding for Economists* are welcome! If you're planning to make a pull request, it's usually best to lodge an issue to discuss it first but feel free to go straight to making a pull request for corrections, typos, and fixing out of date package issues.

To make changes:

1. create a new branch
2. install the Python environment or alternatively build and work in the docker image (which comes with the Python environment)
3. make your changes using the Python environment
4. if you installed new packages then update the package list in `environment.yml`
5. run pre-commit using `pre-commit run --all-files`
6. if the checks clear, commit your change and, finally, make a pull request
7. your pull request will be reviewed and, hopefully, your changes merged into the book

Note that when a pull request is accepted, it doesn't automatically change the website, just the code. We periodically update the website to reflect underlying changes in the repo.

### Setting up the Environment

The *Coding for Economists* Python environment can be installed using

```bash
conda env create -f environment.yml
```

on the command line. **This takes a long time to install with vanilla Conda and we strongly recommend using *Mamba* to speed it up**. The Dockerfile version uses **Mamba** for this reason. The environment construction is slower than is ideal because *Coding for Economists* depends on a LOT of packages, which in turn have a lot of dependencies.

You can check that this has worked by running `which python` on the command line. You should get something like

```bash
/Users/USERNAME/opt/anaconda3/envs/codeforecon/bin/python
```

If you don't, and you get something like `/usr/bin/python` instead, then you need to following the instructions for the command line version of Python being incorrect below.

Some extra assets are required to successfully build the book. You can see how to install these automatically (for Linux at least) by looking at the Dockerfile.

- Natural language processing models: within the Python environment, you will need to run `python -m spacy download en_core_web_sm` to download the spacy model, and `python3 -m nltk.downloader all` for the **nltk** models.
- Fonts: The book uses some special fonts, such as Varta, which you can find on Google fonts.
- LaTeX: The book was built with TeX Live.

### Using the docker image

There is a Dockerfile for the environment, which is the easiest way to set up a dev env. You run it by following these steps:

1. Ensure you have docker, the docker extension for VS Code, and the VS Code remote extension installed
2. In VS Code, right-click on the Dockerfile and hit "build image". Switch to the docker tab and hit "Run interactive". Switch to the VS Code Remote tab, then click "Attach in new window" on the running container.
3. Once you are in the container via VS Code remote, you may need to install the Python extension (within the container version of VS Code).
4. Open up the relevant folder, "app", in VS Code remote. It's usually in `../app`.
5. Once you are in the container, you'll need to use `conda activate codeforecon` to switch to the right conda environment to build files and run notebooks. The build command is as usual for Jupyter Book: `jupyter-book build .`.
6. To ping back the built HTML files, use `docker cp running-container-name:app/_build/ .` from your local command line (not the docker container) within the folder where you want to move all of the build files. We suggest creating a "scratch" folder and running the command from within it, or transferring directly to your local "_build" folder. You can partially view the HTML within the docker container using a HTML preview extension but note that MathJax and internal book links won't work.

Warning: if you are building the Dockerfile with the environment, it will take some time to build.

There is a bug that arises during builds due to the many dependencies of the book—this is automatically addressed by the Dockerfile but you may be interested in what is going on. It comes from a list index error. You can squish this manually by commenting out `token.children[1].content = token.children[1].content[3:]` in `"/opt/conda/envs/codeforecon/lib/python3.10/site-packages/mdit_py_plugins/tasklists/__init__.py"`, usually line 90, in todoify. (This is due to version issues between **markdown-it-py**, **myst-nb**, and **myst-parser**.) On a Mac, this line will likely be at `"/Users/USERNAME/mambaforge/envs/codeforecon/lib/python3.10/site-packages/mdit_py_plugins/tasklists/__init__.py"`.

### Building the Book

To build the book using **Jupyter Book** use

```bash
jupyter-book build .
```

Once this command is run, you should be able to look at the HTML files for the book locally on your computer.

Note that, due to package conflicts, several pages may not compile when taking this approach. One work around is to manually re-run troublesome notebooks and, when jupyter-book encounters a problem when executing them, it will pick up the notebook at the last point it was successfully manually executed. If you do have this problem, it may be that jupyter-book is not picking up the right jupyter kernel. You can look at installed kernels within your current Python environment using `jupyter kernelspec list` on the command line.

### Uploading Built Files

Only upload built files based on a successful commit or merge to the main branch. See [here](https://jupyterbook.org/publish/gh-pages.html) for how to upload revised HTML files, but the key command is

```bash
ghp-import -n -p -f _build/html
```

Typically, only maintainers will need to upload built files.

### Pre-commit

To perform the pre-commit checks, use

```bash
pre-commit run --all-files
```

Pre-commit is currently configured to:

- check for large added files
- strip outputs from notebooks
- apply the [black](https://black.readthedocs.io/en/stable/) code formatter to .py and .ipnb scripts

If **black-nb** finds a pre-commit error that is difficult to diagnose, a tip is to convert it to a regular script to find the problem, using, for example,

```bash
jupytext --to py data-intro.ipynb
```

## Good to Know

### Debugging notebook errors

If you get a

```bash
File "python3.8/site-packages/myst_nb/parser.py", line 139, in nb_to_tokens
    start_line = source_map[cell_index] if source_map else (cell_index + 1) * 10000
IndexError: list index out of range
```

error then it may be that the notebook metadata has gone awry. If you can isolate the notebook, you can refresh the metadata by running:

```bash
jupytext --to py bad_notebook.ipynb
jupytext --to notebook bad_notebook.py
```

This will overwrite the existing notebook!

### Command line version of Python is incorrect

Deactivate the conda environment (until even the base environment is deactivated) using `conda deactivate`. Then activate your environment with `conda activate your_env_name_goes_here`.

### Special Fonts

This book uses some special fonts, such as Varta. If you install these manually, you may need to refresh your Matplotlib font cache before you can see the new fonts at work:

```bash
rm ~/.matplotlib/fontlist-v330.json
```

## Creating a release

Head over to GitHub, and go to the releases page. Create a tag with the new version number, eg `v1.0.3`. Use the generate release notes button. Then publish. The Zenodo repository and version badge on the intro page will update automatically. The releases and the uploaded website should be consistent.
