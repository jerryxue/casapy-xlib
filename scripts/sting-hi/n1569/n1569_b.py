#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_b.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='-215km/s'
clean_nchan=50
clean_width='5.2km/s'

phase_center='J2000 04h30m49.06 64d50m52.61'

uvcs=True

line_vrange=[-170,5]

######################################################
#               track-dependent setting
######################################################

# ---------- B ARRAY REDUCTION
prefix   = 'n1569b' 
rawfiles = '../raw/AW605_12'

# TRACK INFORMATION
source = 'NGC1569'

fluxcal = '0538+498'
fluxcal_uvrange='<50klambda'
phasecal = '0404+768' 
phasecal_uvrange=''

spw_source = '4,5'
spw_fluxcal = '0,1,2,3'
spw_phasecal = '0,1,2,3'
spw_edge='*:0~10;112~126'

# CALIBRATION & OPTIONS
flagselect = [	"mode='quack' quackinterval=6.0",
				"antenna='VA26' timerange='05:54:10~05:55:10'",
				"antenna='VA26' timerange='05:54:10~05:55:10'",
				"antenna='VA09' timerange='11:01:40~11:05:50'",
				"antenna='VA06' timerange='06:54:10~06:54:20'",
				"timerange='11:00:00~11:10:00'",
				"antenna='VA11&VA18'",
				"timerange='05:09:40~05:10:15' field='0538+498'",
				"timerange='12:16:40~12:19:20' field='0538+498'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '4:11~20;98~111,5:11~20;98~111'
fit_order  = 1

im_size=512
cell_size='2.0arcsec'
n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
