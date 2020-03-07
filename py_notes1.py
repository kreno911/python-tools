
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

break - will break out of a loop, continue will continue as usual

If statements:
  Inline if-else EXPRESSION must always contain else clause
  x = y if "test" not in astring else z

Spatial stuff: OGR - for vector data
               GDAL - for raster data (deprecated)

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
####
# Greedy - will make the largest capture of data 
# 
def testRegexFunctions():
    print("TESTING %s functions." % "Regex")
    a_string = "I contain 123 and 456 and 7 and 99"
    print ("Trying to find all numbers in %s" % a_string)
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
def testArrays():
    print("Testing arrays...")
    print("Capture first two values of an array and default the rest")
    a,b,*c = (1,2,3,4,5,6)
    print("a,b,*c = (1,2,3,4,5,6) =>")
    print("   a=",a,"b=",b,"c=",c)
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
testArrays()
testSets()
testDictionaries()

