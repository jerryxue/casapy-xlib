#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4151_c1.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
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
prefix   = 'n4151c1' 
rawfiles = '../raw/AP104_1'
import_band = 'L'
import_spw='0'
import_starttime = '1985/09/12/15:10:15.0'
import_stoptime ='1985/09/12/19:43:15.0'

# TRACK INFORMATION
source = 'N4151'

fluxcal = '3C286'
fluxcal_uvrange=''
phasecal = '1216+487' 
phasecal_uvrange=''
passcal= '3C286'
passcal_uvrange=''

spw_source = '0'
spw_edge=0

# CALIBRATION & OPTIONS

flagselect=		[	"antenna='VA20'",
					"antenna='VA18&VA27' timerange='1985/09/12/16:14:10.0~1985/09/12/16:14:20.0'",
					"uvrange='<500lambda' field='1216+487'",
					"timerange='1985/09/12/18:45:00.0~1985/09/12/18:45:30.0'"
				]
ref_ant='16'

# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:0~7;23~30'
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
