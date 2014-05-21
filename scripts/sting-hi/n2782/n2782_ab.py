#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n2782_ab.inp
# by Rui on Wed Feb 13 20:47:14 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='2300km/s'
clean_nchan=49
clean_width='10.4km/s'

phase_center='J2000 09h14m05.1 +40d06m49.0'

uvcs=True

line_vrange=[2390,2725]

######################################################
#               track-dependent setting
######################################################

# ---------- ab ARRAY REDUCTION
prefix   = 'n2782ab' 
rawfiles = '../raw/AS453_3'


# TRACK INFORMATION
source = 'NGC2782'

fluxcal = '0134+329'
fluxcal_uvrange='<40klambda'
phasecal = '0917+449'
phasecal_uvrange='<20klambda'

spw_source = '0'
spw_edge='*:0~3;58~62'

# CALIBRATION & OPTIONS

flagselect = 	[
					"timerange='06:10:40~06:10:50' field='0134+329'",
					"timerange='06:12:20~06:13:00' field='0134+329'",
					"antenna='VA01&VA12'"
				]		


# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:4~12;47~57'
fit_order  = 1

n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
