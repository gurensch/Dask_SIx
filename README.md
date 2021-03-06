# Dask implementation of the extended spring indices (SI-x model)


This repository shows the Python scripts that are utilized to get the phenology and false spring data for the MSc thesis 'Exploring vegetation seasonality at large scale and determining its uncertainty. A case study with ensemble weather data and the extended spring indices". The data that is used in this study is the [E-OBS full ensemble dataset](https://www.ecad.eu/download/ensembles/download.php), which can be acquired on request. Special thanks to Theresa Crimmins, Jeff Switzer and Lee Marsh for facilitating re-use of the optimized SI-x model and Serkan Girgin for assisting with the Dask implementation. The following steps are recommended:
1. Load the minimum and maximum temperature data in a Python environment. I used the open_nc.py script, though this is suited only for the E-OBS full ensemble dataset configuration. The output of this step should be the loaded temperature data that fits the internal memory of the device that is used. In this study, 10 ensemble members were loaded each time the function is called (see calc_si.py). The configuration of the loaded data should be two 4D temperature arrays for minimum temperature and maximum temperature with the following dimensions: [ensemble_member, latitude, longitude, days]. Furthermore, an 1D array of all the latitudes should be created. Note that this study employed the full 100-member ensemble of temperature data. Commonly, the first axis of the 4D array will be "years". 
2. Once the temperature arrays and latitude array are loaded in the Python environment, the functions optimized_model.py and run_batches.py must be run. 
3. Lastly, the calc_si.py function can be run to get the spring onset and last freeze arrays. The range must be adjusted to represent the number of years or ensemble members in the temperature dataset. Furthermore, the fourth command in the run_batches statement may need to be adjusted to make sure that the number of latitudes in the dataset is divisible by the number that is stated. Preferably, the number should not deviate too much from 5. 

# Authors

MSc student Geographical Information Management and Applications (Utrecht University):

Rens Vermeltfoort: rensvermeltfoort@gmail.com


Professor/Supervisor Faculty Geo-Information Science and Earth Observation (University of Twente):

Raul Zurita-Milla: r.zurita-milla@utwente.nl
