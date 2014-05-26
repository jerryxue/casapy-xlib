#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_d.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='300km/s'
clean_nchan=58
clean_width='2.6km/s'

phase_center='J2000 02h59m42.2 +25d14m14.0'

uvcs=True

line_vrange=[280,460]

######################################################
#               track-dependent setting
######################################################

# ---------- C ARRAY REDUCTION
prefix   = 'n1156d' 
rawfiles = '../raw/AM418_4'

# TRACK INFORMATION
source = 'NGC1156'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0318+164' 
phasecal_uvrange='<100klambda'
passcal= '0137+331'
passcal_uvrange='<40klambda'

spw_source = '0,1'
spw_edge='*:0~3;123~126'

# CALIBRATION & OPTIONS
flagselect = [	"timerange='22:00:00~24:43:20'",
				"mode='quack' quackinterval=3.0",
				"antenna='VA08&VA15' timerange='23:20:42~23:20:48'",
				"antenna='VA10&VA11' timerange='25:41:42~25:41:48'",
				"antenna='VA08&VA15' spw='0' timerange='23:46:25~23:46:35'",
				"antenna='VA09&VA11' spw='0' timerange='24:50:20~24:50:40'",
				"antenna='VA09&VA11' spw='0' timerange='25:03:00~25:04:00'",
				"antenna='VA22&VA11' spw='0' timerange='25:03:00~25:04:00'",
				"antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
				"antenna='VA21&VA11' spw='0' timerange='25:18:25~25:18:35'",
				"antenna='VA03&VA11' spw='0' timerange='26:50:20~26:50:40'",
				"antenna='VA11&VA28' spw='0' timerange='26:53:40~26:54:40'",
				"uvrange='<500lambda' field='0137+331' timerange='22:33:20~24:46:40'",
				"uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
				"uvrange='<500lambda' field='0318+164' timerange='22:33:20~24:56:40'",
				"uvrange='<500lambda' field='NGC1156' timerange='23:23:20~24:30:00'"]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~7;119~122,1:4~7;119~122'
fit_order  = 1

n_iter=0


# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')