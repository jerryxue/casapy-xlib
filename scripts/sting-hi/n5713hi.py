#
# this CASA reduction script was automatically generated from configuration files:
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_config.inp
#   /Users/Rui/Dropbox/Worklib/casapy/scripts/sting-hi/n5713_comb.inp
# by Rui on Wed Feb 13 20:47:17 CST 2013
#

######################################################
#              track-independent setting
######################################################

clean_mode = 'velocity'
clean_start='1680km/s'
clean_width='20.8km/s'
clean_nchan=23

phase_center='J2000 14h40m11.5 -00d17m20.3'

imcs=True
fit_chans  = '0~2,20~22'
fit_order  = 1


line_vrange=[1760,2060]

######################################################
#               track-dependent setting
######################################################


# ---------- C+D ARRAY COMBINATION 
prefix_combine=['../c92/n5713c92','../d99/n5713d99']
prefix=os.path.splitext(os.path.basename(os.path.realpath(inspect.stack()[0][1])))[0]

# CLEANING, IMAGING, & ANALYSIS

im_size=512+128
cell_size='4.0arcsec'

wt_scale=[4,1]
multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0

# RUN SCRIPTS:
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
