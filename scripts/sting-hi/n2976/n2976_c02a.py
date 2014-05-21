#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_c02a.inp
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

prefix   = 'n2976c02a' 
rawfiles = ['../raw/AT285_9','../raw/AT285_10']
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
					" antenna='VA07&VA08' timerange='13:36:30~13:37:00' ",
					" antenna='VA03&VA15' timerange='13:38:20~13:45:00' ",
					" antenna='VA03&VA15' timerange='13:40:00~14:46:40' ",
					" antenna='VA14&VA15' ",
					" antenna='VA02&VA24' ",
					" antenna='VA03&VA15' ",
					" antenna='VA02&VA15' ",
					" antenna='VA02&VA03' ",
					" antenna='VA02&VA03' timerange='13:40:00~14:46:40' ",
					" mode='quack' quackinterval=10. ",
					" antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' \
						timerange='13:38:20~13:45:00' ",
					" antenna='VA02&VA14;VA02&VA15;VA02&VA24;VA06&VA08;VA06&VA24;VA03&VA24' \
						timerange='14:00:00~14:13:20' ",
					" antenna='VA03&VA14' timerange='13:38:20~15:00:00' "	
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
