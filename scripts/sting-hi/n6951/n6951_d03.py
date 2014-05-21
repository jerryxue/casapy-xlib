#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_d03.inp
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

# ---------- D 03Apr ARRAY REDUCTION

prefix   = 'n6951d03' 
rawfiles = ['../raw/AS750_3',
			'../raw/AS750_4',
			'../raw/AS750_5']
import_starttime="2003/04/24/08:33:55.0"
import_stoptime="2003/04/24/12:01:25.0"

# TRACK INFORMATION
source = 'NGC6951'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '2022+616'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~6;57~62'

# CALIBRATION & OPTIONS
flagselect=[	"mode='quack' quackinterval=20.0", 
				"timerange='08:39:10~08:39:20'",
				"timerange='11:56:20~11:56:30'",
				"antenna='VA04&VA23' timerange='08:46:40~08:53:20' field='2022+616'",
				"antenna='VA04&VA23'",
				"antenna='VA28' timerange='10:00:35.0~10:00:55.0'",
				"field='1331+305' timerange='11:20:00~12:26:40'",
				"antenna='VA20&VA24'","antenna='VA20&VA12'"
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
