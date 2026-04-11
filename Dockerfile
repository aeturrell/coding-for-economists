# DOCKERFILE for Coding for Economists
# Please note that you will need a lot of RAM dedicated to Docker to build this image (15Gb+, change this in your docker settings)

# Set base image
FROM python:3.10-slim

WORKDIR /app

# Update Linux package list and install some key libraries
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get -y install openssl graphviz \
    nano texlive graphviz-dev \
    unzip wget curl build-essential

# Install special fonts
RUN mkdir -p /usr/share/fonts/truetype/
RUN wget https://www.wfonts.com/download/data/2015/10/08/varta/varta.zip
RUN unzip varta.zip
RUN install -m644 *.ttf /usr/share/fonts/truetype/
RUN rm *.ttf
RUN rm varta.zip

# change default shell from ash to bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies via uv
RUN uv sync --frozen

# Install NLP models
RUN uv run python3 -m spacy download en_core_web_sm
RUN uv run python3 -m nltk.downloader all

# Copy the current directory contents into the container at /app
COPY . /app

RUN echo "Success building the codeforecon container!"
