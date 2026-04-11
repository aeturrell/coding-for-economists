# Coding for Economists

[![DOI](https://zenodo.org/badge/316842103.svg)](https://zenodo.org/doi/10.5281/zenodo.10465358)  ![GitHub Release](https://img.shields.io/github/v/release/aeturrell/coding-for-economists)

To read or use the book, head to the [*Coding for Economists* website](https://aeturrell.github.io/coding-for-economists/intro.html).

The rest of this readme is intended to help those who are contributing to the book, rather than readers.

## Dev

These instructions are only for developers working on the book.

### Making Changes

Contributions to *Coding for Economists* are welcome! If you're planning to make a pull request, lodge an issue to discuss it first but feel free to go straight to making a pull request for corrections, typos, and fixing out of date package issues.

Prerequisites:

- installation of `uv`
- Natural language processing models: within the Python environment, you will need to run `uv run python -m spacy download en_core_web_sm` to download the spacy model, and `uv run python3 -m nltk.downloader all` for the **nltk** models.
- Fonts: The book uses some special fonts, such as Varta, which you can find on Google fonts.
- LaTeX: The book was built with TeX Live.

You can see how to complete all of these steps programmatically by looking at how the Dockerfile does it.

To make changes:

1. create a new branch
2. install the Python environment or alternatively build and work in the docker image (which comes with the Python environment)
3. make your content changes, amending the Python environment as necessary (eg add packages via `uv add <packagename>`)
4. Check your changes look right with `uv run quarto render --execute` to render the book, and `uv run python -m http.server -d _book 8000` to read it locally
5. run pre-commit using `uv run pre-commit run --all-files`
6. if the checks clear, commit your change(s) 
7. make a pull request

Your pull request will then be reviewed by an admin.

### Using the docker image

There is a Dockerfile for the environment, which is the easiest way to set up a dev env. You run it by following these steps:

1. Ensure you have docker, the docker extension for VS Code, and the VS Code remote extension installed
2. In VS Code, right-click on the Dockerfile and hit "build image". Switch to the docker tab and hit "Run interactive". Switch to the VS Code Remote tab, then click "Attach in new window" on the running container.
3. Once you are in the container via VS Code remote, you may need to install the Python extension (within the container version of VS Code).
4. Open up the relevant folder, "app", in VS Code remote. It's usually in `../app`.
6. To ping back the built HTML files, use `docker cp running-container-name:app/_book/ .` from your local command line (not the docker container) within the folder where you want to move all of the build files. You could transfer to a local "_book" folder. You can partially view the HTML within the docker container using a HTML preview extension but note that MathJax and internal book links won't work.

### Building the book

To build the book locally with all the content executed use:

```bash
uv run quarto render --execute
```

### Uploading Built Files

You should not need to upload built files manually as there are GitHub Actions that auto build and auto publish when there's a new release. Sometimes it is useful to republish locally, however. Once you have successfully rendered the entire book with no errors, the publish command is

```bash
uv run quarto publish
```

### Special Fonts (Gotcha)

This book uses some special fonts, such as Varta. If you install these manually, you may need to refresh your Matplotlib font cache before you can see the new fonts at work:

```bash
rm ~/.matplotlib/fontlist-v330.json
```

## Creating a release

There's a GitHub Action set up to help with releases (a release is a new version of the book). These are the steps:

- Open a new branch with the new version name
- Change the version in `pyproject.toml`
- Commit the change with a new version label as the commit message (checking the tests pass)
- Head to GitHub and (create a pull request and) merge into main (assuming tests etc pass)
- A new release should be automatically drafted based on that most recent merge commit, and it should use the new version as the tag
- The new release should automatically be published on GitHub
- A new version of the book should automatically be uploaded
- The Zenodo repository and version badge on the intro page will update automatically

This process should mean the releases and the uploaded website (on GitHub pages) should be consistent
