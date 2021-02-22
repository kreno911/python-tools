
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
    # Set and check a boolean variable
    print("Booleans...")
    A_TRUE_VALUE = True
    if A_TRUE_VALUE:
        print("A True value...")
    else:
        print("A False value...")
    # Compound if (logical)
    if True or False:
       print("TRUE or FALSE = true")
    # You need parens for this to work
    if not (True and False):
       print("TRUE and FALSE = false")
    ##### NUMBERS (formats)
    # print a number with 15 decimal places
    new_longitude = -84.426410512618901
    new_latitude  = 33.638104528469903
    print("Lat/Long with 15 dec places: %.15f,%.15f" % (new_longitude,new_latitude))
    print("Ordinary int: %d" % 1234567890123)

    # Skip lines
    print("Print skipped lines (i % 3 == 0)...")
    i = 0
    for i in range(21):
        if (i % 3 == 0):
            print("   Only printing: %d" % i)
    # Print out A-Z
    for one in range(65,91):  # Change #s to see other characters 
        print(chr(one))
    print("range (1,5)")
    for j in range(1, 5):    # Will print 1 - 4
        print("   j = %d" % j)

    # random ints 0 - (N-1)
    print("Print random dice 0 - 9")
    for i in range(10):
        dice = random.randint(0, 10)
        print("dice = ", dice)

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
    # Test for empty directory
    # Other ways: if os.listdir(work_path) = []:, if len(os.listdir(work_path)) > 0:
    if not os.listdir("."):
        print("Dir is empty...")
    else:
        print("This dir has files")

    # Test seeing if a process id directory exists to tell if that
    # process is actually running
    # First look in /proc and grep to see what processes are running.
    # Kill that process and run this script second time to get alternate path
    PID = 31175
    print("Check for process id %d existing" % PID)
    print(os.path.exists("/proc/%s" % PID))

    # Make a system call
    #from subprocess import call
    # os.system does not give you access to process input or output
    #cmd = "/usr/local/ldm/wim/wim_startup.sh %s" % "MATCHER"
    #print cmd
    #os.system(cmd)

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

    # Use pattern = re.compile(patter) and use pattern whenever you are in a
    # loop to improve performance.
    # re.compile("regex", re.IGNORECASE)  to search case insensitive.

    print("Remove spaces in between words:")
    string_w_spaces = "I     have    a   lot of   space between     each   word"
    print("string_w_spaces = %s" % string_w_spaces)
    print("string_w_spaces without spaces = %s" % re.sub(' +',' ',string_w_spaces))

    print("Find text within parenthesis...(first way):")
    string_w_txt_in_paren = "This is (text) within parenthesis"
    print(string_w_txt_in_paren[string_w_txt_in_paren.find("(")+1:string_w_txt_in_paren.find(")")])
    print("Test regex capture...")
    tar_file = "tarfile_10-29-2018_33_tester.tar"
    n = re.search(".*_(..)-(..)-(\d{4})_(..).*", tar_file)
    # YYYYMMDD
    date_part = n.group(3) + n.group(1) + n.group(2)
    print(tar_file, "(YYYYMMDD): ", date_part)

