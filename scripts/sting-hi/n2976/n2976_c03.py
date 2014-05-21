#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_c03.inp
# by Rui on Wed Feb 13 20:47:14 CST 2013
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
prefix   = 'n2976c03' 
rawfiles = ['../raw/AT285_13','../raw/AT285_14']
import_field=['NGC2976','0841+708','0542+498']
import_scan='2~20'

# TRACK INFORMATION
source = 'NGC2976'

fluxcal = '0542+498'
fluxcal_uvrange='<50klambda'
phasecal = '0841+708'
phasecal_uvrange='<20klambda'

spw_source = '0,1'
spw_fluxcal='2,3,4,5'
spw_phasecal='2,3,4,5'
spw_edge='*:0~5;116~126'

# CALIBRATION & OPTIONS
flagselect =	[
					"mode='quack' quackinterval=3.0",
					"timerange='07:06:40~07:40:00' field='0542+498'",
					"antenna='VA07&VA08' timerange='07:32:08~07:32:12'",
					"antenna='VA14&VA15'",
					"antenna='VA09&VA15'",
					"antenna='VA03&VA15'",
					"antenna='VA02&VA03'",
					"antenna='VA03&VA14'",
					"antenna='VA09&VA18'",
					"antenna='VA11&VA14'",
					"antenna='VA02&VA09'",
					"antenna='VA07&VA08'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:6~11;110~115,1:6~11;110~115'
fit_order  = 1

n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
