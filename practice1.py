import netCDF4
import pandas as pd

nc_file = './barcelona_20180101-20180331_no2.nc'
nc = netCDF4.Dataset(nc_file, mode='r')

nc.variables.keys()

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
# no2 = nc.variables['no2'][:]

# a pandas.Series designed for time series of a 2D lat,lon grid
no2 = pd.Series(time_var, index=dtime)

no2.to_csv('./no2.csv',index=True, header=True)
