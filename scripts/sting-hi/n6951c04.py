#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_c04.inp
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

# ---------- C 04May ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AS787_6']
import_starttime="2004/05/10/10:31:05.0"
import_stoptime="2004/05/10/13:53:05.0 "

# TRACK INFORMATION
source = 'NGC6951'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '2022+616'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~6;57~62'

# CALIBRATION & OPTIONS
flagselect=	[	"timerange='2004/05/10/12:51:59~2004/05/10/12:54:22'",
				"timerange='2004/05/10/12:59:33~2004/05/10/15:59:33'",
				#"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_RR'",
				#"field='1331+305' mode='clip' cliprange='10~1000' clipexpr='ABS_LL'",
				"antenna='VA22' ",
				"mode='quack' quackinterval=20.0",
				"antenna='VA06' timerange='10:33:30~11:33:40'",
				"timerange='12:13:20~13:03:20' field='NGC6951'",
				"timerange='12:47:40.0~12:47:50.0' antenna='VA06&VA08'",
				"timerange='10:38:00~10:38:10' field='2022+616'",
				"antenna='VA06&VA12'","antenna='VA06&VA28'",
				"antenna='VA04'",
				"antenna='VA06'",
				"antenna='VA18&VA25'","antenna='VA11&VA21'"
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