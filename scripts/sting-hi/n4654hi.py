#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4654_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4654_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='831km/s'
clean_nchan=47
clean_width='10.4km/s'

phase_center='J2000 12h43m56.6 +13d07m36.0'

uvcs=True

line_vrange=[830,1200]


######################################################
#               track-dependent setting
######################################################


# ---------- C+D ARRAY COMBINATION 

prefix_combine=['../c/n4654c','../d/n4654d']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS


im_size=1024
cell_size='4.0arcsec'
min_pb=0.10
 
multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
