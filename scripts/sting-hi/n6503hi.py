#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6503_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6503_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2288km/s'
clean_nchan=34
clean_width='20.8km/s'

phase_center='J2000 13h55m39.9 +40d27m42.0'

uvcs=True

line_vrange=[1760,2060]

######################################################
#               track-dependent setting
######################################################


# ---------- D 87Jun ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = ['../raw/AD211_A880125.xp1']
import_spw='3,8'

# TRACK INFORMATION
source = 'NGC5371'
fluxcal = '1409+524'
phasecal = '1419+419'

spw_source = '2'
spw_fluxcal= '1'
spw_phasecal='2'

spw_edge = '*:0~20;58~62'

# CALIBRATION & OPTIONS
flagselect=["antenna='VA02'","antenna='VA06&VA17'"]


# CLEANING, IMAGING, & ANALYSIS

fit_spw    = '0:21~23;55~57'
fit_order  = 1


im_size=512+128

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

min_pb=0.25



# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
