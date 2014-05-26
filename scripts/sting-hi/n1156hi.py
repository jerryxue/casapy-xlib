#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_comb.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='300km/s'
clean_nchan=58
clean_width='2.6km/s'

phase_center='J2000 02h59m42.2 +25d14m14.0'

uvcs=True

line_vrange=[280,460]

######################################################
#               track-dependent setting
######################################################

# ---------- B+C+D ARRAY COMBINATION 

prefix_combine=['../b/n1156b',
				'../c/n1156c',
				'../d/n1156d']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

im_size=1024
cell_size='2arcsec'

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

min_pb=0.2

# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
