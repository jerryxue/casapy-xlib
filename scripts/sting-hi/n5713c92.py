#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_c92.inp
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


# ---------- C 92 Track REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0] 
rawfiles = ['../raw/AP225_1']

# TRACK INFORMATION
source = 'NGC5713'
spw_source='0'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '1445+099'
phasecal_uvrange=''

spw_edge = "*:0~4;56~62"

# CALIBRATION & OPTIONS

flagselect	=	[	"timerange='12:33:40.0~12:36:30.0'"			]
 
# CLEANING, IMAGING, & ANALYSIS
fit_spw = "0:5~12;42~55"
n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
