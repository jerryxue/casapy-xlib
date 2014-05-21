#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_c06.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1450.00km/s'
clean_nchan=78
clean_width='5.2km/s'

phase_center='J2000 00h59m50.1 -07d34m41.0'

imcs=True
fit_chans    = '0~4;69~77'
fit_order  = 1

line_vrange=[1470,1800]

######################################################
#               track-dependent setting
######################################################

# IMPORTING
prefix   = 'n0337c06' 
rawfiles = '../raw/AM0873_3'
import_spw='0,1'
import_scan='6,8,10,12,14,16,18,30'

# TRACK INFORMATION
source = 'NGC0337'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0059+001'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~6;57~62'

# CALIBRATION & OPTIONS
flagselect= [	"timerange='04:38:30~04:51:20.0'",
				"antenna='VA11&VA21'",
				"antenna='VA06&VA21'",
				"antenna='VA06&VA11'",
				"antenna='VA03&VA04'",
				"timerange='2006/11/04/03:25:00~03:26:40' antenna='VA06&VA15'",
				"timerange='2006/11/04/02:28:40~02:29:30' antenna='VA07&VA15'",
				"timerange='2006/11/04/01:59:35~01:59:45'",
				"timerange='2006/11/04/03:07:15~03:07:25'",
				"timerange='2006/11/04/04:15:00~04:15:15'",
				"antenna='VA22'",
				"timerange='2006/11/04/10:03:45~10:04:15'",
				"timerange='2006/11/04/10:04:54~10:05:06'",
				"timerange='2006/11/04/10:06:04~10:06:16'",
				"timerange='03:00:00~11:00:00.0' antenna='VA03'",
				"antenna='VA11'",
				"antenna='VA06'",
				"antenna='VA05'",
				"timerange='2006/11/04/04:33:06~04:34:05'"
			]


# CLEANING, IMAGING, & ANALYSIS
fit_spw='1:7~10,0:52~56'

im_size=512+256+128
cell_size='4.0arcsec'
imstat_box_spec = '93,206,234,350'
n_iter=0

# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
