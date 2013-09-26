##
# CASAPY initialization file 
#
# To load the pipeline scripts automatically, please:
#   1) place this file to ~/.casa/
#   2) alias casapy='casapy --log2term'
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
from glob import glob as filesearch
import inspect

print ""
print ""
print "+"*70
print ""
print ""

# SPECIFIY ENVI PATHS

#     PYTHON PATH
xlib_path=os.path.dirname(os.path.realpath(inspect.stack()[0][1]))  # pipeline script location
xlibp_path=os.path.dirname(xlib_path)
borrow_path=xlibp_path+'/borrow'                    # borrowed modules location
#     SHELL PATH
if  'MIRBIN' in os.environ.keys():
    mir_path=os.environ['MIRBIN']                                       # MIRIAD task location
else:
    mir_path='/unknown'
gs_path='/opt/local/bin'                                            # GhostScript location
carmafiller_path='/usr/local/miriad-carma/opt/casa/bin'
carmafiller_libpath='/usr/local/miriad-carma/opt/casa/lib'

# PIPELINE VARIABLES


# USER VARIABLES

xlib=xlib_path+'/'                          # shortcut for xlib script path
stinghi=xlibp_path+'/scripts/sting-hi/'     # shortcut for sting-hi script path
stingco=xlibp_path+'/scripts/sting-co/'     # shortcut for sting-co script path
sting13co=xlibp_path+'/scripts/sting-13co/' # shortcut for sting-13co scripth path
examples=xlibp_path+'/scripts/examples/'    # shortcut for examples script path
testing=xlibp_path+'/scripts/testing/'      # shortcut for testing script path

# ADD PATH & LOAD MODULES 
pathlist=[mir_path,gs_path,carmafiller_path]
libpathlist=[carmafiller_libpath]
#use subprocess+env rather than modifying os.environ
#os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist) 
extenv={"PATH":os.pathsep.join(pathlist),
        "DYLD_LIBRARY_PATH":os.pathsep.join(libpathlist),
        "HOME":"~/"}

sys.path.insert(1,xlib_path)
import xutils as xu                 # xlib modules 
#import xexp as xe                   # exlib-exp modules

sys.path.insert(1,borrow_path+os.sep+'analysis_scripts')
#import analysisUtils as au          # borrowed modules

print '>>>> MachineName:'
machinename=socket.gethostname()
print machinename
print ''
print '>>>> PipelinePath:'
print xlib_path
print ''
print '>>>> MiriadPath:'
print mir_path

print ""
print ""
print "+"*70
print ""
print ""