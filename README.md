# coding-for-economists

This readme is intended to help those contributing to or editing the book, not those trying to follow it. To read or use the book, head to the [coding for economists website](https://aeturrell.github.io/coding-for-economists/intro.html). You can use the book interactively via the following options, all available via the link above:

- download pages to your computer as jupyter notebooks
- run pages in Google Colab through your browser

## Dev

These instructions are only for developers working on the book.

### Making A Change

To make a change, create a new branch, install the environment or use the docker image or build the docker image, make your change, if you installed new packages then update the package list in `environment.yml`, run pre-commit using `pre-commit run --all-files`, if the checks clear then commit your change and, finally, make a pull request. But do speak to us before making a pull request.

Another way to make a change or contribute is to submit a notebook.

### Setting up the Environment

In principle, the environment can be installed using

```bash
conda env create -f environment.yml
```

on the command line. **This takes a really, really long time to install**. The dockerfile version uses **Mamba** to speed up the install. The environment construction is slow because Coding for Economists depends on a LOT of packages, which in turn have a lot of dependencies.

You can check that this has worked by running `which python` on the command line. You should get something like

```bash
/Users/USERNAME/opt/anaconda3/envs/codeforecon/bin/python
```

If you don't, and you get something like `/usr/bin/python` instead, then you need to following the instructions for the command line version of Python being incorrect below.

Some extra assets associated with packages are required. You will need to run `python -m spacy download en_core_web_sm` to download the spacy model, and `python3 -m nltk.downloader all` for the **nltk** models.

### Using the docker image

There is a Dockerfile for the environment, which is the easiest way to set up a dev env. You run it by following these steps:

1. Ensure you have docker, the docker extension for VS Code, and the Code remote extension installed
2. In VS Code, right click on the Dockerfile and hit "build image". Switch to the docker tab and hit "Run interactive". Switch to the VS Code Remote tab, then click "Attach in new window" on the running container.
3. Once you are in the container via VS Code remote, you may need to install the Python extension (within the container version of VS Code).
4. If you're using the pre-built image from Dockerhub, you will need to ensure that you have the latest git commit of the code (for now, the Dockerhub image isn't automatically updated when a new commit is made).
5. Open up the relevant folder, "app", in VS Code remote.
6. Once you are in the container, you'll need to use `conda activate codeforecon` to switch to the right conda environment to build files and run notebooks.
7. To ping back the built HTML files, use `docker cp running-container-name:app/_build/ .` from your local command line (not the docker container) within the folder where you want to move all of the build files. We suggest creating a "scratch" folder and running the command from within it, or transferring directly to your local "_build" folder. You can partially view the HTML within the docker container using a HTML preview extension but note that MathJax and internal book links won't work in this.

Warning: if you are building the dockerfile with the environment, it will take some time to build. There is a pre-built image available on Dockerhub [here](https://hub.docker.com/repository/docker/aeturrell/codingforeconomists/general).

There is a bug inbetween all the dependencies that sees a list index error arise. You can squish this manually by commenting out `token.children[1].content = token.children[1].content[3:]` in `"/opt/conda/envs/codeforecon/lib/python3.8/site-packages/mdit_py_plugins/tasklists/__init__.py"`, line 84, in todoify. However, the commenting out is done automatically by the Dockerfile. (Generally, there have been version issues between markdown-it-py, myst-nb, and myst-parser.) On a Mac, this line will likely be at `"/Users/USERNAME/opt/anaconda3/envs/codeforecon/lib/python3.8/site-packages/mdit_py_plugins/tasklists/__init__.py"`.

### Building the Book

To build the book using Jupyter books use

```bash
jupyter-book build .
```

Once this command is run, you should be able to look at the HTML files for the book locally on your computer.

Note that, due to package conflicts, several pages may not compile when taking this approach. One work around is to manually run troublesome notebooks and, when jupyter-book encounters a problem when executing them to build the book, it will pick up the notebook at the last point it was successfully manually executed. If you do have this problem, it may be that jupyter-book is not picking up the right jupyter kernel. You can look at installed kernels using `jupyter kernelspec list`.

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

### Command line version of python is incorrect

Deactivate the conda environment (until even the base environment is deactivated) using `conda deactivate`. Then activate your environment with `conda activate your_env_name_goes_here`.

### Special Fonts

This book uses some special fonts, such as Varta. If you install these manually, you may need to refresh your Matplotlib font cache before you can see the new fonts at work:

```bash
rm ~/.matplotlib/fontlist-v330.json
```