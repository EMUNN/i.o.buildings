from netCDF4 import Dataset
import pandas as pd
import numpy as np
import xarray as xr

data = Dataset('./barcelona_20181001-20181231_no2.nc', 'r')

# print(data)
# print(data.variables.keys())

columns = ['isValid', 'lat', 'lon', 'no2', 'numObs', 'precipitation', 'temperature', 'time', 'windU', 'windV']

#
# lats = nc_fid.variables['lat'][:]
# lons = nc_fid.variables['lon'][:]
# time = nc_fid.variables['time'][:]
no2 = data.variables['no2'][:]

print(no2)
