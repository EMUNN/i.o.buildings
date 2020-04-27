import netCDF4
import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

DS = xr.open_dataset('./barcelona_20181001-20181231_no2.nc')

# print(no2)

test = DS.no2.isel(time=0)

# da = DS.no2.sel(lat=1, lon=1, method='nearest')
# da = da.sel(time=slice('2018-03-31T10:00:00','2018-03-31T23:00:00'))



# da.plot.line(x='time')
# no2 = nc.variables['no2'][:]

print(test)
