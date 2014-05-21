#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n1156_c.inp
# by Rui on Wed Feb 13 20:47:13 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='300km/s'
clean_nchan=58
clean_width='2.6km/s'

phase_center='J2000 02h59m42.2 +25d14m14.0'

uvcs=True

line_vrange=[280,460]

######################################################
#               track-dependent setting
######################################################

# ---------- C ARRAY REDUCTION
prefix   = 'n1156c' 
rawfiles = ['../raw/AM418_1','../raw/AM418_2','../raw/AM418_3']
import_starttime = '1993/08/09/10:59:45.0'
import_stoptime ='1993/08/09/16:28:15.0'

# TRACK INFORMATION
source = 'NGC1156'

fluxcal = '0137+331'
fluxcal_uvrange='<40klambda'
phasecal = '0318+164' 
phasecal_uvrange='<100klambda'
passcal= '0137+331'
passcal_uvrange='<40klambda'

spw_source = '0,1'
spw_edge='*:0~3;123~126'

# CALIBRATION & OPTIONS
flagselect = [	"mode='quack' quackinterval=3.0",
				"antenna='VA23' spw='1'",
				"antenna='VA09&VA11' ",
				"antenna='VA02&VA11' ",
				"antenna='VA11&VA21' ",
				"antenna='VA11&VA21' ",
				"antenna='VA10&VA11'",
				"antenna='VA11&VA27'",
				"antenna='VA11&VA14'",
				"antenna='VA11&VA22'"
				]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~7;119~122,1:4~7;119~122'
fit_order  = 1

im_size=512
cell_size='4.0arcsec'
phase_center='J2000 02h59m42.2 +25d14m14.0'
n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
