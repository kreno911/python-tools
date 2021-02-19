
####################################
#   This first part is to cover all the basics needed to 
#   understand python.
#
#   The only imports tested here are in the import statement below.
#
####################################

'''
Basic quick notes:
Upgrade: https://stackoverflow.com/questions/15221473/how-do-i-update-pip-itself-from-inside-my-virtual-environment
pip uses requirements.txt to get manually set versions for packages.
pip install -r requirements.txt (check docs)

If you get this on a linux box:
  -bash: ./test.py: /usr/bin/python^M: bad interpreter: No such file or directory
  In the Notepad++ editor: Edit->EOL Conversion -> UNIX
  Or just use dos2unix command

break - will break out of a loop, continue will continue as usual

If statements:
  Inline if-else EXPRESSION must always contain else clause
  x = y if "test" not in astring else z

# Quick functions()
#   .strip(): will remove leading and trailing characters
#   .lstrip():  will remove leading characters
#   .rstrip(): will remove trailing characters
#   os.chdir(path): cd to path
#   os.getcwd(): get current working dir

 Local vs. global functions:
 Make a local pointer to the global function. If being called million times, its a little faster.
   lmax = max
   tt = time.time
 This tt reference will work faster due to the path python takes to look up functions.
 -----------
 Use a dictionary over a list as the searching is basically 0 time for dictionary (hashing).
 
 To see the default imports a python program has (at python prompt): dir()
       dir(__builtins__) 

 Find out where a library is located that you imported
 print(<module>.__file__)
 Exceptions
   If catching exceptions like so:
       try:
           ...
       except Exception, e:
           print e
   And you want to see more info:
   import traceback
   ...
   traceback.print_exc()

try else:
    try:
        function1()
        function2()
    except x:
        print("some exception...")
    else:
        print("Hello")
        function3()
Hello will be printed after function1 returns successfully and function2 will
never execute. This is a tricky way to get a function to execute only if another
function executes and you DONT want to catch that exception. So function3 could
throw exception x but you dont care in this case. 

WORKING EXAMPLES (for specific uses of these functions)

'''
import os, sys, glob, re, shutil, random

# Basic stuff that does not fit anywhere
def testBasics():
    # Use underscore for large numbers with ','
    number = 1_000_000
    print("large number 1_000_000 is %d" % number)
    # Other printing options
    print("Large number using f'{number}'", f'{number}')
    
# Function goes with testOsFunctions to show how to create/delete
# list files and dirs.
# Creates the following structure:
# /tmp/dir1/subdir1/subdir1[1-20].log, /tmp/dir1/subdir2/subdir2[1-10].txt
# /tmp/dir1/dir1[A-H].log
# /tmp/dir2/file[1-10].txt
# /tmp/dir3/subdir3/subsubdir3/subsubdir3[1-5].txt
def create_dirs_and_files():
    # Loop to the lowest denominator and create dirs then files
    try:
        # os.mkdir will create a single directory.
        # os.makedirs will create list of directories (mkdir -p)
        os.makedirs("/tmp/dir1/subdir1/", mode=0o755) # default mode is 0777 (umask)
        os.mkdir("/tmp/dir2/")
        os.makedirs("/tmp/dir3/subdir3/subsubdir3")
    except OSError:
        print("Could not create dir...")
    print("Dirs created!!")

def testOsFunctions():
    print("Testing OS functions...")
    create_dirs_and_files()

    # Test out splittext
    (drive, tail) = os.path.splitext("/projects/python/work/errors.txt")
    # Print out the full path up to extension and the extension 
    # Two ..text will leave a '.' in each value
    print("splitext: %s Tail: %s" % (drive, tail))
        # List a directory
    # os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    print("Walk one directory (/tmp) and break after first file group...")
    for dirName, dirs, files in os.walk("/tmp"):
        print('Found directory: %s' % dirName)
        for dir in dirs:
            print("  Subdir: %s" % dir)
        for file in files:
            print("  File: %s" % file)
        # Break after first dir listing
        break
####
# Greedy - will make the largest capture of data 
# 
def testRegexFunctions():
    print("TESTING %s functions." % "Regex")

    a_string = "I contain 123 and 456 and 7 and 99"
    print("Trying to find all numbers in %s" % a_string)
    # Find all consecutive #s
    numbers = re.findall('[0-9]+', a_string)
    # Find each #
    numbers_single = re.findall('[0-9+]', a_string)
    print(numbers)
    print("single numbers: ", numbers_single)

    a_string = "From: My Friend: Say hello"
    print("Greedy match on '%s'" % a_string)
    ff = re.findall("^F.+:", a_string)
    print(ff)
    print("non-greedy match:")
    print(re.findall("^F.+?:", a_string))

    a_string = "an-email.me@test.com"
    print("match non-blank chars")
    print(re.findall("\S+@\S+", a_string))
    print("something with blank 'my emai...': ", re.findall("\S+@\S+", "my email@gmail.com"))


