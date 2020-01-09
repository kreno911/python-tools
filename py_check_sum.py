
#########################################
# Take two files as input and dtermine if they are 
# identical.
#
# Usage: python py_check_sum.py test_data/test1 test_data/test3
#
##########################################

import sys, os, hashlib

# Need two files on command line
if (len(sys.argv) != 3):
    print("Please enter two files to compare.")
    sys.exit(11)

file1 = open(sys.argv[1],'rb')
file2 = open(sys.argv[2],'rb')

file1_chksum = hashlib.md5(file1.read()).hexdigest()
file2_chksum = hashlib.md5(file2.read()).hexdigest()
print("File1: %s" % file1_chksum)
print("File2: %s" % file2_chksum)

if file1_chksum == file2_chksum:
    print("These files are identical")
else:
    print("These files are different")
