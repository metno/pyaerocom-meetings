# MET Norway Spring 2021 pyaerocom workshop

## Preparations

Please see [technical setup](https://github.com/metno/pyaerocom-meetings/tree/master/Feb2021_Workshop#technical-setup) below.


## Participants and working groups

See here: https://docs.google.com/spreadsheets/d/1M1r18DE-7BEVBO077sWNfprlvppir3Exo6vikE2yCxo/edit#gid=0

## Agenda

See here: https://docs.google.com/document/d/1iGBjMBwvkqfdboJV5r2bOKv25NgSFs5i01G6Galt2vo/edit

## Technical setup

It is highly recommended to go through the following instructions before the workshop.

**Please do not hesitate** to contact us if something is unclear or does not work.

### Install php on your local computer

This is needed to run a local version of the [AeroVal](https://aerocom-evaluation.met.no/) web interface.

```bash
sudo apt update
sudo apt install php
```

### Required GitLab / GitHub repositories

Please clone the following repositories into the same directory on your local computer:

#### pyaerocom-meetings repository:

```bash
git clone https://github.com/metno/pyaerocom-meetings.git
```

#### AeroVal Gitlab repositories

**NOTE**: you need to be connected via VPN to be able to access the following GitLab repos:

1. `web` repo (contains code for web rendering):  
  ```bash
  git clone git@gitlab.met.no:aerocom-evaluation/web.git
  ```

2. `data` repo:  
  ```bash
  git clone git@gitlab.met.no:aerocom-evaluation/data.git
  ```

3. `workshop2021` project submodule:  
  This is to be cloned into `data` repo, so please clean `data` first. Then:  
  ```bash
  cd data/json
  git clone git@gitlab.met.no:aerocom-evaluation/workshop2021.git
  ```

### Mount PPI locally

In order to work locally, you will need to have access to the model and obs data on lustre (storeA and / or storeB). When pyaerocom is imported it will try to see if lustre is mounted, either in root `/` or in the user home `~` directory. Thus, it is recommended to mount `/lustre/storeA` and / or `/lustre/storeB` into your home directory `~`. To do that, you have 2 options:

#### If you have sudo rights on your laptop:

The recommended way is to use the following command(s) to mount storeA and / or storeB locally:

```bash
cd 
mkdir lustre
mkdir lustre/storeA
mkdir lustre/storeB
sudo mount -t cifs //cifs-int-gw-a.met.no/storeA lustre/storeA -o username=<username>
sudo mount -t cifs //cifs-int-gw-b.met.no/storeB lustre/storeB -o username=<username>
```

#### Without sudo rights:

If you do not have sudo rights, you can mount via sshfs command: 

```bash
cd 
mkdir lustre
sshfs <username>@xvis-m4a:/lustre lustre
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

#### Installing latest development version of pyaerocom

**NOTE**: this is only relevant for those who want to use recently developed features of pyaerocom, which are not included in the latest official release.

The standard installation will install the latest release of pyaerocom, which corresponds roughly to Nov 2020. If you want to use the latest developments from any of the development branches, you need to install pyaerocom from source. To install a development version of pyaerocom into a new conda environment (named `pyadev`) you can do the following (here, the `main-dev` branch is installed):

```bash
git clone git@github.com:metno/pyaerocom.git
cd pyaerocom
git checkout main-dev
conda env create -n pyadev -f pyaerocom_env.yml
python setup.py install
```

## Getting started - Example notebooks

This folder contains the following example notebooks, which will also be discussed during the workshop, but feel free to take a look, in order to test your technical setup.

- **setup_and_intro.ipynb**: Introduction into technical setup, pyaerocom API and co-location routines (**uses data located on PPI via VPN**).
- **example_webeval.ipynb**: Introduction into web evaluation tools including minimal example experiment (**uses data located on PPI via VPN**).
- **example_webeval_local.ipynb**: (COMING SOON) Introduction into web evaluation tools including minimal example experiment (**uses data located on local machine**).

## Speedup - create a local copy of relevant obsdata 

**NOTE:** this will require 20GB of disk space on your computer (or on an external disk)!

We prepared a copy of EBAS, GHOST and AERONET data in a tarball, which you can download to speedup reading of obsdata (which is slow via VPN, i.e. if you use a local pyaerocom installation). The tarball is available at `/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/PYAEROCOM/ws21_19GB.tar.gz`. You may use the following commands to download and and extract the data into a local directory of your choice (here ~/MyPyaerocom is used):

```bash
cd ~/MyPyaerocom
rsync -av <username>@xvis-m4a:/lustre/storeA/project/aerocom/aerocom1/AEROCOM_OBSDATA/PYAEROCOM/ws21_19GB.tar.gz .
tar -xzvf ws21_19GB.tar.gz
rm -r ws21_19GB.tar.gz
```
The extracted directory contains sub-directories for AERONET, EBAS and GHOST data. Note that GHOST is only available for 2018 and 2019.
