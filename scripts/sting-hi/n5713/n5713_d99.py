#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_d99.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1680km/s'
clean_width='20.8km/s'
clean_nchan=23

phase_center='J2000 14h40m11.5 -00d17m20.3'

imcs=True
fit_chans  = '0~2,20~22'
fit_order  = 1


line_vrange=[1760,2060]

######################################################
#               track-dependent setting
######################################################

# ---------- D 99 Track REDUCTION

prefix   = 'n5713d99' 
rawfiles = ['../raw/AG559_2']
import_starttime='1999/04/25/11:04:45.0'
import_stoptime='1999/04/25/12:47:45.0'
import_field='NGC5713,1442+101,1409+524'

# TRACK INFORMATION
source = 'NGC5713'
spw_source='0'

fluxcal = '1409+524'
fluxcal_uvrange='<3klambda'
phasecal = '1442+101'
phasecal_uvrange=''

spw_edge = "*:0~5;56~62"

# CALIBRATION & OPTIONS
flagselect	=	[	"antenna='VA02'",	
					"antenna='VA12'",	
					"antenna='VA06&VA17'" , 
					"antenna='VA06&VA28'",
					"antenna='VA07&VA21'"
				]


fit_spw = "0:6~35;54~55"
n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
