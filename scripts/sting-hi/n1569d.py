#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_d.inp
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

# ---------- D ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AW325_4','../raw/AW325_5']

# TRACK INFORMATION
source = 'NGC1569'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0614+607'
phasecal_uvrange=''

spw_source = '4,5'
spw_fluxcal = '0,1,2,3'
spw_phasecal = '0,1,2,3'
spw_edge='*:0~10;112~126'

# CALIBRATION & OPTIONS
flagselect = 	[
				"mode='quack' quackinterval=3.0",
				"antenna='VA16'",
				"timerange='1992/09/06/08:17:45~1992/09/06/08:19:45' antenna='VA28'",
				"timerange='1992/09/06/09:16:30~1992/09/06/09:18:30' antenna='VA28'",
				"timerange='1992/09/06/09:21:30~1992/09/06/09:23:30' antenna='VA28'",
				"timerange='1992/09/06/11:42:30~1992/09/06/11:44:30' antenna='VA28'",
				"timerange='1992/09/06/12:05:15~1992/09/06/12:07:15' antenna='VA28'",
				"timerange='1992/09/06/11:02:30~1992/09/06/11:04:15' antenna='VA28'",
				"antenna='VA10&VA28' timerange='1992/09/06/08:31:00~1992/09/06/08:31:40'",
				"antenna='VA12' timerange='08:29:10~08:35:30' field='0137+331'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '4:11~20;98~111,5:11~20;98~111'
fit_order  = 1

n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
