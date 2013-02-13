##
# CASA initialization file 
#
# For loading pipeline scripts automatically, please:
#   1) place this file to ~/.casa/
#   2) create an alias
#   alias casapy='casapy --log2term'
#       or
#   alias casapy='yourpath/CASA.app/Contents/MacOS/casapy --log2term'
#
# Notes:
#   casapy startup options:
#       --help
##

import socket
import sys
import time
import os
import string
from sets import Set
import math
import copy
import numpy as np

machinename=socket.gethostname()

print ""
print ""
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print ""
print ""
print '>>>> MachineName:'
print machinename




# customize pipeline setup 

script_home='/Users/Rui/Dropbox/Worklib/casapy/'
gspath='/opt/local/bin:'
mirbin='/usr/local/miriad-carma/bin/darwin/'
if  machinename.find('carma-data')!=-1:
    script_home='/Users/ruixue1/Worklib/casapy/'
    gspath='/opt/local/bin/'
    mirbin='/usr/local/miriad/miriad/bin/darwin/'
if  machinename.find('neon')!=-1:
    script_home='/Users/Rui/Dropbox/Worklib/casapy/'
    gspath='/opt/local/bin/'
    mirbin='/usr/local/miriad-carma/bin/darwin/'

if  not (script_home in sys.path):
    sys.path=[script_home]+sys.path

import sys
sys.path.append(script_home+"analysis_scripts/")
import analysisUtils as au

print ""
print ">>>> reduction script path:"
print script_home
print ""

print ">>>> ghostscript path:"
print gspath
os.environ['PATH']=gspath+os.environ['PATH']
print ""

print ">>>> miriad path:"
print mirbin
print ""

print ">>>> load reduction modules:"
from reduc_lib import *
from iplot_lib import *
print "reduc_lib.py"
print "iplot_lib.py"
print ""

print ">>>> load modified tasks:"
from iplotxy import iplotxy
print "iplotxy.py"
print ""

print ">>>> reduction script_version:"
script_version='20121110'
print script_version
print ""

print ">>>> notification email:"
myemail=None
print myemail
print ""

print ">>>> Additional Variable Settings:"
stinghi=script_home+'scripts/sting-hi/'
stingco=script_home+'scripts/sting-co/'
print "stinghi="+stinghi
print "stingco="+stingco

print ""
print ""
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print ""
print ""