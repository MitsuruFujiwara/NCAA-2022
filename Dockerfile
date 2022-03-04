FROM ubuntu:20.04

#==============================================================================
# Global
#==============================================================================

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

#==============================================================================
# System
#==============================================================================

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:git-core/ppa

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    cmake \
    build-essential \
    gcc \
    g++ \
    curl \
    wget \
    unzip \
    git

#==============================================================================
# Conda
#==============================================================================

ARG CONDA_DIR=/opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

RUN curl -sL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o conda.sh && \
    /bin/bash conda.sh -f -b -p $CONDA_DIR && \
    export PATH="$CONDA_DIR/bin:$PATH"  && \
    conda config --set always_yes yes --set changeps1 no

RUN pip install --upgrade pip

#==============================================================================
# LightGBM
#==============================================================================

RUN git clone --recursive --branch stable --depth 1 https://github.com/Microsoft/LightGBM && \
    cd LightGBM/python-package && python setup.py install && \
    # clean
    apt-get autoremove -y && apt-get clean && \
    conda clean -a -y && \
    rm -rf /usr/local/src/*

#==============================================================================
# Google Chrome
#==============================================================================

RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /tmp/google-chrome-stable_current_amd64.deb && \
    dpkg -i /tmp/google-chrome-stable_current_amd64.deb || \
    (apt -f install -y && dpkg -i /tmp/google-chrome-stable_current_amd64.deb) && \
    rm -f /tmp/google-chrome-stable_current_amd64.deb

RUN pip install chromedriver-binary-auto

#==============================================================================
# SQL
#==============================================================================

RUN pip install PyMySQL SQLAlchemy

#==============================================================================
# Other Libraries
#==============================================================================

RUN pip install jpholiday lxml more_itertools
RUN conda install -q -y numpy scipy scikit-learn jupyter notebook ipython pandas matplotlib bs4 seaborn html5lib
RUN conda install -y -c conda-forge feather-format selenium optuna

#==============================================================================
# System CleanUp
#==============================================================================

RUN apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    conda clean -a -y