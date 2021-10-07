# Set base image (this also loads the Alpine Linux operating system)
FROM continuumio/miniconda3:4.10.3-alpine

WORKDIR /app

# Update Linux package list and install some key libraries, including latex
RUN apk update && apk add openssl graphviz \
    nano texlive

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml
# for debugging (builds in under 1 min)
# RUN conda create -n codeforecon python=3.8

# Make RUN commands use the new environment:
RUN echo "conda activate codeforecon" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Copy the current directory contents into the container at /app
# COPY . /app
