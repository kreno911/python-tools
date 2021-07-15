################################################################################
#
# Unit: get_mrms_files.py
#
# Overview:
#   This script will wget/FTP various MRMS file types and copy them into the
#   target directory.
#
#   Details:
#       This script must be run hourly to ensure we are getting the latest files.
#       File types downloaded are *.grib2.gz
#
################################################################################

import os, sys, re, shutil, glob
from datetime import datetime, date, timedelta

# Where we save data to (temporary)
TARGET_TEMP_DIR = "/mnt/nfs/weatherDev/temp/MRMS_WGET"
# Where to write the data (S3 at some pt)
TARGET_DATED_DIR = "/mnt/nfs/weatherDev/temp/MRMS_HOLD/%s/"

# Base dir for MRMS data (public site)
MRMS_BASE = "http://mrms.ncep.noaa.gov/data/2D/"
# All types we need to collect (subdirectories under MRMS_BASE)
types = [ "VIL", "EchoTop_18", "EchoTop_30", "MergedAzShear_0-2kmAGL", "SHI",
          "NLDN_CG_001min", "NLDN_CG_005min", "MergedAzShear_3-6kmAGL",
          "LayerCompositeReflectivity_Low", "LayerCompositeReflectivity_High",
          "LowLevelCompositeReflectivity", "LVL3_HREET", "MergedReflectivityQCComposite",
          "MergedReflectivityQComposite", "MergedReflectivityComposite",
          "PrecipFlag", "RadarQualityIndex", "LVL3_HighResVIL"
        ]

