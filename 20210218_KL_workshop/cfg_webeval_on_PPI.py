#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:34:10 2021

@author: hansb
"""



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

# stp['obs_config'] = obs_cfg



model_cfg = {
    'Aerocom-Median' : {'model_id' : 'AEROCOM-MEDIAN-2x3-GLISSETAL2020-1_AP3-CTRL'},
    'EC-Earth'    : {'model_id' : 'EC-Earth3-AerChem-met2010_AP3-CTRL2019'}
}

# stp['model_config'] = model_cfg

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
