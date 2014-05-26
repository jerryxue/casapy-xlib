#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1210km/s'
clean_nchan=20
clean_width='20.8km/s'

phase_center='J2000 20h37m14.1 +66d06m20.0'

uvcs=True

line_vrange=[1225,1607]

######################################################
#               track-dependent setting
######################################################

# ---------- B+C+D ARRAY COMBINATION
prefix_combine=['../d03/n6951d03',
				'../c04/n6951c04',
				'../b06/n6951b06',
				'../c02/n6951c02']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS
im_size=512
cell_size='4.0arcsec'

wt_scale=[1,1,1,1.5]
multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0


# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
