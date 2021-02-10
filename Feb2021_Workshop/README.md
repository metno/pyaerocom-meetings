# MET Norway Spring 2021 pyaerocom workshop

**Workshop theme:** running the web evaluation tools.

## About the workshop:

The focus of this workshop will be on setting up and running the web evaluation tools that feed the AeroVal website (https://aerocom-evaluation.met.no/).
As a result, an introduction into the general API of pyaerocom will be kept short.

#### Pre-remarks:

A basic knowledge of the Python programming language and git is highly recommended. It is beneficial to be familiar with common Python libraries such as numpy, pandas and scipy as well as libraries for reading of and working with model data (e.g. NetCDF4, iris, xarray). Further, it will be helpful to be familiar with jupyter notebooks.

It will also be very beneficial to be familiar with the conda python packaging manager (comes with installation of Anaconda or miniconda Python distributions).

## Participants and working groups

See here: https://docs.google.com/spreadsheets/d/1M1r18DE-7BEVBO077sWNfprlvppir3Exo6vikE2yCxo/edit#gid=0

## Agenda

See here: https://docs.google.com/document/d/1iGBjMBwvkqfdboJV5r2bOKv25NgSFs5i01G6Galt2vo/edit

## Preparations

It is highly recommended for each participant, to go through the following instructions before the workshop.

**Please do not hesitate** to contact us if something is unclear or does not work.

### Installing pyaerocom (assuming you use conda as package manager)

[conda ???](https://docs.conda.io/en/latest/)

The following command installs the latest pyaerocom release (and all requirements) into a new conda
environment ([conda environments ???](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)):

```bash
conda create -c conda-forge --name pya pyaerocom jupyterlab
```

After the installation is complete, activate the environment via:

```bash
conda activate pya
```

That's it.

### Getting started with pyaerocom

For a brief introduction into the technical setup and pyaerocom basic API see notebook [setup_and_intro.ipynb](https://github.com/jgliss/pyaerocom-meetings/blob/master/Feb2021_Workshop/setup_and_intro.ipynb).
