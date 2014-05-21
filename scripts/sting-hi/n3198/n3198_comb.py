#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_comb.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='440.00km/s'
clean_width='10.4km/s'
clean_nchan=43

phase_center='J2000 10h19m54.92 +45d32m59.0'

imcs=True
fit_chans = '0~2,39~42'
fit_order=1

line_vrange=[470,830]

######################################################
#               track-dependent setting
######################################################

"""
Project     Data    Config  Comment
AT0285      02      C5.15   Good. 
							The Spectral Window Setting of file1,2,3 were strange (don't cover
							whole velocity range)
AT0285		03		D5.15
AW0605		04		D5.15
AW0605		05		B5.15 

CONCAT
"""

# ---------- C+D ARRAY COMBINATION 
prefix_combine=['../d04a/n3198d04a',
				'../d03b/n3198d03b',
				'../d03a/n3198d03a',
				'../c02d/n3198c02d',
				'../c02c/n3198c02c',
				'../c02b/n3198c02b',
				'../c02a/n3198c02a',
				'../b05/n3198b05']
prefix='n3198hi'

# CLEANING, IMAGING, & ANALYSIS

im_size=1024+256
cell_size='2arcsec'

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

min_pb=0.1


# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
