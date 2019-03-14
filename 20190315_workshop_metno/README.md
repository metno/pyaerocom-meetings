# pyaerocom workshop at Norwegian Meteorological Institute

Date: 15/03/2019  

Time: 09:00 - 16:00  

Agenda: See [here](https://github.com/jgliss/pyaerocom-meetings/blob/master/20190315_workshop_metno/Agenda_pyaerocom_WS_20190315.pdf)  

## Course notebooks

jupyter notebooks used in this workshop can be found in the [notebooks](https://github.com/jgliss/pyaerocom-meetings/tree/master/20190315_workshop_metno/notebooks) directory.

## More information about pyaerocom

- Website: https://pyaerocom.met.no/
- GitHub: https://github.com/metno/pyaerocom

## Setup

Participants are supposed to log on to PPI and load the python environment

### Log in to PPI

`$ ssh -A xvis-m4a.met.no`

### Clone or update this repository

`$ git clone https://github.com/jgliss/pyaerocom-meetings.git`

#### Or (if you have it cloned already)

`$ cd pyaerocom-meetings`  
`$ git pull`

#### Navigate into workshop directory

`$ cd 20190315_workshop_metno`

### Load the python conda environment that has pyaerocom installed

Activate pyaerocom-master module on PPI.

`module load aerocom/aerocom-pyaerocom-master`

### Start jupyter lab

After activating the pyaerocom environment, open jupyter lab using the following command:

`jupyter lab --no-browser --ip=$HOSTNAME.met.no`

If the browser does not automatically open the jupyter lab app in your browser, right click on the displayed URL and open the link.

### Run the notebooks

From within jupyter lab, navigate to the jupyter notebooks (.ipynb files) in the notebooks directory run it.
