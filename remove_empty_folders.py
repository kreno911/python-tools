#! /usr/bin/env python
import os, sys, datetime

################################################################################
#
# Unit: remove_empty_folders.py
#
# Overview:
#   Remove any empty folders under the directory prior to the current
#   hour.
#
################################################################################

def removeEmptyFolders(path):
  if not os.path.isdir(path):
    return

  # remove empty subfolders
  files = os.listdir(path)
  if len(files):
    for f in files:
      fullpath = os.path.join(path, f)
      if os.path.isdir(fullpath):
        removeEmptyFolders(fullpath)

  # if folder empty, delete it
  if len(os.listdir(path)) == 0:
        # str - to convert int to string
        if not path.endswith(str(datetime.datetime.utcnow().hour)) and not path == keep:
                os.rmdir(path)

if len(sys.argv) != 2:
    print("Need directory, could be '.'")
    sys.exit(11)
keep = sys.argv[1]
removeEmptyFolders(sys.argv[1])

