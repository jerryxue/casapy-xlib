#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_d03.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='-115km/s'
clean_nchan=24
clean_width='10.4km/s'

phase_center='J2000 09h47m15.40 67d54m59.00'

uvcs=True

line_vrange=[-105,95]

######################################################
#               track-dependent setting
######################################################

# ---------- C ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = ['../raw/AB1038_15','../raw/AB1038_16']
import_starttime='2003/05/10/02:46:15.0'
import_stoptime='2003/05/10/04:21:55.0'
import_spw='0'
import_field=['NGC2976','1331+305','0921+622']

# TRACK INFORMATION
source = 'NGC2976'

fluxcal = '1331+305'
phasecal = '0921+622'

spw_source = '0'
spw_edge='0:0~4;57~62'

# CALIBRATION & OPTIONS
flagselect =	[
					"mode='quack' quackinterval=5.0 ",
					"antenna='VA20' timerange='03:20:14~03:20:16'",
					"antenna='VA20&VA28' timerange='02:40:40~02:50:50'",
					"timerange='04:14:00~04:14:10' field='1331+305'"
					"antenna='VA03&VA09'",
					"antenna='VA02&VA17'",
					"antenna='VA09&VA19'",
					"antenna='VA15&VA27'",
					"antenna='VA03&VA10'",
					"antenna='VA03&VA27'",
					"antenna='VA16&VA26'",
					"antenna='VA14&VA27'",
					"antenna='VA08&VA11'",
					"antenna='VA11&VA20'",
					"antenna='VA10&VA15'",
					"antenna='VA05&VA16'",	
					"antenna='VA14&VA15'",	
					"antenna='VA01&VA05'",	
					"antenna='VA09&VA18'",	
					"antenna='VA09&VA27'",
					"antenna='VA03&VA15'",
					"antenna='VA03&VA17'",
					"antenna='VA10&VA27'",
					"antenna='VA03&VA19'",
					"antenna='VA08&VA14'",
					"antenna='VA09&VA27'",
					"antenna='VA10&VA14'",
					"antenna='VA02&VA07'",
					"antenna='VA18&VA19'"]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:5~12;53~56'
fit_order  = 1

n_iter=0


# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
