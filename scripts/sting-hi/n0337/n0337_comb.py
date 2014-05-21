#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_comb.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1450.00km/s'
clean_nchan=78
clean_width='5.2km/s'

phase_center='J2000 00h59m50.1 -07d34m41.0'

imcs=True
fit_chans    = '0~4;69~77'
fit_order  = 1

line_vrange=[1470,1800]

######################################################
#               track-dependent setting
######################################################

# IMPORTING
prefix_combine=['../d03/n0337d03','../c06/n0337c06']
prefix='n0337hi'

# CLEANING, IMAGING, & ANALYSIS

im_size=384
cell_size='8.0arcsec'
imstat_box_spec = '34,153,164,278'

multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0
neg_component=0

# RUN SCRIPTS:
#execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
