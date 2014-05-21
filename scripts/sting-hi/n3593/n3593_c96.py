#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_c96.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='410km/s'
clean_nchan=88
clean_width='5.2km/s'

phase_center='J2000 11h14m37.0 +12d49m3.6'

uvcs=True

line_vrange=[470,770]


######################################################
#               track-dependent setting
######################################################

# ---------- C 96 ARRAY REDUCTION

prefix   = 'n3593c96' 
rawfiles = ['../raw/AC459_2','../raw/AC459_3','../raw/AC459_4']

# TRACK INFORMATION
source = 'NGC3593'

fluxcal = '1328+307'
fluxcal_uvrange=''
phasecal = '1117+146'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~4;57~62'

# CALIBRATION & OPTIONS
flagselect = [  " mode='quack' quackinterval=8.0 ",
                " timerange='03:42:30~03:43:00' ",
                " timerange='06:51:10~06:51:20' ",
                " timerange='05:02:30~05:02:50' ",
                " timerange='07:11:14~07:11:16' ",
                " timerange='07:53:40~07:53:50' ",
                " timerange='08:02:10~08:02:20' "
                ]


# CLEANING, IMAGING, & ANALYSIS
fit_spw = '0:5~18,1:45~56'
fit_order  = 1

n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
