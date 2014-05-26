#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_comb.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='-215km/s'
clean_nchan=50
clean_width='5.2km/s'

phase_center='J2000 04h30m49.06 64d50m52.61'

uvcs=True

line_vrange=[-170,5]

######################################################
#               track-dependent setting
######################################################

# ---------- B+C+D ARRAY COMBINATION 

prefix_combine=['../c/n1569c','../d/n1569d','../b/n1569b']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

im_size=512+256
cell_size='2.0arcsec'

imstat_box_spec = '72,96,284,686'
wt_scale=[4,4,1]
multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

min_pb=0.1


# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
