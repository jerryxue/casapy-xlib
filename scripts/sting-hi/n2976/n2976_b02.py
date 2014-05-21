#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2976_b02.inp
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

prefix   = 'n2976b02' 
rawfiles = ['../raw/AB1038_2','../raw/AB1038_3','../raw/AB1038_4','../raw/AB1038_5',
			'../raw/AB1038_6','../raw/AB1038_7','../raw/AB1038_8']
import_spw='0'

# TRACK INFORMATION
source = 'NGC2976'

fluxcal = '1331+305'
phasecal = '0921+622'

spw_source = '0'
spw_edge='0:0~3;57~62'

# CALIBRATION & OPTIONS
flagselect =	[
					" antenna='VA08&VA12' ",
					" timerange='24:55:50~25:40:00' ",
					" timerange='17:11:40~17:36:40' ",
					" antenna='VA02&VA06'",
					" antenna='VA06&VA22'"
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
