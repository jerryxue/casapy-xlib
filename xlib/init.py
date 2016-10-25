########################################################################
# CASAPY INITIALIZATION FILE 
#
# To load the pipeline scripts automatically, please:
#   1)    Setup the initialization file 
#
#         ln -s <yourpath>/xlib/init.py ~/.casa/init.py
#           or
#         in ~/.casa/init.py, add: execfile('<yourpath>/xlib/init.py') 
#
#   2)    CREATE ALIAS (for saving script logs)
#
#         casa='casa --log2term'
#           or
#         casa='casa --log2term --nologger''
########################################################################

import socket
from glob import glob as filesearch
import inspect

print ""
print ""
print "+"*80
print ""

#   XLIB PATH
xlib_path=os.path.dirname(os.path.realpath(inspect.stack()[0][1]))

#   MIRIAD PATH
if  'MIRBIN' in os.environ.keys():
    mir_path=os.environ['MIRBIN']
else:
    mir_path='not located'

sys.path.insert(1,xlib_path)
import xutils as xu                 # xlib modules
from ximport import ximport 
from xclean import xclean
from xcal import xcal
from xconsol import xconsol
xu.ximport=ximport
xu.xclean=xclean
xu.xcal=xcal
xu.xconsol=xconsol

print '>>>> Machine Name   :'
machinename=socket.gethostname()
print machinename
print ''
print '>>>> Pipeline Path  :'
print xlib_path
print ''
print '>>>> MIRAID Path    :'
print mir_path
print ''
print '>>>> Current CASA Version:'
print '  '+casadef.casa_version + ' (r'+casadef.subversion_revision+')'
print ''
print '>>>> Compatible CASA Version:'
print '>=4.7.0-REL (r38335)'
print ""
print "+"*80
print ""

########################################################################
#    SOME PERSONAL SETTINGS.......
########################################################################


#   path of some non-essential programs (gs/wget...)
#   ADD PATH & LOAD MODULES 
#   use subprocess+env rather than modifying os.environ
#   os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist) 
bin_paths=['/opt/local/bin','/usr/local/miriad-carma/opt/casa/bin']
lib_paths=['/usr/local/miriad-carma/opt/casa/lib']
extenv={"PATH":os.pathsep.join(list(set(bin_paths))),
        "DYLD_LIBRARY_PATH":os.pathsep.join(list(set(lib_paths))),
        "HOME":"~/"}

#   if some project-related scripts exist, load thenm
for name in filesearch(os.path.dirname(xlib_path)+'/scripts/*/*config.py'):
    print 'run: '+name
    execfile(name)

#   if macports modules exist, add them
mp_path='/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages'
if  os.path.exists(mp_path):
    sys.path.insert(1,mp_path)

#   if experimental modules exist, import them
exp_path=xlib_path+'/xexp.py'
if  os.path.exists(exp_path):
    import xexp as xe

#   if the au module exist, add it
au_path=os.path.dirname(xlib_path)+'/borrow/analysis_scripts'
if  os.path.exists(au_path):
    sys.path.insert(1,au_path)
    import analysisUtils as au

print ""
print "+"*80
print ""


