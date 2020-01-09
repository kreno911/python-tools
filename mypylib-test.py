
# Tester for mypylib functions
# When all functions return True, we are good to go

import unittest
from mypylib import *

class TestMypylib(unittest.TestCase):
    def test_files_older_than_a(self):
        print("Test 1")
        #file1 = "test_data/temp_data.csv"
        file1 = "test_data/test1"
        file2 = "test_data/test2"
        if is_older(file1, file2):
            print("%s is older than %s" % (file1, file2))
        else:
            print("%s is not older than %s" % (file1, file2))
    def test_files_older_than_b(self):
        print("Test 2")
        # Test exception thrown for non-existent file
        file1 = "test_data/test"
        file2 = "test_data/test2"
        with self.assertRaises(FileNotFoundError):
            is_older(file1, file2)
    