#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_c2.inp
# by Rui on Wed Feb 13 20:47:16 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='740km/s'
clean_nchan=24
clean_width='20.8km/s'

phase_center='J2000 12h10m32.6 +39d24m21.0'

uvcs=True

line_vrange=[865,1120]


######################################################
#               track-dependent setting
######################################################


# ---------- C ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AP104_2',
			'../raw/AP104_3',
			'../raw/AP104_4',
			'../raw/AP104_5']
import_band = 'L'
import_starttime = '1985/09/14/17:02:15.0'
import_stoptime ='1985/09/15/03:19:15.0'

# TRACK INFORMATION
source = 'N4151'

fluxcal = '3C286'
fluxcal_uvrange=''
phasecal = '1216+487' 
phasecal_uvrange=''

spw_source = '0'
spw_edge=0

# CALIBRATION & OPTIONS
flagselect = [  "antenna='VA20' timerange='24:55:00~24:56:40'",
				"antenna='VA18&VA27'",
				"antenna='VA11&VA27'",
				"antenna='VA06&VA19'",
				"antenna='VA08' timerange='17:08:00~17:16:40'",
				"timerange='19:15:00~19:15:50'",
				"antenna='VA11&VA18'",
				"antenna='VA21&VA27'",
				"antenna='VA21&VA25'",
				"antenna='VA25&VA27'",
				"antenna='VA06&VA18'",
				"antenna='VA18&VA21'",
				"scan='17~36'"
			]



# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:1~7;23~30'
fit_order  = 1

im_size=512+256
cell_size='4.0arcsec'

n_iter=20000







# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
