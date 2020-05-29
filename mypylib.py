
from datetime import datetime
import os, re, stat, time

# Important links/info
#   https://www.techbeamers.com/python-time-functions-usage-examples/#time-time-function
#   datetime.strptime returns datetime.datetime (2016-10-10 10:00:00)
#   os.path.getmtime returns float (1513777689.66)

####
# Check if first file is older than second.
# Param 1: First file for comparison 
# Param 2: Second file for comparison
# Returns: True if first file is older than second 
# Raises: FileNotFoundError if either file does not exist
####
def is_older(file1, file2):
    """ Return True if first file is older than second file.
        Both parameters must be string pointing to files.
    """
    try:
        f1_time = datetime.fromtimestamp(os.path.getctime(file1))
        f2_time = datetime.fromtimestamp(os.path.getctime(file2))
        return f1_time < f2_time
    except FileNotFoundError:
        print("Exception: Check your files: [%s,%s]" % (file1,file2))
        raise FileNotFoundError
####
# Return file age based on unit (default to minutes)
# Param 1: file to check age of
# Param 2: unit to check for: mM - minutes, default
#                             sS - seconds
#                             hH - hours
#                             dD - days
# Raises: ValueError if unit not found
#
# time.time() returns # seconds since 1970 as floating point.
#   Ex: 1504634843.1003768
# Note: 
#   Age is NOT exact and time is truncated. Should be fine for most uses.
####
def get_age_of_file(file, unit="M"):
    """ Return unit age of given file. 
        unit defaults to 'm|M' - minutes
        's|S' - seconds
        'h|H' - hours
        'd|D' - days
        This function truncates mantissa on all times int(x) and is not exact. 
        Values of 1.9 will return 1. Use this function when inexact times are sufficient. 
        """
    if unit not in ("m","M","s","S","h","H","d","D"):
        raise ValueError("unit not correct! [m|M|s|S|h|H|d|D]")
    # Seconds old
    if unit == "S" or unit == "s":
        return int((time.time() - os.stat(file)[stat.ST_MTIME]))
    # Hours old
    if unit == "H" or unit == "h":
        return int((time.time() - os.stat(file)[stat.ST_MTIME])/60/60)
    # Days old
    if unit == "D" or unit == "d":
        return int((time.time() - os.stat(file)[stat.ST_MTIME])/60/60/24)
    # Minutes
    return int((time.time() - os.stat(file)[stat.ST_MTIME])/60)
####
# Return all files that are older given date from given list.
# Param 1: Date in format: "%Y-%m-%d %H:%M:%S", ex: 2019-10-25 14:30:00"
# Param 2: List of files with absolute paths
# Returns: List of strings of file paths for files older than date
####
def files_older_than(older_than_date, list_of_files):
    # convert the date to a time (strptime returns datetime.datetime)
    files = []
    timestamp = datetime.strptime(older_than_date, "%Y-%m-%d %H:%M:%S")
    epoch_seconds = (timestamp-datetime(1970, 1, 1)).total_seconds()
    for filename in list_of_files:
        if int(os.path.getmtime(filename)) < epoch_seconds:
            files.append(filename)
    return files

#############
# Return whether this string contains a character (ignore periods).
# Param: some_string - any string of numbers/characters
# Returns boolean True if this string contains a character
#############
def contains_char(some_string):
    # '.' are picked up as word chars, so just return true
    if "." in some_string:
        return False
    chars = re.compile('\D')  # non-digit 
    return bool(chars.search(some_string))
