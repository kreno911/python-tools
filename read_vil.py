from netCDF4 import Dataset
import numpy as np

def get_vil_value(v):
    avil_value = -1
    if value > 0.0:
        if v >= 13574:
            avil_value = 6
        elif v >= 4977:
            avil_value = 5
        elif v >= 2900:
            avil_value = 4
        elif v >= 1448:
            avil_value = 3
        elif v >= 317:
            avil_value = 2
        elif v >= 58:
            avil_value = 1
    return avil_value
ds = Dataset("/TEST_DATA/WX/ciws/VIL/2019/0202/20190202_v_024230_l_0000000.nc", "r", format="NETCDF4")
#print(ds.variables)
#print(ds.dimensions)
# Print what is available for DS
print(ds.__dict__.keys())
# Print individual item
print(ds.__getattr__("comment"))

# for dim in ds.dimensions.values():
#    print(dim)
#print(ds.dimensions['time'])

vars = ds.variables
# for var in vars.values():
#     print("Var: ", var)

x0 = vars.get('x0')
#print(x0[0])   # Print first index of the lat array
y0 = vars.get('y0')
t0 = vars.get('time')
# list = d[:]  # Returns a shallow copy of the whole list which mean in this case, just the values.
#               It does not mean anything for scalar values like we have here, only compound objs.
# Mapping var contains a bunch of info about the projection and miscel stuff
mapping = vars.get('grid_mapping0')
print("Earth Radius: %d, %s, Origin(%f, %f)" % (mapping.earth_radius, mapping.long_name,
                                        mapping.latitude_of_projection_origin,
                                        mapping.longitude_of_projection_origin))
# Time stuff
#print(t0)  # Print whole time structure
#print(t0.shape)   # Not sure what this one is
print("Time long name: ", t0.long_name)   # Product validity time
print("string: ", t0.string)              # 2019-02-02T02:42:30Z
print("Timestamp: ", int(t0[0]))          # 1549075350

# Get the VIL structure
vil = vars.get("VIL")
#print(vil)
#data = vil[:]

cnt = 0
vil_value = -1
# Look at this in panopoly to see the real coords value..
print("Length: ", len(x0), len(y0), x0[0], y0[0])  # -2559500.0 -1542500.0
the_value = vil[0][0][2694][3531]
print("Value at (3531,2694):", the_value, "With scale factor: %d" % (the_value/vil.scale_factor))
# for ixx in range(len(x0)):
#     for iyy in range(len(y0)):
#         for value in vil[0][iyy][ixx]:
#             cnt += 1
#             vil_value = get_vil_value(value / vil.scale_factor)
#             if vil_value > 0.0:
#                 print("VIL: %d" % vil_value, "(%d,%d)" % (x0[ixx], y0[iyy]), "(%d)" % int(value/vil.scale_factor))
print("Total %d" % cnt)

ds.close()

# Very good read: https://www.earthinversion.com/utilities/reading-NetCDF4-data-in-python/
# https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f
'''
print(vil)
<class 'netCDF4._netCDF4.Variable'>
int16 VIL(time, z0, y0, x0)
    standard_name: atmosphere_cloud_liquid_water_content
    long_name: Vertically integrated liquid water (VIL)
    class_name: VIL
    product_name: VIL
    ancillary_variables: VIL_FLAGS PRECIP_PHASE
    units: kg m-2
    grid_mapping: grid_mapping0
    scale_factor: 0.0024414807580797754
    add_offset: 0.0
    valid_range: [    0 32767]
    _ChunkSize: [   1    1 1760 2560]
    missing_value: -32768
    _FillValue: -1
unlimited dimensions: 
current shape = (1, 1, 3200, 5120)   <- shows size of each dimension and position 
filling off
'''