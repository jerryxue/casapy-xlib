#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3593_d96.inp
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

# ---------- D 96 ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AC459_5','../raw/AC459_6']
import_scan='2~9'

# TRACK INFORMATION
source = 'NGC3593'

fluxcal = '1328+307'
fluxcal_uvrange=''
phasecal = '1117+146'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '*:0~4;57~62'

# CALIBRATION & OPTIONS
flagselect = [  "mode='quack' quackinterval=8.0 ",
                "timerange='23:25:40~23:26:20'",
                "timerange='23:32:40~23:50:00'",
                "antenna='VA17' timerange='23:30:00~23:31:00'",
                "antenna='VA16' timerange='22:13:00~22:13:30'",
                "antenna='VA16' timerange='22:32:30~22:33:00'",
                "antenna='VA16' timerange='23:01:30~23:02:00'",
                "antenna='VA01' timerange='22:44:00~22:44:30'",
                "timerange='22:48:00~22:48:30'",
                "antenna='VA28' timerange='22:58:30~22:59:00'"
                "uvrange='900lambda'",
                "timerange='23:26:30~23:27:00' field='1328+307' antenna='VA16'",
                "antenna='VA12' timerange='22:07:30~22:08:00'",
                "antenna='VA12' timerange='23:16:30~23:17:00'"
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
