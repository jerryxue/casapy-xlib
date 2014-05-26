#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4605_d.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='25km/s'
clean_nchan=24
clean_width='10.4km/s'

phase_center='J2000 12h34m27.1 +02d11m16.0'

uvcs=True

line_vrange=[35,255]



######################################################
#               track-dependent setting
######################################################


# ---------- D ARRAY REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AC168_1']


# TRACK INFORMATION
source = 'NGC4254'
fluxcal = '1331+305'
phasecal = '1221+282'

spw_source = '0'
spw_edge = '0:0~3;58~63'

# CALIBRATION & OPTIONS
flagselect=	[	"timerange='10:29:30~10:30:00'"
			]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~6;55~57'
fit_order  = 1

n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
