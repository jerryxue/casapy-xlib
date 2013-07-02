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
    gspath='/opt/local/bin:'
    mirbin='/usr/local/miriad/miriad/bin/darwin/'
if  machinename.find('neon')!=-1:
    script_home='/Users/Rui/Dropbox/Worklib/casapy/'
    gspath='/opt/local/bin:'
    mirbin='/usr/local/miriad-carma/bin/darwin/'

extenv={"PATH":"/usr/local/miriad-carma/bin/darwin:/usr/local/miriad-carma/opt/casa/bin:",
        "DYLD_LIBRARY_PATH":"/usr/local/miriad-carma/opt/casa/lib",
        "HOME":"~/"}
            
# add scripts path
print ""
print ">>>> reduction script path:"
print script_home
print ""
if  not (script_home in sys.path):
    sys.path=[script_home]+sys.path
if  not (script_home+"analysis_scripts/" in sys.path):
    sys.path=[script_home+"analysis_scripts/"]+sys.path

print ">>>> ghostscript path:"
print gspath
os.environ['PATH']=gspath+os.environ['PATH']
print ""

print ">>>> miriad path:"
print mirbin
print ""

print ">>>> load reduction/analysis modules:"
from xutils import *
from iplot_lib import *
import analysisUtils as au
print "xutils.py"
print "iplot_lib.py"
print "analysisUtils.py"
print ""

print ">>>> load modified tasks:"
from iplotxy import iplotxy
print "iplotxy.py"
print ""

print ">>>> reduction script_version:"
script_version=''
print script_version
print ""

print ">>>> notification email:"
myemail='jerryxue@gmail.com'
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