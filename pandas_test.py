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
    # To make sure ALL columms are printed
    pd.set_option('display.max_columns', None)
    # Other options to add to read_*
    #    delimuter="\t"  (tab) - check docs for others
    #    
    # Create sample dataframe
    df = pd.DataFrame({'numbers': [1, 2, 3],
                       'colors': ['red', 'white', 'blue'],
                       'vil': [float("NaN"), float("nan"), float("nan")]},
                      columns=['numbers', 'colors', 'vil'])
    # print number of columns/rows
    print("Number of columns %d" % len(df.columns))
    print("Number of rows %d" % len(df.index))
    # print columns only
    print(df.columns)
    # Print a few columns
    print(df[['colors','vil']])
    print(df)
    vil_updates = [44, 55, 66]
    # Assign values to whole column 
    df['vil'] = vil_updates
    print(df)
    
    df = pd.DataFrame(np.random.rand(4, 8))
    # Print first 5 
    print(df.head(5))
    '''
    prints the following
              0         1         2         3         4         5         6         7
    0  0.523416  0.459015  0.861435  0.237601  0.013846  0.071018  0.273127  0.872113
    1  0.717681  0.322752  0.857043  0.355224  0.747973  0.724821  0.234605  0.850687
    2  0.945175  0.177572  0.899477  0.108231  0.477513  0.800410  0.963119  0.795947
    3  0.470568  0.381467  0.066612  0.912329  0.072366  0.334874  0.161733  0.674814
    '''
    ntsb_file = "ntsb_events.csv"
    # Copied this from Hue (postgres) CSV windows to unix and got: invalid continuation byte
    # Used ISO-8859-1 encoding to get to work.
    ntsb_df = pd.read_csv(ntsb_file, encoding="ISO-8859-1")
    print(ntsb_df)


    def get_random_list_of_ints(size):
        return [random.randrange(1, 50, 1) for i in range(size)]

    res = get_random_list_of_ints(7)
    print("Size: %d" % len(res))
    print(res)

print("Testing pandas....")
#basics()
handle_small_parquet()
