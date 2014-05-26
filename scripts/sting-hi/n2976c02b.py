#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_c02b.inp
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
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AB1038_11','../raw/AB1038_12']
import_spw='0'

# TRACK INFORMATION
source = 'NGC2976'

fluxcal = '1331+305'
phasecal = '0921+622'

spw_source = '0'
spw_edge='*:0~3;57~62'

# CALIBRATION & OPTIONS

flagselect =	[
					"antenna='VA07&VA08'",
					"mode='quack' quackinterval=3.0",
					"antenna='VA20' timerange='10:45:40.0~10:45:50.0'",
					"timerange='11:02:00.0~11:02:10.0'",
					"antenna='VA15'",
					"antenna='VA09&VA18'",
					"antenna='VA11&VA14'",
					"antenna='VA03&VA14'",
					"antenna='VA02&VA03'",
					"antenna='VA09&VA14'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~12;53~56'
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
