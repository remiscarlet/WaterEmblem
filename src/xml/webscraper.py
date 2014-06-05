#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
import re
import string
import os.path
import subprocess 
import codecs

shipxml = codecs.open(os.path.join(os.path.curdir,"KanmusuStats.xml"))
shiplines = shipxml.readlines()
shiplist = []
print shiplines[3][12:19]
#for line in shiplines:
#    if line[:9] == "<JP-Name>":
#        print line
#        shiplist.append(line[9:line.rfind("<")])
#
#shiplist.pop(0)
#print shiplist
