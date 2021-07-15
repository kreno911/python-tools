import pandas as pd
import random
import pyarrow.parquet as pq
from pyarrow.parquet import ParquetFile

def handle_large_parquet():
    print("Testig large parquet...")
    the_file = "/TEST_DATA/parquet/large-sbss-flight_track.parquet"
    pfile = pq.read_table(the_file)
    print("Column names: {}".format(pfile.column_names))
    #df = pd.read_parquet(the_file)
    #print("Column names: {}".format(df.column_names))
    #positions = df['position'].tolist()
    #print(len(positions))
def handle_small_parquet():
    print("Testig small parquet...")
    the_file = "/TEST_DATA/parquet/small-tonyg.parquet"
    # read_table creates pyarrow table
    # https://arrow.apache.org/docs/python/parquet.html#reading-and-writing-single-files
    pyarrow_table = pq.read_table(the_file)
    print("Column names: {}".format(pyarrow_table.column_names))
    df = pyarrow_table.to_pandas()
    # ['times_timestamp', 'flightState_location_latitude',
    #               'flightState_location_longitude', 'masked_flightid']
    # Grab all lats and longitudes and print
    lats = df['flightState_location_latitude'].tolist()
    longs = df['flightState_location_longitude'].tolist()
    print("Sizes: (%d, %d)" % (len(lats),len(longs)))
    # Pandas print multiple columns (Will short print)
    #print(df[['flightState_location_latitude','flightState_location_longitude']])
    # select three rows and two columns (rows: 2-4m 0-based)
    print(df.loc[1:3, ['flightState_location_latitude','flightState_location_longitude']])
    # Write out entire file to CSV
    #df.to_csv('/TEST_DATA/OUTPUT/small-tonyg-out.csv', index=False)
    # Write out the lat/longs to a file in CSV (no header row, no index)
    df.to_csv('/TEST_DATA/OUTPUT/lat-longs.csv', columns=["flightState_location_latitude","flightState_location_longitude"],header=False,index=False)
def basics():
    # Example dataframe
    df = pd.DataFrame({'numbers': [1, 2, 3],
                       'colors': ['red', 'white', 'blue'],
                       'vil': [float("NaN"), float("nan"), float("nan")]},
                      columns=['numbers', 'colors', 'vil'])
    print(df)
    vil_updates = [44, 55, 66]
    df['vil'] = vil_updates
    print(df)

    def get_random_list_of_ints(size):
        return [random.randrange(1, 50, 1) for i in range(size)]

    res = get_random_list_of_ints(7)
    print("Size: %d" % len(res))
    print(res)

print("Testing pandas....")
#basics()
handle_small_parquet()
