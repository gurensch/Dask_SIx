import xarray as xr

tn_path_ensemble = r'C:\Users\Rens\Documents\GIMA\Thesis\eobs_data\tn_ensemble_master_2013.nc'
tx_path_ensemble = r'C:\Users\Rens\Documents\GIMA\Thesis\eobs_data\tx_ensemble_master_2013.nc'

#function to convert Celcius to Fahrenheit
def tempunits(inT):
    return (9./5)*inT+32

#function for getting the correct array setup for model input
def xarray_ensemble(path, lonmin, lonmax, latmin, latmax): 
    data = xr.open_dataarray(path, chunks={'latitude':50,'longitude':50, 'ensemble':1})
    data = data.sel(latitude=slice(latmin,latmax))
    data = data.sel(longitude=slice(lonmin,lonmax))
    data = data.transpose('ensemble', 'latitude', 'longitude', 'time')
    data = tempunits(data)
    latitude = data.latitude.values
    return data, latitude

mint, lat = xarray_ensemble(tn_path_ensemble, -25, 45, 34, 71.5) #full coverage
maxt, lat = xarray_ensemble(tx_path_ensemble, -25, 45, 34, 71.5) #full coverage

min_slice, lat_slice = xarray_ensemble(tn_path_ensemble, 10, 12, 50, 52) #part of germany for tests
max_slice, lat_slice = xarray_ensemble(tx_path_ensemble, 10, 12, 50, 52) #part of germany for tests