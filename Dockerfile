# DOCKERFILE for Coding for Economists
# Please note that you will need a lot of RAM dedicated to Docker to build this image (15Gb+, change this in your docker settings)

# Set base image (this also loads a Linux operating system)
FROM condaforge/mambaforge:23.3.1-1

WORKDIR /app

# Update Linux package list and install some key libraries, including latex
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get -y install openssl graphviz \
    nano texlive graphviz-dev \
    unzip

# Install special fonts
RUN mkdir -p /usr/share/fonts/truetype/
RUN wget https://www.wfonts.com/download/data/2015/10/08/varta/varta.zip
RUN unzip varta.zip
RUN install -m644 *.ttf /usr/share/fonts/truetype/
RUN rm *.ttf
RUN rm varta.zip

# change default shell from ash to bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

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
RUN python3 -m spacy download en_core_web_sm
RUN python3 -m nltk.downloader all

# Comment out the offending line in todoify
RUN sed -i '90 s/^/#/' /opt/conda/envs/codeforecon/lib/python3.10/site-packages/mdit_py_plugins/tasklists/__init__.py

# On Mac, this is going to be something like
# sed -i '90 s/^/#/' /Users/YOUR-USERNAME/mambaforge/envs/codeforecon/lib/python3.10/site-packages/mdit_py_plugins/tasklists/__init__.py

# Copy the current directory contents into the container at /app
COPY . /app

RUN echo "Success building the codeforecon container!"
