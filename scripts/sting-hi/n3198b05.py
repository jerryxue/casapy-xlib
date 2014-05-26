#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_b05.inp
# by Rui on Wed Feb 13 20:47:15 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='440.00km/s'
clean_width='10.4km/s'
clean_nchan=43

phase_center='J2000 10h19m54.92 +45d32m59.0'

imcs=True
fit_chans = '0~2,39~42'
fit_order=1

line_vrange=[470,830]

######################################################
#               track-dependent setting
######################################################

"""
Project     Data    Config  Comment
AT0285      02      C5.15   Good. 
							The Spectral Window Setting of file1,2,3 were strange (don't cover
							whole velocity range)
AT0285		03		D5.15
AW0605		04		D5.15
AW0605		05		B5.15 

CONCAT
"""

# ---------- C 02 Track REDUCTION
prefix   = os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]
rawfiles = ['../raw/AW605_14','../raw/AW605_15']
import_starttime='2005/04/26/23:21:25.0'
import_stoptime='2005/04/27/08:00:00.0'

# TRACK INFORMATION
source = 'NGC3198'
spw_source='0,1'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '1035+564'
phasecal_uvrange=''

spw_edge =6

# CALIBRATION & OPTIONS
flagselect = [  "timerange='2005/04/26/23:30:13.0~2005/04/26/23:30:18' field='0542+498'",
				"timerange='2005/04/27/06:00:45.0~2005/04/27/06:01:02' field='1035+564'",
				#"clipexpr(ABS I)++clipminmax(0,10)++field(1035+564)",
				#"antenna='VA09' corr(LL)++spw(0)",
				#"ant(VA18)++corr(LL)++spw(0)",
				#"ant(VA22)++corr(RR)++spw(1)",
				"timerange='2005/04/27/04:08:24.0~2005/04/27/04:08:26' field='NGC3198'",
				"timerange='2005/04/27/06:31:30.0~2005/04/27/06:31:40' field='NGC3198'",
				"timerange='2005/04/27/04:19:00.0~2005/04/27/04:20:00' field='NGC3198'",
				"timerange='2005/04/27/01:54:05.0~2005/04/27/01:54:25' field='NGC3198'",
				"timerange='2005/04/27/07:14:15~07:14:40' field='1331+305'",
				"antenna='VA04'","antenna='VA21&VA22'","antenna='VA12&VA28'",
				"timerange='2005/04/27/07:16:40~07:16:50' field='1331+305' antenna='VA28'",
				"mode='quack' quackinterval=20.0",
				"antenna='VA22'"
			]

 
# CLEANING, IMAGING, & ANALYSIS
fit_spw='1:6~20,0:48~56'

n_iter=0



# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
