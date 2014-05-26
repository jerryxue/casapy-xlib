#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_comb.inp
# by Rui on Wed Feb 13 20:47:14 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2300km/s'
clean_nchan=49
clean_width='10.4km/s'

phase_center='J2000 09h14m05.1 +40d06m49.0'

uvcs=True

line_vrange=[2390,2725]

######################################################
#               track-dependent setting
######################################################

# ---------- B+C+D ARRAY COMBINATION 
prefix_combine=['../ab/n2782ab','../c/n2782c','../d/n2782d']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

im_size=512*2
cell_size='2.0arcsec'

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
