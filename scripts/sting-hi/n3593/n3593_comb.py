#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_comb.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='410km/s'
clean_nchan=88
clean_width='5.2km/s'

phase_center='J2000 11h14m37.0 +12d49m3.6'

uvcs=True

line_vrange=[470,770]


######################################################
#               track-dependent setting
######################################################

# ---------- C06+D03 ARRAY COMBINATION 
prefix_combine=['../c96/n3593c96','../d96/n3593d96']
prefix='n3593hi'

# CLEANING, IMAGING, & ANALYSIS

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0


# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
