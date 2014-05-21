#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_comb.inp
# by Rui on Wed Feb 13 20:47:16 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='740km/s'
clean_nchan=24
clean_width='20.8km/s'

phase_center='J2000 12h10m32.6 +39d24m21.0'

uvcs=True

line_vrange=[865,1120]


######################################################
#               track-dependent setting
######################################################


# ---------- C ARRAY COMBINATION 
prefix_combine=['../c1/n4151c1','../c2/n4151c2',
				'../b93/n4151b93',
				'../a1/n4151a1']
prefix='n4151hi'

# CLEANING, IMAGING, & ANALYSIS

im_size=512+256
cell_size='4.0arcsec'

wt_scale=[5500,3500,4.0,1.0]

multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0




# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
