# Run the evaluation on PPI

There are two main reasons for preferring to run your evaluation on PPI instead of your local machine, transfer time over the network and memory. Some model files are very large and transferring all that data over the network is a significant time sink. Some observational data sets ar eso large that the memory on your laptop becomes a limiting factor. In these cases you need to run the analysis on PPI.

## Log in to PPI
Remember that you have to be on the VPN
```
$ ssh -X <username>@xvis-m4a
```

After logging in, activate the module with pyaerocom installed and activate the `pya` envirnoment in conda:

```
$ module load aerocom/anaconda3-stable
$ conda activate pya
```

## "Duplicate" the setup on your local machine
Select a location where you have read and write access on lustre and clone the `web` and `data` like you did for your local setup:

```
$ git clone https://gitlab.met.no/aerocom-evaluation/web.git
$ git clone https://gitlab.met.no/aerocom-evaluation/data.git

$ cd data/json
$ git clone https://gitlab.met.no/aerocom-evaluation/workshop2021.git
```
## Running the valuation on PPI
In the `data` repository there is a config file version of the simple setup from the notebook you saw earlier (also copied below) called `cfg_webeval_on_ppi.py`

This particular setup is light enough that i can be run on the login node of PPI. For a heavier setup you need to request a compute node. The easiest way is with the `qlogin` command:
```
$ qlogin -pe mpi 1 -q ded-parallelx.q -l h_vmem=30G -l h_rt=1:00:00
```
Here `-pe mpi 1` tells `qlogin` that we want one one processor and `-q ded-parallelx.q` is the queue we want to use (different options are available here including `research-bionic.q` and `research-el7.q` etc. with slightly different setups). The other options tells the machine we want 30 GB og memory and that the process is allowed to run for a maximum of 1 hour.

After running the `qlogin` command, we get a new login prompt asking for username and password. After logging in we are on a compute node. It look like this
```
<username>@c6220ii-4pz1zz1-ao-compute:
```
If you are inactive for too long here you get kicked out, so if you need to think about what to do run `tail -f`. This does nothing, but the machine thinks you are doing something. Activate the pyaerocom envirnoment. If you do this often I recommend adding these commands to your `/home/<username>/.bashrc` file so it is set up automatically every time you log in.

```
$ module load aerocom/anaconda3-stable
$ conda activate pya
```
Move to where you cloned the `web` and `data` repositories and go to config files:
```
$ cd data/config_files
```
If everything is set up correctly you can run the config file using python now:
```
$ python cfg_webeval_on_ppi.py
```
## Visualizing the results
Since we have mounted PPI on our machines we can navigate to the `web` repository directory from our local machine and run the local web server. For me it looks like this when I'm in $HOME:
```
<username>@laptop:~$ cd lustre/storeA/project/fou/kl/CAMS61/pyaerocom_Feb21_meeting/web/

$ php -S localhost:8000
```

## Some tips
1. Since you have mounted PPI locally the easiest way to transfer config files from your local work space to PPI is to just copy them.
2. If you want you can open your PPI config files using spyder or your preferred editor on you laptop to do changes.
3. You can even run/debug your remote files on your laptop (with a performance hit).

## Config file
```python
import os
import pyaerocom as pya
pya.__version__

# Output directory (where json files are stored): NOTE: this should point to the *data* Gitlab repo that you should have cloned
OUT_BASEDIR = os.path.abspath('../../data/json/')

# ID of project (please use this ID, as this is linked with the URL later on and will make sure to write into the correct GitLab repo, under data/json/{PROJ_ID})
# IMPORTANT NOTE: for the workshop, please all use this project ID
PROJ_ID = 'workshop2021'

# ID of experiment (will be name of subdirectory under data/json/{PROJ_ID}/{EXP_ID}) and used for experiment navigation in the web interface.
# IMPORTANT NOTE: PLEASE CHANGE THIS FOR YOUR OWN EXPERIMENT (e.g. Group1, Group2, ...)
EXP_ID = 'example1'

# Directory where colocated NetCDF files are stored (this is not relevant for the website, so it can be set flexibly)
COLDATA_BASEDIR = os.path.abspath('./coldata')

stp = pya.web.AerocomEvaluation(proj_id=PROJ_ID, exp_id=EXP_ID, 
                                exp_name='Tutorial experiment for pyaerocom workshop',
                                out_basedir=OUT_BASEDIR,
                                basedir_coldata=COLDATA_BASEDIR)
# print(stp)

obs_cfg = {
    # key is name as it appears in web interface, value contains setup 
    'Aeronet' : {
        'obs_id'        : 'AeronetSunV3Lev2.daily', # ID of obsnetwork
        'obs_vars'      : ['ang4487aer', 'od550aer'], # list of variables (Angstrom Exponent, 440-870nm, and AOD at 550 nm)
        'obs_vert_type' : 'Column', # this is needed, choose from Column or Surface
        'obs_filters'   : {'altitude' : [0, 1000]},
        'ignore_station_names' : 'DRAGON*'
    }
}

stp['obs_config'] = obs_cfg



model_cfg = {
    'Aerocom-Median' : {'model_id' : 'AEROCOM-MEDIAN-2x3-GLISSETAL2020-1_AP3-CTRL'},
    'EC-Earth'    : {'model_id' : 'EC-Earth3-AerChem-met2010_AP3-CTRL2019'}
}

stp['model_config'] = model_cfg

DEFAULT_COLOCATION_SETTINGS = dict(
    start = 2010, 
    stop = 2011,
    ts_type = 'daily', # desired output frequency of colocated data objects
    colocate_time = False, # if True and if input "ts_type" is lower resolution than highest available in model and obs, then model and obs are first colocated in higher res. before resampling to "ts_type"
    weighted_stats = True, # only relevant if models are evaluated against gridded satellite data
    apply_time_resampling_constraints = True,
    min_num_obs = pya.const.OBS_MIN_NUM_RESAMPLE,
    reanalyse_existing = True, # relevant for re-runs. If True, pre-existing colocated data files are re-used for computation of json files 
    remove_outliers=True, # remove outliers during colocation
    harmonise_units=True, # harmonise units before colocation (e.g. if obs is in ug m-3 and model is in kg m-3). Will crash if unit conversion cannot be done (e.g. obs in ug m-3 and model in nmole mole-1).
    model_keep_outliers=True, # if True, and remove_outliers is True, then only obs outliers are removed  (default behaviour)
)

stp.update(**DEFAULT_COLOCATION_SETTINGS)

stp.var_mapping = pya.web.web_naming_conventions.VAR_MAPPING

stp.run_evaluation()
```
