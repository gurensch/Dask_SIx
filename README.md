# Dask_SIx
Dask implementation of the extended spring indices (SI-x model)

This repository shows the Python scripts that are employed to get the phenology and false spring data for the MSc thesis 'Exploring vegetation seasonality at large scale and determining its uncertainty. A case study with ensemble weather data and the extended spring indices". The data that is used in this study is the [E-OBS full ensemble dataset](https://www.ecad.eu/download/ensembles/download.php), which can be acquired on request. The following steps are recommended:
1. Load the modules:
import time
from netCDF4 import Dataset
import numpy as np
import xarray as xr
from dask.distributed import as_completed
2. Load the minmum and maximum temperature data in a Python environment. I used the open_nc.py script, though this is suited only for the E-OBS full ensemble dataset configuration. The output of this step should be the loaded temperature data that fits the internal memory of the device that is used. In this study, 10 ensemble members were loaded each time the function is called (see calc_si.py). The configuration of the loaded data should be two 4D temperature arrays for minimum temperature and maximum temperature with the following dimensions: [ensemble_member, latitude, longitude, days]. Furthermore, an 1D array of all the latitudes should be created. Note that this study employed the full 100 member ensemble of temperature data. Commonly, the first axis of the 4D array will be "years". 
3. Once the temperature arrays and latitude array are loaded in the Python environment
