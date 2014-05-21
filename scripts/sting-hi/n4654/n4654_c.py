#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4654_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n4654_c.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='831km/s'
clean_nchan=47
clean_width='10.4km/s'

phase_center='J2000 12h43m56.6 +13d07m36.0'

uvcs=True

line_vrange=[830,1200]


######################################################
#               track-dependent setting
######################################################


# ---------- C ARRAY REDUCTION
prefix   = 'n4654c' 
rawfiles = ['../raw/AP206_2']

# TRACK INFORMATION
source = 'NGC4654'

fluxcal = '1331+305'
phasecal = '1221+282'

spw_source = '0'
spw_edge = '*:0~5;58~62'

# CALIBRATION & OPTIONS
flagselect=	[	"timerange='1992/03/12/04:03:20~1992/03/12/04:06:40'",
				"timerange='1992/03/12/10:16:25.0~1992/03/12/10:16:35.0'"
			]


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:6~19;55~57'
fit_order  = 1

n_iter=0


# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
