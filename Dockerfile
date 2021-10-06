# Set base image (this also loads the Debian Linux operating system)
FROM python:3.8.12-buster

# Update Linux package list and install some key libraries for compiling code
RUN apt-get update && apt-get install -y gcc libffi-dev \
    g++ libssl-dev openssl build-essential graphviz \
    libgdal-dev libgeos-dev libproj-dev proj-data proj-bin

# Install Latex
RUN apt-get --no-install-recommends install -y texlive-latex-extra

# Ensure python points to this version of Python
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 12
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.8 12

# ensure local python is preferred over any built-in python
ENV PATH /usr/local/bin:$PATH

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# set the working directory in the container
WORKDIR /app

# Copy only packages to cache them in docker layer
COPY pyproject.toml /app/

# Install the packages
RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Copy the current directory contents into the container at /app
COPY . /app
