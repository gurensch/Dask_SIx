import time
from netCDF4 import Dataset
import numpy as np

def tempunits(inT):
    return (9./5)*inT+32

def open_nc(min_path, max_path, ens_begin, ens_eind):
    start_time = time.clock()
    nc_tn = Dataset(min_path, 'r')
    nc_tx = Dataset(max_path, 'r')
    mint = nc_tn.variables['tn'][:,ens_begin:ens_eind,90:,:]
    maxt = nc_tx.variables['tx'][:,ens_begin:ens_eind,90:,:]
    lat = nc_tn['latitude'][90:]
    mint = np.ma.getdata(mint)
    maxt = np.ma.getdata(maxt)
    lat = np.ma.getdata(lat)
    mint = np.where(mint <= -9999, np.nan, mint)
    maxt = np.where(maxt <= -9999, np.nan, maxt)
    mint = np.swapaxes(mint,0,1)
    mint = np.swapaxes(mint,1,2)
    mint = np.swapaxes(mint,2,3)
    maxt = np.swapaxes(maxt,0,1)
    maxt = np.swapaxes(maxt,1,2)
    maxt = np.swapaxes(maxt,2,3)
    mint = tempunits(mint)
    maxt = tempunits(maxt)
    print(time.clock() - start_time)
    return mint, maxt, lat
