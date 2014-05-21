#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_c.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='25km/s'
clean_nchan=24
clean_width='10.4km/s'

phase_center='J2000 12h34m27.1 +02d11m16.0'

uvcs=True

line_vrange=[35,255]



######################################################
#               track-dependent setting
######################################################


# ---------- C ARRAY REDUCTION
prefix   = 'n4605c' 
rawfiles = ['../raw/AB1038_8',
		'../raw/AB1038_9',
		'../raw/AB1038_10']
import_starttime='2002/12/19/07:54:45'
import_stoptime='2002/12/19/11:45:15'
import_spw='0'

# TRACK INFORMATION
source = 'NGC4605'

fluxcal = '1331+305'
phasecal = '1313+675' 

spw_source = '0'
spw_edge = '*:0~4;57~62'

# CALIBRATION & OPTIONS
flagselect = ["antenna='VA20'",
			"antenna='VA07&VA08'",
			"antenna='VA08&VA10'",
			"antenna='VA15&VA28'",
			"antenna='VA14&VA16'"]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:5~7;54~56'
fit_order  = 1

n_iter=0
min_pb=0.1





# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
