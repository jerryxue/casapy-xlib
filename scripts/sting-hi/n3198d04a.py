#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_d04a.inp
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
rawfiles = ['../raw/AW605_13']
import_starttime='2004/07/09/19:12:05.0'
import_stoptime='2004/07/09/23:09:05.0'
import_scan='1,18~25'
import_spw='0,1'

# TRACK INFORMATION
source = 'NGC3198'
spw_source='0,1'

fluxcal = '0542+498'
fluxcal_uvrange='<50klambda'
phasecal = '1035+564'
phasecal_uvrange=''

spw_edge =6

# CALIBRATION & OPTIONS
flagselect = [  "timerange='2004/07/09/22:03:28.0~22:04:32' field='NGC3198'",
				"timerange='2004/07/09/22:26:56.0~22:27:45' field='NGC3198'",
				"timerange='2004/07/09/21:33:44.0~21:34:34' field='NGC3198'",
				"timerange='2004/07/09/21:41:03.0~21:41:06' field='NGC3198'",
				"timerange='2004/07/09/21:52:07.0~21:55:31' field='NGC3198'",
				"timerange='2004/07/09/22:57:18.0~22:57:30' field='NGC3198'",
				"timerange='2004/07/09/22:58:11.0~23:03:05' field='NGC3198'",
				"timerange='2004/07/09/22:29:23.5~22:29:28.3' field='NGC3198'",
				"timerange='2004/07/09/22:57:57.9~22:58:48.4' field='NGC3198'",
				"timerange='2004/07/09/21:48:54~21:49:58' field='1035+564'",
				"timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
				"timerange='2004/07/09/21:48:03~21:48:10' field='1035+564'",
				"timerange='2004/07/09/22:13:33~22:13:38' field='1035+564'",
				"timerange='2004/07/09/22:06:38.3~22:06:48' field='1035+564'",
				"timerange='2004/07/09/19:12:29~19:12:43' field='0542+498'",
				"timerange='2004/07/09/19:12:00~19:12:11' field='0542+498'",
				"timerange='2004/07/09/19:16:28~19:16:43' field='0542+498'",
				"timerange='2004/07/09/19:17:39~19:17:53' field='0542+498'",
				"mode='clip' cliprange='10~10000' field='NGC3198' clipexpr='ABS_RR'",
				"mode='clip' cliprange='10~10000' field='NGC3198' clipexpr='ABS_LL'",
				"antenna='VA22'",
				"antenna='VA26'",
				"mode='clip' cliprange='10~10000' field='1035+564' clipexpr='ABS_RR'",
				"mode='clip' cliprange='10~10000' field='1035+564' clipexpr='ABS_LL'",
				"uvrange='<600lambda' field='1035+564'",
				"mode='quack' quackinterval=15.0 field='1035+564'",
				"antenna='VA06&VA27' field='NGC3198' timerange='2004/07/09/22:08:00~2004/07/09/22:08:10'"
				]

 
# CLEANING, IMAGING, & ANALYSIS
fit_spw=''
n_iter=0




# RUN SCRIPTS:
execfile(script_home+'ximport'+script_version+'.py')
execfile(script_home+'xcal'+script_version+'.py')
execfile(script_home+'xcalplot'+script_version+'.py')
execfile(script_home+'xmerge'+script_version+'.py')
checkstatwt(prefix+'.src.ms',statwt_fitspw=fit_spw)
execfile(script_home+'xclean'+script_version+'.py')
