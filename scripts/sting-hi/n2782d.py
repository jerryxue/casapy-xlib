#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_d.inp
# by Rui on Wed Feb 13 20:47:14 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2300km/s'
clean_nchan=49
clean_width='10.4km/s'

phase_center='J2000 09h14m05.1 +40d06m49.0'

uvcs=True

line_vrange=[2390,2725]

######################################################
#               track-dependent setting
######################################################

# ---------- D ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AS389_1','../raw/AS389_2']
import_starttime='1989/12/10/06:49:15.0'
import_stoptime='1989/12/10/16:13:15.0'
import_spw='0'

# TRACK INFORMATION
source = 'NGC2782'

fluxcal = '1328+307'
fluxcal_uvrange='<40klambda'
phasecal = '0859+470'
phasecal_uvrange='<20klambda'

spw_source = '0'
spw_edge='*:0~3;58~62'

# CALIBRATION & OPTIONS
flagselect = 	[
					"timerange='10:50:00~10:52:20' antenna='VA09&VA12'",
					"timerange='13:15:00~13:17:00' antenna='VA09&VA12'",
					"timerange='09:23:20~09:26:40'",
					"timerange='09:33:20~09:36:40'",
					"timerange='09:51:40~09:53:20'",
					"timerange='10:00:00~10:01:40'",
					"timerange='10:19:10~10:20:00'",
					"timerange='10:38:20~10:39:10'",
					"timerange='12:56:40~12:57:30'",
					"timerange='14:40:00~14:41:40'",
					"timerange='14:48:20~14:50:00'",
					"timerange='15:06:40~15:10:00'",
					"timerange='13:17:30~13:19:10'",
					"timerange='15:13:20~15:20:00'",
					"timerange='11:00:40~11:01:20'",
					"timerange='10:51:10~10:52:00'",
					"timerange='15:25:00~15:50:00' field='NGC2782'",
					"uvrange='<500lambda' field='0859+470'",
					"timerange='10:10:00~10:11:40'",
					"timerange='11:14:10~11:15:50'",
					"timerange='11:21:40~11:23:20'",
					"timerange='15:20:00~15:21:40'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~11;47~57'
fit_order  = 1

n_iter=0

# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
