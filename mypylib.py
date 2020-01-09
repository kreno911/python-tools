
from datetime import datetime
import os, re

####
# Check if first file is older than second.
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
# Return all file paths that are older the this_file.
####
def files_older_than(this_file, list_of_files):
    for filename in list_of_files:
        if os.path.getmtime(os.path.join(os.path, filename)) < now - 7 * 86400:
            if os.path.isfile(os.path.join(os.path, filename)):
                print("%s is older than %s" % (this_file,filename))

