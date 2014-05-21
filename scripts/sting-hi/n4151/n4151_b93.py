#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_b93.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
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


# ---------- C ARRAY REDUCTION
prefix   = 'n4151b93' 
rawfiles = ['../raw/AP251_9','../raw/AP251_10']
import_starttime = '1993/04/23/22:58:15.0'
import_stoptime = '1993/04/24/10:31:15.0'

# TRACK INFORMATION
source = 'NGC4151'
spw_source='0'

fluxcal = '1328+307'
fluxcal_uvrange=''
spw_fluxcal='0'

phasecal = '1225+368' 
phasecal_uvrange=''
spw_phasecal='0'

spw_edge='*:0~4;58~62'

# CALIBRATION & OPTIONS
flagselect = [ 	"antenna='VA11'",
				"mode='quack' quackinterval=4.0",
				"timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA21&VA22'",
				"timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA21'",
				"timerange='1993/04/24/05:26:40~06:33:20' field='1328+307' antenna='VA14&VA22'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:5~15;47~57'
fit_order  = 1

im_size=512+256
cell_size='4.0arcsec'

n_iter=20000






# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
