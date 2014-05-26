#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_c08a.inp
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
rawfiles = ['../raw/AC921_17']
import_starttime='2008/05/04/21:20:45.0'
import_stoptime='2008/05/04/23:13:15.0'

# TRACK INFORMATION
source = 'NGC2976'

fluxcal = '1331+305'
phasecal = '0841+708'
phasecal_uvrange='<20klambda'

spw_source = '0'
spw_edge='*:0~40;117~126'

# CALIBRATION & OPTIONS
flagselect = [
				"antenna='VA08&EA17'",
				"antenna='EA11&VA20'",
				"antenna='EA21'",
				"antenna='VA03&VA20'",
				"antenna='VA20&EA23' timerange='21:47:20.0~21:47:30.0'",
				"antenna='VA09&EA17' timerange='21:11:50.0~21:12:00.0'",
				"antenna='VA12&EA17' timerange='22:45:00.0~22:45:10.0'",
				"antenna='EA17&EA19' timerange='22:45:00.0~22:45:10.0'",
				"antenna='VA12&EA25'",
				"antenna='VA15&EA25'",
				"antenna='VA15&EA19'",
				"antenna='EA16&EA19'",
				"antenna='EA05&VA28'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:41~55;108~116'
fit_order  = 1

n_iter=0


# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
