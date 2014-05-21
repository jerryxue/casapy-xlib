#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0772_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0772_d99a.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2050.0km/s'
clean_width='20.8km/s'
clean_nchan=39

phase_center='J2000 01h59m19.58 +19d00m27.10'

uvcs=True

line_vrange=[2147,2735]

######################################################
#               track-dependent setting
######################################################

# ---------- D 99apr Track REDUCTION
prefix   = 'n0772bc13a_oh23' 
rawfiles = '/Volumes/Scratch/reduc/evla/n0772/13B-363.sb24382374.eb25239554.56540.51835789352.ms'
import_spw='6,16'
import_scan='2~15'
importmode='ms'
import_width=['8','8']

# TRACK INFORMATION
source = 'NGC0772'
spw_source='0,1'

fluxcal = '0137+331=3C48'
fluxcal_uvrange='<40klambda'
phasecal = 'J0204+1514'
phasecal_uvrange='<100klambda'

#spw_edge = "0:0~5;110~126"

# CALIBRATION & OPTIONS
# flagselect = [  "antenna='ea08' spw='*:16'",
#                 "antenna='ea16' spw='*:16'",
#                 "antenna='ea20' spw='*:16'",
#                 "antenna='ea25' spw='*:16'",
#                 "antenna='ea26' spw='*:16'",
#                 "antenna='ea28' spw='*:16'"
#                 ]            



# CLEANING, IMAGING, & ANALYSIS
fit_spw = '*:0~15;112~127'
fit_order  = 1

im_size=256
cell_size='12.0arcsec'

#multi_scale=[0,4,12]
#clean_gain=0.3
#cycle_factor=5.0

min_pb=0.1
restor_beam=['31.54arcsec', '16.66arcsec', '50.54deg']
rest_freq='1666380000Hz'
n_iter=0

# RUN SCRIPTS:
#execfile(script_home+'ximport'+script_version+'.py')
#execfile(script_home+'xcal'+script_version+'.py')
# execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
# checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
