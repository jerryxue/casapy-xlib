#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n3198_c02c.inp
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
rawfiles = ['../raw/AT285_8']

# TRACK INFORMATION
source = 'NGC3198'
spw_source='0,1'
import_starttime='2002/11/26/11:25:50'
import_stoptime='2002/11/26/12:19:50'

fluxcal = '1331+305'
fluxcal_uvrange=''
phasecal = '1006+349'
phasecal_uvrange='<30klambda'

spw_edge =6

# CALIBRATION & OPTIONS
flagselect = [	"timerange='2002/11/26/11:40:09~2002/11/26/11:40:10'",
				"timerange='2002/11/26/11:45:46~2002/11/26/11:45:53'",
				"timerange='2002/11/26/11:51:48~2002/11/26/11:51:54'",
				"timerange='2002/11/26/11:22:30~11:24:30'",
				"mode='quack' quackinterval=20.0 field='1006+349'",
				"antenna='VA09&VA14'",
				"antenna='VA07&VA08' timerange='11:40:00~11:40:20'"
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
