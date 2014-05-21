#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n0337_d03.inp
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
prefix   = 'n0337d03' 
rawfiles = '../raw/AT285_1'
import_scan='2~5'

# TRACK INFORMATION
source = 'NGC0337'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0059+001'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~6;57~62'

# CALIBRATION & OPTIONS
flagselect = [  "timerange='2003/02/16/22:06:02~22:06:30' field='0137+331'",
				"antenna='VA08&VA11'",
				"antenna='VA20&VA11'",
				"antenna='VA03&VA08'",
				"antenna='VA03&VA09'",
				"antenna='VA03&VA10'",
				"antenna='VA14&VA27'",
				"antenna='VA08&VA14'",
				"antenna='VA08&VA10'",
				"antenna='VA04&VA20'",
				"antenna='VA10&VA15'",
				"antenna='VA09&VA19'",
				"antenna='VA02&VA03'"]


# CLEANING, IMAGING, & ANALYSIS
fit_spw='1:7~10,0:52~56'

im_size=256+128+64
cell_size='8.0arcsec'
imstat_box_spec = '42,103,117,175'
n_iter=0

# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
