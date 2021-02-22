#!/usr/bin/python

import sys
import xml.etree.cElementTree as ET

##
## Found this on the web when trying to process extremely large
## XML files. In our case, this did not work since we were trying 
## to process FIXM files which contain namespaces and this just 
## chokes on those. But it does seem to work on regular XML files.
##

# Example routetest.xml
'''
<route>
   <name>port name</name>
   <speed>10 Gb</speed>
   <location>Northeast</location>
</route>
'''

def process_buffer(buf):
    tnode = ET.fromstring(buf)
    #pull it apart and stick it in the database
    for child in tnode:
        print "Tag: '%s', Value: '%s'" % (child.tag, child.text)

inputbuffer = ''
with open(sys.argv[1], 'rb') as inputfile:
    append = False
    # Modify tags here to get what you want
    for line in inputfile:
        if '<route>' in line:
            inputbuffer = line
            append = True
        elif '</route>' in line:
            inputbuffer += line
            append = False
            process_buffer(inputbuffer)
            inputbuffer = None
            del inputbuffer #probably redundant...
        elif append:
            inputbuffer += line

