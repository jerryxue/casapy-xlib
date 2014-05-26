#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_b06.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1210km/s'
clean_nchan=20
clean_width='20.8km/s'

phase_center='J2000 20h37m14.1 +66d06m20.0'

uvcs=True

line_vrange=[1225,1607]

######################################################
#               track-dependent setting
######################################################

# ---------- B 06Jul ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = ['../raw/AH912_7']
import_starttime="2006/07/01/08:05:05.0"
import_stoptime="2006/07/01/18:02:25.0"

# TRACK INFORMATION
source = 'NGC6951'

fluxcal = '1331+305'
phasecal = '2022+616'

spw_source = '0,1'
spw_edge = '*:0~6;57~62'

# CALIBRATION & OPTIONS
flagselect=	[	"mode='quack' quackinterval=25.0",
				"timerange='08:06:20~08:06:30'",
				"antenna='VA07'",
				"antenna='VA22'",
				"antenna='VA04&VA06'",
				"timerange='15:11:40~15:12:10'",
				"timerange='13:26:05.0~13:26:25.0' antenna='VA17'",
				"antenna='VA06&VA25' timerange='08:55:45.0~08:56:05.0'",
				"antenna='VA06&VA25' timerange='09:35:35.0~09:35:55.0'",
				"timerange='17:03:35.0~17:03:55.0'",
				"antenna='VA11&VA21' timerange='13:23:20~14:13:20'",
				"antenna='VA06&VA28' timerange='17:02:25~17:02:45'",
				"timerange='16:30:35.0~16:30:55.0' antenna='VA06&VA25'",
				"timerange='11:15:15.0~11:15:35.0' antenna='VA06&VA17'",
				"timerange='14:35:55.0~14:36:20.0' antenna='VA06&VA17'",
				"timerange='15:37:45.0~15:38:05.0'",
				"timerange='17:00:00.0~17:00:10.0' antenna='VA06&VA17'"
			]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '1:7~15,0:48~56'
fit_order  = 1

n_iter=0


# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
