#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_b.inp
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
prefix   = 'n1156b' 
rawfiles = ['../raw/AM418_5','../raw/AM418_6']

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

flagselect = [	"antenna='VA20&VA26'  spw='0' timerange='09:36:35~09:36:50'",
				"antenna='VA02&VA26'  spw='0' timerange='17:24:10~17:24:20'",
				"antenna='VA22&VA27'  spw='1' timerange='17:10:40~17:10:50'",
				"antenna='VA02&VA26'  spw='0' timerange='11:14:20~11:15:00'",
				"antenna='VA02&VA26'  spw='0' timerange='12:42:10~12:42:20'",
				"antenna='VA10&VA26'  spw='0' timerange='12:42:10~12:42:20'",
				"antenna='VA26' spw='0' timerange='17:13:42~17:13:48'",
				"antenna='VA17' spw='0'",
				"antenna='VA22' timerange='09:35:20~09:36:00'",
				"timerange='17:15:20~17:16:00' field='0137+331'",
				"timerange='13:28:00~13:29:20'",
				"antenna='VA27' timerange='14:59:00~14:59:40'",
				"timerange='17:10:40~17:11:00'",
				"timerange='09:41:40~09:41:50'",
				"antenna='VA10&VA26'",
				"antenna='VA26&VA28'",
				"antenna='VA20&VA26'",
 				"antenna='VA18&VA26'",
 				"antenna='VA23&VA26'",
 				"antenna='VA08&VA26'",
 				"antenna='VA02&VA26'",
 				"antenna='VA03&VA26'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~7;119~122,1:4~7;119~122'
fit_order  = 1

im_size=512+256
cell_size='2.0arcsec'
n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
