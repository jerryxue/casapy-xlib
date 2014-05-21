#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='25km/s'
clean_nchan=24
clean_width='10.4km/s'

phase_center='J2000 12h34m27.1 +02d11m16.0'

uvcs=True

line_vrange=[35,255]



######################################################
#               track-dependent setting
######################################################


# ---------- B+C ARRAY COMBINATION 
prefix_combine=['../b/n4605b','../c/n4605c']
prefix='n4605hi'

# CLEANING, IMAGING, & ANALYSIS
im_size=(512+256)*2
cell_size='2.0arcsec'

#multi_scale=[0,3,15]
#clean_gain=0.3
#cycle_factor=5.0

min_pb=0.1


# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
