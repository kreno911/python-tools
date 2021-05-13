from netCDF4 import Dataset

ds = Dataset("/TEST_DATA/WX/ciws/VIL/2019/0202/20190202_v_024230_l_0000000.nc", "r", format="NETCDF4")
#print(ds.variables)
#print(ds.dimensions)
# Print what is available for DS
print(ds.__dict__.keys())
# Print individual item
print(ds.__getattr__("comment"))

#for dim in ds.dimensions.values():
#    print(dim)
#print(ds.dimensions['time'])

for var in ds.variables.values():
    print(var)

ds.close()