def testFilesAndDirs():
    print("...FILE/DIR TESTING...")
    # Does a file exist?
    if not os.path.isfile("nofile"):
        print("nofile does not exist")
    # Does directory exist
    if not os.path.isdir("/home/nodir"):
        print("/home/nodir does NOT exist")

    print("Opening file...")
    # Opens a file for reading. 'w' writing, 'a' append 
    afile = open("python_test_file1.txt")
    for line in afile:
        if line.strip():               # quick way to skip blank lines
            print("   ", line.rstrip())        # Pick off newlines
    print("Closing file...")
    afile.close()

    # Use the with statement to open a file. It will automatically close the file.
    print("Opening file with 'with' statement...(with (open(file) as f)")
    with open("python_test_file1.txt") as afile:
        for line in afile:
            print("\tline = %s" % line.strip())   # pick off newlines

    # Test out a file with name/value pairs and split them out
    # Some values could have ',' with further parsing needed
    afile2 = open("python_test_file2.txt", 'r')
    print("  Key/value file")
    for line in afile2:
        if line.strip():
            key, value = line.split("=")
            print("Key: ", key, ", Value: ", value.rstrip())
            # extra parsing if needed
            if value.count(",") != 0:   # Found some , character
                print("   ", value.rstrip(), " [1]: ", value.split(",")[1].rstrip())

    # Create a few directories by numbered list
    for i in range(1, 6):  # create dirs 1 - 5
        try:
            print("Creating dir: %d" % i)
            os.makedirs(str(i))   # Need str function as param needs to be a string
        # Catch any exception and print the error message
        except Exception as e:
            print("Exception caught: %s" % e)
            print("   Now going to delete %s..." % str(i))
            os.rmdir(str(i))

    # Get a directory listing
    print("Directory listing...")
    files = os.listdir("/tmp")
    index = 0
                    # This extra does ! work
    for f in files: # Tried to add conditional:  'and f.endswith(".ncl"):'
        print("/tmp File: ", f)
        # Only print first 3 
        if index == 2:
            break
        index += 1 
def testSysFunctions():
    # Can import anywhere in file 
    import multiprocessing
    print("CPUs?? ", multiprocessing.cpu_count())  # Return 4 on HP laptop

def testGlobFunctions():
    # Print out only txt files. Note glob will return the FULL path of a file 
    # If you want only the filename, use glob1() 
    # glob1() requires 2 args: dir and pattern 
    # This means if you use the files down the road, you will need to os.chdir()
    # to reference them, ie: sorting that list will not find the files.
    print("Glob(*.txt): %s", glob.glob("*.txt"))

    # Get the latest file in a dir (should be a small directory of files)
    listOfFiles = glob.glob('*')
    print("Size of listOfFiles: %d" % len(listOfFiles))
    latest_file = max(listOfFiles, key=os.path.getctime)

    # Filter files based on regex
    files_starting_w_dd = [f for f in glob.glob("*") if re.search("^\d\d",f) ]
    # This returns a list of files that begin with a double digit

    # Sort a list of files by date
    ##files = glob.glob("*.txt")
    ##files.sort(key=os.path.getmtime,reverse=True)  # Reverse optional
    # False is the default 

def testStringFunctions():
    print("TESTING %s functions." % "STRING")
    # Simple compare (mixed quotes)
    if "none" == 'none':
        print("string is none")
    print("Does string contain something?")
    a_string = "I contain 3"
    if "3" in a_string:
        print("Found 3 inside final_string [%s]" % a_string)

    # Pad a string/number with 0's
    number = "6"    # Since 6 here is defined as a string, need int() to convert
    # if its just a number, no need to convert
    print("This number has 5 places: %05d" % int(number))

    # zfill function
    zfill_string = "fill me in"
    print("%s : (15 total characters front-padding with 0s) " % (zfill_string.zfill(15)))
    print("")
    print("String length (thisis my string) (%d)." % len("thisis my string"))
    print("")
    print("Basic printing/substitions...")
    print("    String substition: %s" % "a_string")
    print("    Int substition: %d" % 1234)
    print("")
    # Create string array of padded digits
    hours = ["%02d" % h for h in range(24)]
    # hours will contain '00', '11', '22'...'23'
    print("Replace ; with new pipe: \"hi;I am;a block head;\"")
    print("hi;I am;a block head;".replace(';','|'))

    # Use split() to split a string with varying spaces between each field
    # It will not add extra elements due to > 1 space between
    x = "this   has   multiple spaces"
    print("x.split() size = %d" % len(x.split()))
    print("x.split(' ') size = %d" % len(x.split(' ')))

    print("Split name:value...")
    line = "NAME:ACTION"
    print("Split line = ", line.split(":")[1])

    string1 = "I AM A BASIC STRING THAT IS NOT TOO LONG"
    print(string1, " is %d chars long" % len(string1))

    # Try splitting only the first 3 words delimited by space
    first_3_words = string1.split(" ", 3)
    print("Split only first 3 words: %s" % first_3_words)

    # Replace the spaces in the string with * using split/join
    new_string_w_stars = "*".join(string1.split())
    print("After split/joining with asterisk: %s" % new_string_w_stars)

    # Do same as above but replace *'s for only first 3
    new_string_w_3_stars = string1.replace(" ", "*", 3)
    print("Replace first 3 spaces with asterisk: %s" % new_string_w_3_stars)

    print("Print last 3 digits of string...")
    s = "03_33_222"
    print("s = %s" % s, s[len(s)-3:])
    print("Print everything except last 4 chars...")
    print("  s = %s" % s[:-4])

    UP = 0
    DOWN = 1
    DEGRADED = 2
    values = [UP,DOWN,DEGRADED]
    port_string = "p=%d, q=%d, x=%d" % tuple(values)
    print("substitution with array of values: port_string = ", port_string)

