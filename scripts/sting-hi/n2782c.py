#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_c.inp
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

# ---------- C ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = '../raw/AS453_4'


# TRACK INFORMATION
source = 'NGC2782'

fluxcal = '1328+307'
fluxcal_uvrange=''
phasecal = '0859+470'
phasecal_uvrange='<15klambda'

spw_source = '0'
spw_edge='*:0~3;58~62'

# CALIBRATION & OPTIONS
flagselect = 	[
					"timerange='01:09:00~01:09:20'",
					"timerange='02:39:10~02:40:00'",
					"timerange='02:52:00~02:54:10' antenna='VA13&VA17'",
					"timerange='03:10:00~03:15:00' antenna='VA13&VA17;VA17&VA19'",
					"timerange='03:20:50~03:24:10'",
					"timerange='03:40:00~03:43:20'",
					"timerange='03:57:30~04:00:50'",
					"timerange='04:09:10~04:10:00'",
					"timerange='04:35:50~04:40:00'",
					"timerange='02:51:40~02:54:10'",
					"timerange='03:10:50~03:13:20'",
					"timerange='04:25:50~04:28:00'",
					"timerange='04:54:10~04:55:00'",
					"antenna='VA11&VA20' timerange='03:00:00~03:06:40'"
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
