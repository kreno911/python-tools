
# Tester for mypylib functions
# When all functions return True, we are good to go
#
# All tests should be named test_<actual_function_name>_<test_case>
#
# Run as: python3 -m unittest mypylib-test.py

import unittest
from mypylib import *

class TestMypylib(unittest.TestCase):
    # Basic test between two files. May need to create/modify
    # to get test to work correctly. 
    def test_files_older_than_a(self):
        print("Test files_older_than_a")
        #file1 = "test_data/temp_data.csv"
        file1 = "test_data/test1"
        file2 = "test_data/test2"
        if is_older(file1, file2):
            print("%s is older than %s" % (file1, file2))
        else:
            print("%s is not older than %s" % (file1, file2))
    # Test FileNotFoundError exception thrown for non-existent file
    def test_files_older_than_b(self):
        print("Test files_older_than_b")
        file1 = "test_data/test"
        file2 = "test_data/test2"
        with self.assertRaises(FileNotFoundError):
            is_older(file1, file2)
    # Test minutes old for file - create file an hour or so old
    # to get successful values.
    def test_get_age_of_file_a(self):
        print("Test get_age_of_file_a")
        afile = "test_data/test1"
        print("Testing get_age_of_file() minutes...")
        print("%s is %d minutes old" % (afile, get_age_of_file(afile)))
        print("      %d seconds old" % get_age_of_file(afile, unit='s'))
        print("      %d hours old" % get_age_of_file(afile, unit='H'))
        print("      %d days old" % get_age_of_file(afile, unit='d'))
    # Test that ValueError is raised if unit is not correct
    def test_get_age_of_file_b(afile):
        pass
