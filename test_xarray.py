
import xarray as xr
import os

print("isel - select based on index, sel() - select based on location sel(lat=33, long=77)")
print("latitude = y coordinate, longitude is x coordinate")
print("sel() method has a method parameter which can be set to nearest which will get data closest to point passed")
print(".plot(robust=True) -> This will remove outliers when drawing a map so you can see more detail")
# This is a VIL file from work
netcdf_file = "/TEST_DATA/WX/ciws/VIL/2019/0202/20190202_v_024230_l_0000000.nc"

if not os.path.exists(netcdf_file):
    print("This file does not exist: %s" % netcdf_file)

# added mask_and_scale to get rid of multiple values warning
ds = xr.open_dataset(netcdf_file, engine="netcdf4", mask_and_scale=False)
#print(ds)   # print whole structure of file
#print(ds.info())  # print information similar to ncdump -h
#print("DIMS: ", ds.dims)    # dimensions (next line)
# Frozen({'x0': 5120, 'y0': 3200, 'z0': 1, 'time': 1, 'DataIngestTimeDim': 1,
#   'ipAndFilenameAndTimeDim': 3, 'DataSubsetTimeDim': 1, 'ipAndSubsetTimesDim': 4})
#print("X = %s" % ds.dims["x0"])   # print only x indicies
#print(ds.data_vars)  # Should see "VIL" in there
# Can access all x/y values
#print(ds.x0.data)
#print(ds.y0.data)

the_attrs = ds.attrs
#print(the_attrs)
# {'FileFormat': 'Netcdf4', 'Conventions': 'CF-1.4',
#   'history': 'File created 2019-02-02T02:42:37Z on machine ciwsa071 by ProductAdapterVIL 1.0.0',
#   'institution': 'Data produced by the MIT Lincoln Lab Weather Sensing Group',
#   'references': 'http://www.wx.ll.mit.edu', 'source': 'CIWS National Data Stream: MosTileAsm:Mosaic:CiwsRelay',
#   'title': 'CIWS National VIL Mosaic Product - 1 km @ 2.5 minutes',
#   'comment': 'Precip (VIL) derived from mosaic of NEXRAD, TDWR and Canadian radar systems.',
#   'FileType': 'NetCDF', '_CoordSysBuilder': 'ucar.nc2.dataset.conv.CF1Convention'}

#print(ds.coords)
'''
Coordinates:
  * x0       (x0) float64 -2.56e+06 -2.558e+06 -2.558e+06 ... 2.558e+06 2.56e+06
  * y0       (y0) float64 -1.542e+06 -1.542e+06 ... 1.656e+06 1.656e+06
  * z0       (z0) float64 0.0
  * time     (time) datetime64[ns] 2019-02-02T02:42:3
'''
x_values = ds.coords['x0'].values
y_values = ds.coords['y0'].values
time_values = ds.coords['time'].values
vil_values = ds["VIL"]  # This is a DataArray

# Use zip to work with the dimensions together (works only with two dimensions)
# for x,y in zip(x_values, y_values):
#     print("(%d, %d)" % (x, y))
print ("Sizes: X: %d, Y: %d, T: %d" % (len(x_values),len(y_values),len(time_values)))
# netCDF4 lib: print(vil[0][0][2694][3531]) => 0.05371257667775506 (22)
the_value = vil_values[0][0][2694][3531].data
print(type(the_value))
print(the_value, the_value*vil_values.attrs["scale_factor"])
# Prints: 22 0.05371257667775506, this matches the same index using Netcdf lib

# file: "/TEST_DATA/WX/ciws/VIL/2019/0202/20190202_v_024230_l_0000000.nc"

'''
print(ds["VIL"])   # VIL is the data variable we want 
<xarray.DataArray 'VIL' (time: 1, z0: 1, y0: 3200, x0: 5120)>
[16384000 values with dtype=int16]
Coordinates:
  * x0       (x0) float64 -2.56e+06 -2.558e+06 -2.558e+06 ... 2.558e+06 2.56e+06
  * y0       (y0) float64 -1.542e+06 -1.542e+06 ... 1.656e+06 1.656e+06
  * z0       (z0) float64 0.0
  * time     (time) datetime64[ns] 2019-02-02T02:42:30
Attributes:
    standard_name:        atmosphere_cloud_liquid_water_content
    long_name:            Vertically integrated liquid water (VIL)
    class_name:           VIL
    product_name:         VIL
    ancillary_variables:  VIL_FLAGS PRECIP_PHASE
    units:                kg m-2
    grid_mapping:         grid_mapping0
    scale_factor:         0.0024414807580797754
    add_offset:           0.0
    valid_range:          [    0 32767]
    _ChunkSize:           [   1    1 1760 2560]
    missing_value:        -32768
    _FillValue:           -1
'''