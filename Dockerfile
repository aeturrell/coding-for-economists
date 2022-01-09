# DOCKERFILE for Coding for Economists
# Please note that you will need a lot of RAM dedicated to Docker to build this image (15Gb+, change this in your docker settings)

# Set base image (this also loads the Alpine Linux operating system)
FROM continuumio/miniconda3:4.10.3-alpine

WORKDIR /app

# Update Linux package list and install some key libraries, including latex
RUN apk update && apk add openssl graphviz \
    nano texlive alpine-sdk build-base graphviz-dev \
    bash

# change default shell from ash to bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

# Install mamba
RUN conda install mamba -n base -c conda-forge

# Ensure pip's setuptools is latest
RUN pip install --upgrade setuptools wheel

# Create the environment:
COPY environment.yml .
# Install everything at once:
RUN mamba env create -f environment.yml
# Do a debug or incremental env install (builds in under 3 min):
# RUN mamba create -n codeforecon -c conda-forge python=3.8 pyyaml rich numpy spacy -y

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "codeforecon", "/bin/bash", "-c"]

RUN mamba list

# Install NLP models
RUN python3 -m spacy download en
RUN python3 -m nltk.downloader all

# Comment out the offending line in todoify
RUN sed -i '84 s/^/#/' /opt/conda/envs/codeforecon/lib/python3.8/site-packages/mdit_py_plugins/tasklists/__init__.py

# Copy the current directory contents into the container at /app
COPY . /app

RUN echo "Success building the codeforecon container!"
