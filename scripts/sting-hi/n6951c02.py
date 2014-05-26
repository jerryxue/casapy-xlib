#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n6951_c02.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1210km/s'
clean_nchan=20
clean_width='20.8km/s'

phase_center='J2000 20h37m14.1 +66d06m20.0'

uvcs=True

line_vrange=[1225,1607]

######################################################
#               track-dependent setting
######################################################

# ---------- C 02Oct ARRAY REDUCTION

prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AM737_1','../raw/AM737_2']

# TRACK INFORMATION
source = 'NGC6951'

fluxcal = '0542+498'
fluxcal_uvrange=''
phasecal = '2022+616'
phasecal_uvrange=''

spw_source = '0,1'
spw_edge = '0:0~10;28~30,1:0~2;21~30'

# CALIBRATION & OPTIONS
flagselect = [  "timerange='2002/10/18/00:31:45.0~2002/10/20/00:31:45.0'",
                "antenna='VA10'",
                "timerange='2002/10/20/02:56:35~2002/10/20/02:56:55'",
                "timerange='2002/10/20/04:03:35~2002/10/20/04:03:55'",
                "timerange='27:46:20~27:47:00'",
                "timerange='26:37:00~30:00:00' field='NGC6951'",
                "timerange='26:37:00~30:00:00' field='2022+616'"
			 	]
 

# CLEANING, IMAGING, & ANALYSIS
fit_spw    = '0:11~17,1:14~20'
fit_order  = 1

n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
