import urllib
import re

# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://www.wunderground.com/global/stations/65432.html")
# Read from the object, storing the page's contents in 's'.
s = f.read()
match=re.search(r'(<div*?)>(\w)',s)
if match !=None:
       print match.group(2)
f.close()