def testSysFunctions():
    pass
def testGlobFunctions():
    pass
def testStringFunctions():
    print("TESTING %s functions." % "STRING")
    # zfill function
    zfill_string = "fill me in"
    print("%s : (15 total characters front-padding with 0s) " % (zfill_string.zfill(15)))
def testShutilFunctions():
    pass
def testRandomFunctions():
    pass
def testEnv():
    pass
def testArgs():
    pass
def testLists():
    print("Testing lists...")
        # Empty list (init)
    list1 = []
    # String list
    list2 = ["one", "two", "three" ]
    print("List of strings: ", list2)
    print("Index 0 = %s, index 1 = %s" % (list2[0], list2[1]))
    # Print a "long" list with each value on a separate line
    print("Each on a line (\"\\n\".join(list2):")
    print("\n".join(list2))
    # Append to the list
    list2.append("4_appended")
    print("List of strings (print list2): ", list2)
    # Get length
    print ("Size of list: ", len(list2))
    # Count occurrences
    list2.append("two")
    print("There are %d occurrences of two" % list2.count("two"))
    # Remove
    list2.remove("two")
    list2.remove("4_appended")
    print("After remove 4_appended: ", list2)
    # Get a slice of a list (0 - 9) ([x  for x in range(10)])
    ## Indexes in python are not inclusive.
    #  [0:5] -> get 1st - 5th index
    list3 = [x for x in range(10)]
    print("slicing...list3 is: ", list3)
    print("...all numbers except first and last: ", list3[1:-1])
    list4 = [x for x in range(10)]
    # To maintain the original list, assign a new list
    sorted_list = sorted(list4)
    print("list4 sorted in reverse: ", sorted(list4, reverse=True))
    # Second way to reverse a list
    print("list4 reversed 2[ \"\".join(str(list4[::-1]))]: ", "".join(str(list4[::-1])))
    print("Print every other item starting at index 0: %s" \
            % list4[0::2])
    print("Print every other item starting at index 1: %s" \
            % list4[1::2])
    # Convert list of strings to list of ints
    int_list = list(map(int,"132,133,34,235,137".split(",")))
    print(sorted(int_list))

    print("Capture first two values of an array and default the rest")
    a,b,*c = (1,2,3,4,5,6)
    print("a,b,*c = (1,2,3,4,5,6) =>")
    print("   a=",a,"b=",b,"c=",c)

    # Make a list from a string of csv values
    new_list = "N2H,N3H,NAH,NBH,NCO,NCZ,NCR,SRQ".split(",")
    print("new_list was string of csv values, now: %s" % new_list)
    # Will print: ['N2H', 'N3H', 'NAH', 'NBH', 'NCO', 'NCZ', 'NCR', 'SRQ']

    # Make a list of lists
    # Example list[0] should be a list of car names
    #         list[1] should be a list of boat names
    listOfLists = []   ##! to do
    car_list = ['BMW', 'AUDI', 'FORD']
    boat_list = ['STRIPER', 'MAKO', 'SAILFISH']
    ##listOfLists[0] = car_list
    ##listOfLists[1] = boat_list

    # Compare 2 list and print differences
    list1 = [1,2,3,4]
    list2 = [3,4,5,6]
    list3 = []    # Test empty list comparison 
    print("List1: ", str(list1))
    print("List2: ", str(list2))
    # sets do not maintain order, so can be different on each call
    diff_list1 = list(set(list1) - set(list2))
    print("Comparing lists (in 1 not in 2): " + str(diff_list1))
    diff_list2 = list(set(list2) - set(list1))
    print("Comparing lists (in 2 not in 1): " + str(diff_list2))
    diff_list3 = list(set(list1) - set(list3))
    print("Comparing list with empty list: " + str(diff_list3))

def testSets():
    pass
def testDictionaries():
    pass
def testFiles():
    # Always make use of context managers.
    # Context managers eliminate the need for close().
    # Also use these for threads and database connections
    with open("somefile_to_write_to", 'w') as wr_file:
        wr_file.write("Something...")

'''
Block out...
'''
testBasics()
testOsFunctions()
testSysFunctions()
testGlobFunctions()
testShutilFunctions()
testRandomFunctions()
testEnv()
testArgs()

testRegexFunctions()

testStringFunctions()
testLists()
testSets()
testDictionaries()

