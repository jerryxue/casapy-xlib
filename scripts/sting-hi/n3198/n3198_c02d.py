#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_c02d.inp
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

prefix   = 'n3198c02d' 
rawfiles = ['../raw/AT285_9','../raw/AT285_10']
import_starttime='2003/01/07/10:39:10.0'
import_stoptime='2003/01/07/23:00:00.0'

# TRACK INFORMATION
source = 'NGC3198'
spw_source='0,1'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '1006+349'
phasecal_uvrange='<30klambda'

spw_edge =6

# CALIBRATION & OPTIONS
flagselect = [	"timerange='2003/01/07/13:12:09~2003/01/07/13:12:10'",
				"mode='quack' quackinterval=20.0 field='1006+349'",
				"mode='quack' quackinterval=30.0 field='1331+305'",
				"timerange='2003/01/07/10:36:50.0~10:37:10.0'",
				"uvrange='<1300lambda' field='1006+349'",
				"timerange='13:12:00~13:12:20' field='1006+349'"
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
