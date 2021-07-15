# Use ftplib for anonymous login
from ftplib import FTP
from datetime import datetime, timedelta
import re

'''
    https://pysftp.readthedocs.io/  - site with docs
    
    NOTE: pysftp package does NOT allow anonymous FTP without user/pass (SSH)
'''
# Do a simple listing of a public website FTP server
site  = "ftp.ncep.noaa.gov"
today = (datetime.utcnow() - timedelta(hours=8))
today_str = today.strftime('%Y%m%d')

#directory="/pub/data/nccf/com/hrrr/prod/hrrr."+today_str+"/conus"
directory="/pub/data/nccf/com/hrrr/prod/hrrr.20210711/conus"
ftp = FTP(site)
ftp.login()             # Anonymous login
ftp.cwd(directory)      # Change to a directory
files = ftp.nlst("*.grib2")
print("Times: %s:%s:%s" % (datetime.utcnow(),today_str,today))
print("Total files: %d" % len(files))
count = 0
for afile in files:
    # Look for pressure level files only
    search_for = re.search('hrrr.t(\d+)z.wrfprsf(\d\d)', afile)
    if search_for:
        count += 1
        print("Pressure level grib2: " + afile)

ftp.quit()
print("Total PRS files: %d" % count)

