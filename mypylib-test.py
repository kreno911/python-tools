
# Tester for mypylib functions
# When all functions return True, we are good to go
#
# All tests should be named test_#_<actual_function_name>_<test_case>
#
# Run as: python3 -m unittest mypylib-test.py

import unittest
from mypylib import *

class TestMypylib(unittest.TestCase):
    # Basic test between two files. May need to create/modify
    # to get test to work correctly. 
    def test_1_is_older_a(self):
        print("Test files_older_than_a")
        #file1 = "test_data/temp_data.csv"
        file1 = "test_data/test1"
        file2 = "test_data/test2"
        if is_older(file1, file2):
            print("%s is older than %s" % (file1, file2))
        else:
            print("%s is not older than %s" % (file1, file2))
    # Test FileNotFoundError exception thrown for non-existent file
    def test_2_is_older_b(self):
        print("Test files_older_than_b")
        file1 = "test_data/test"
        file2 = "test_data/test2"
        with self.assertRaises(FileNotFoundError):
            is_older(file1, file2)
    # Test minutes old for file - create file an hour or so old
    # to get successful values.
    def test_3_get_age_of_file_a(self):
        print("Test get_age_of_file_a")
        afile = "test_data/test1"
        print("Testing get_age_of_file() minutes...")
        print("%s is %d minutes old" % (afile, get_age_of_file(afile)))
        print("      %d seconds old" % get_age_of_file(afile, unit='s'))
        print("      %d hours old" % get_age_of_file(afile, unit='H'))
        print("      %d days old" % get_age_of_file(afile, unit='d'))
    # Test that ValueError is raised if unit is not correct
    def test_4_get_age_of_file_b(self): 
        print("Test test_get_age_of_file_b (exception)")
        with self.assertRaises(ValueError):
            get_age_of_file("test_data/test1", unit='x')
    # Test files older than a date
    def test_5_files_older_than(self):
        print("Test files older that date 1")
        # Must create a list of files with various dates
        files = ["comma.py","line_printer.py","mypylib-test.py"]
        delete_files = files_older_than("2020-02-01 10:00:00", files)
        print("Files: %s" % delete_files)  # Should print all
        self.assertEqual(len(delete_files), 3)
    # Test files NOT older than a date
    def test_6_files_older_than(self):
        print("Test files NOT older that date 1")
        # Must create a list of files with various dates
        files = ["comma.py","line_printer.py","mypylib-test.py"]
        delete_files = files_older_than("2019-02-01 10:00:00", files)
        print("Files: %s" % delete_files)  # Should print all
        self.assertEqual(len(delete_files), 0)

    def testAddressInNetwork():
        print("Testing addressInNetwork to see if IP is in a network...")
        # False
        print("addressInNetwork('188.104.8.64','172.16.0.0','255.240.0.0') = ", \
                addressInNetwork('188.104.8.64','172.16.0.0','255.240.0.0'))
        # True
        print("addressInNetwork('10.9.8.7', '10.9.1.0','255.255.0.0') = ", \
                addressInNetwork('10.9.8.7', '10.9.1.0','255.255.0.0'))
        # False
        print("addressInNetwork('10.9.8.7', '10.9.1.0','255.255.255.0') = ", \
                addressInNetwork('10.9.8.7', '10.9.1.0','255.255.255.0'))

