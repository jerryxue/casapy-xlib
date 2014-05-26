#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_comb.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='-115km/s'
clean_nchan=24
clean_width='10.4km/s'

phase_center='J2000 09h47m15.40 67d54m59.00'

uvcs=True

line_vrange=[-105,95]

######################################################
#               track-dependent setting
######################################################

# ---------- B+C+D ARRAY COMBINATION 
prefix_combine=[	'../b02/n2976b02',
					'../c02a/n2976c02a',
					'../c02b/n2976c02b',
					'../c03/n2976c03',
					'../d03/n2976d03',
					'../c08a/n2976c08a',
					'../c08b/n2976c08b']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS
im_size=512+256+256
cell_size='2.0arcsec'


#multi_scale=[0,4,12]
#clean_gain=0.3
cycle_factor=5.0

# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
