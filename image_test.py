
from PIL import Image
from PIL.ExifTags import TAGS

# For date: DateTimeOriginal
for (tag,value) in Image.open("IMG_0068.JPG")._getexif().iteritems():
    if TAGS.get(tag) == 'DateTimeOriginal':
        print "Image was created: %s" % value

