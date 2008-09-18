#!/usr/bin/python

from pyhatebu import *
import sys
import os


if len(sys.argv) < 2:
    entries = get_hotentry()
else:
    entries = get_popular(sys.argv[1])
if len(sys.argv) == 2:
    num = 5
else:
    num = sys.argv[2]

links = " "
for entry in entries[0:int(num)]:
    link = entry['url']+" "
    links += link

os.system("open /Applications/Firefox.app"+links)



