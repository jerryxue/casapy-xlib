#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5371_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5371_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2300km/s'
clean_nchan=33
clean_width='20.8km/s'

phase_center='J2000 13h55m39.9 +40d27m42.0'

uvcs=True

line_vrange=[2330,2770]

######################################################
#               track-dependent setting
######################################################


# ---------- D 87Jun ARRAY REDUCTION

prefix   = 'n5371hi' 
rawfiles = ['../raw/AG559_1']
import_scan='8~10,17'

# TRACK INFORMATION
source = 'NGC5371'
fluxcal = '1409+524'
phasecal = '1419+419'

spw_source = '2'
spw_fluxcal= '1'
spw_phasecal='2'

spw_edge = '*:0~20;60~62'

# CALIBRATION & OPTIONS
flagselect=["antenna='VA02'","antenna='VA06&VA17'"]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '2:21~31;56~59'
fit_order  = 1

im_size=128+64
cell_size='20.0arcsec'

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

min_pb=0.25




# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
