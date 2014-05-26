#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1569_c.inp
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

# ---------- C ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = ['../raw/AW325_6']
import_starttime='1993/06/29/12:06:45.0'
import_stoptime='1993/06/29/17:57:15.0'
#import_spw='0,1,4,5'

# TRACK INFORMATION
source = 'NGC1569'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0614+607_0'
phasecal_uvrange=''

spw_source = '4,5'
spw_fluxcal = '0,1'
spw_phasecal = '0,1,2,3'
spw_edge='*:0~10;112~126'

# CALIBRATION & OPTIONS
flagselect = 	[
				"mode='quack' quackinterval=6.0",
				"timerange='13:46:40~13:47:20'",
				"timerange='13:49:50~13:50:10'",
				"timerange='17:33:20~17:47:30.0'",
				"timerange='12:23:15.0~13:05:30.0'",
				"antenna='VA23&VA25'","antenna='VA03&VA23'",
				"antenna='VA11&VA12'",
				"antenna='VA19&VA25'",
				"antenna='VA19&VA23'",
				"antenna='VA06&VA19'",
				"antenna='VA04&VA25'",
				"antenna='VA18&VA23'",
				"antenna='VA17&VA24'",
				"antenna='VA12&VA20'",
				"antenna='VA05&VA20'",
				"antenna='VA05&VA18'",
				"antenna='VA04&VA23'",
				"antenna='VA04&VA18'",
				"antenna='VA03&VA04'",
				"antenna='VA11'",
				"antenna='VA02&VA23'",
				"antenna='VA04&VA05'",
				"antenna='VA04&VA19'",
				"antenna='VA03&VA25'",
				"antenna='VA02&VA03'",
				"antenna='VA03&VA19'",
				"scan='2'",
				"scan='4'"
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
