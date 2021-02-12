# MET Norway Spring 2021 pyaerocom workshop

Workshop theme: running the web evaluation tools.

## Participants and working groups

See here: https://docs.google.com/spreadsheets/d/1M1r18DE-7BEVBO077sWNfprlvppir3Exo6vikE2yCxo/edit#gid=0

## Agenda

See here: https://docs.google.com/document/d/1iGBjMBwvkqfdboJV5r2bOKv25NgSFs5i01G6Galt2vo/edit

## Technical setup

It is highly recommended for each participant, to go through the following instructions before the workshop.

**Please do not hesitate** to contact us if something is unclear or does not work.

### Install php on your local computer

```bash
sudo apt update
sudo apt install php
```

### Required GitLab / GitHub repositories

Please clone the following repositories into the same directory on your local computer:

#### pyaerocom-meetings repository:

```bash
git clone git@github.com:metno/pyaerocom-meetings.git
```

#### AeroVal Gitlab repositories

1. `web` repo (contains code for web rendering):

  ```bash
  git clone git@gitlab.met.no:aerocom-evaluation/web.git
  ```

2. `data` repo:

  ```bash
  git clone git@gitlab.met.no:aerocom-evaluation/data.git
  ```

3. workshop project submodule:

  To be cloned into `data` repo, so please clean `data first`. Then:

  ```bash
  cd data/json
  git clone SUBMODULE_URL
  ```

### Installing pyaerocom (assuming you use conda as package manager)

[conda ???](https://docs.conda.io/en/latest/)

The following command installs the latest pyaerocom release (and all requirements) + jupyterlab into a new conda
environment called pya ([conda environments ???](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)):


```bash
conda create -c conda-forge -n pya pyaerocom jupyterlab
```

After the installation is complete, activate the environment and open jupyter lab via:

```bash
conda activate pya
jupyter lab
```

That's it.

### Getting started with pyaerocom

For a brief introduction into the technical setup and pyaerocom basic API see notebook [setup_and_intro.ipynb](https://github.com/jgliss/pyaerocom-meetings/blob/master/Feb2021_Workshop/setup_and_intro.ipynb).