def testEnv():
    # Print an environmental variable
    print("Home ENV var is [%s]" % os.environ['HOME'])
    print("TEST ENV var is [%s]" % os.environ.get('TEST'))
    print("TEST ENV, using getenv [%s]" % os.getenv('TEST'))
    # Need to use str function to make the reference a string
    if str(os.getenv('TEST')) == 'None':
        print("   env.get() TEST is None")
    else:
        print("   2) TEST value is [%s]" % str(os.getenv('TEST')))
    # Check if one exist - throws exception if !exists
    try:
        if os.environ['TEST'] != "":
            print("env TEST does exist...")
    except KeyError as e:
        # You may see e.msg in getopt cases, msg does ! exist for this e
        print("Keyerror caught do to non-existant ENV var. Msg: %s" % e)
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
# Test out tuples
def testTuples():
    ##### TUPLES
    from operator import itemgetter
    print("TUPLES ****************")
    # Init a tuple
    aTuple = ()
    # Assign
    aTuple = (4, 5)
    print("     aTuple = %s,%s" % aTuple)
    # Combine 2 tuple lists together
    tupleList1 = [] #[(11,3),(5,4)]
    tupleList1.append((11,3))
    tupleList1.append((5,4))
    tupleList2 = [(7,77),(8,88)]
    big_list = []
    # Using append will create a list of lists
    # Here we want to take both tuples and just combine all the values
    # into one tuple list
    big_list.extend(tupleList1)  
    big_list.extend(tupleList2)
    print("     Combined tuple lists: ", big_list)
    print("     Max X: ", max(big_list, key=itemgetter(0))[0])
    print("     Max Y: ", max(big_list, key=itemgetter(1))[1])

def testSets():
    DICT = {}   # Initialize
    # Here can use a dictionary to mimic a switch statement
    # in java
    # You want to switch on a character and return a number 
    # for that letter
    VALS = {'A':1,'J':1,'S':1,'B':2,'K':2,'T':2,'C':3,'L':3,'U':3 }
    print("Swich statment: 'A' will return (1): %d" % VALS.get('A'))
    # Other assignment way
    SOME_DICT = {'key':'value'}
    print("SOME_DICT simple: ", SOME_DICT)
    # To check for a value in a dictionary
    if 'A' in VALS:
        print("A is in VALS dict")
    else:
        print("A was not found in VALS dict")

    # Assignment of a single value
    somedict = {}
    somedict['mykey'] = "myvalue is this"
    print("%s key with %s value" % ("mykey", somedict.get("mykey")))

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
# Try importing exit functions which will get called no matter what happens
import atexit
# Register exit function
def all_done():
    print("all_done() functions called at END...")
atexit.register(all_done)

#print "  Sleeping..."
#time.sleep(5)  # sleep for 5 seconds

testBasics()
testOsFunctions()
testSysFunctions()
testGlobFunctions()
testEnv()
testArgs()

# testFilesAndDirs()
testRegexFunctions()

testStringFunctions()
testLists()
testTuples()
testSets()
testDictionaries()

