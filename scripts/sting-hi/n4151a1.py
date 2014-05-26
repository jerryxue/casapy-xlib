#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_a1.inp
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
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AM591_14','../raw/AM591_15']
import_starttime = '1998/05/12/01:59:25.0'
import_stoptime = '1998/05/12/03:14:35.0 '

# TRACK INFORMATION
source = 'NGC4151'
spw_source='0'

fluxcal = '1328+307'
fluxcal_uvrange=''
phasecal = '1223+395' 
phasecal_uvrange='>20klambda'

spw_edge='*:0~4;58~62'

# CALIBRATION & OPTIONS
flagselect = 	[
				"mode='quack' quackinterval=6.0",
				"timerange='02:09:10~02:09:20' antenna='VA23&VA26'",
				"timerange='03:14:20~03:14:30' antenna='VA23&VA26'",
				"timerange='02:19:40~02:19:50' antenna='VA01&VA26'",
				"timerange='02:34:50~02:34:58'",
				"timerange='02:39:40~02:39:50' antenna='VA01&VA28'",
				"mode='quack' quackinterval=30.0 field='1328+307'",
				"timerange='02:35:00~02:35:20' field='1328+307'",
				#"uvrange(<40000lambda' field(1328+307)",
				"antenna='VA14'",
				"antenna='VA15&VA27' field='1223+395'"
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
