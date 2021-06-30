import os, sys, datetime

# The scan file will contain files to check. If one does not exist
# print it out to screen.
scan_file = "/Users/icecube/Downloads/item_images_to_check.txt"
direct = "."
# If one argument is provided, use it for search dir
if len(sys.argv) == 2:
    direct = sys.argv[1]
#print("Searching: %s" % direct)

files_to_check = []
with open(scan_file) as scanf:
    files_to_check = [line.strip() for line in scanf]

# Search subdirectories, create list of filenames only in this
all_files_found = []
## When merging lists you will see, [[list1],[list2]...] IF you use append(list)
## So use list.extend(list) instead
for dirpath, dirnames, filenames in os.walk(direct):
    all_files_found.extend(filenames)

# Check if what is in scan file is found on disk
filter = ".jpg"
for ff in all_files_found:
    if not ff.endswith(filter):
        continue
    if not ff in files_to_check:
        print("File not found in scan file: %s" % ff)

# Check if what was found on disk, exists in scan file
for ff in files_to_check:
    if not ff.endswith(filter):
        continue
    if not ff in all_files_found:
        print("File not found on disk: %s" % ff)

# Using os.listdir only lists current directory (use walk above)
'''
files = os.listdir(direct)
if len(files):
    for f in files:
        if not f.endswith(filter):
            continue
        if not f in files_to_check:
            print("File not found: %s" % f)
'''