# ---------- B+C+D ARRAY COMBINATION 

track_list = [      'C1',
					'C2',
					'C3',
					'C4',
					'C5',
					'C6',
					'C7',
					'C8']


telescopes = [	    'CARMA',
					'CARMA',
					'CARMA',
					'CARMA',
					'CARMA',
					'CARMA',
					'CARMA',
					'CARMA']

mirfile_list=	[	'../../sdi/n2976/vis/ngc2976_C1_10SEP30.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C2_10OCT02.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C3_10OCT12.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C4_10OCT13.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C5_10OCT13.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C6_10OCT14.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C7_10OCT29.13co.cal',
					'../../sdi/n2976/vis/ngc2976_C8_10NOV01.13co.cal']


for i in range(0,len(mirfile_list)):
	rawfiles=mirfile_list[i]
 	prefix=track_list[i]+'.src'
 	telescope=telescopes[i]
 	importmode='mir'
 	execfile(script_home+'ximport'+script_version+'.py')
 	
# ---------- IMAGE DATA 

prefix_combine=track_list
prefix='n2976co13'

# CLEANING, IMAGING, & ANALYSIS
clean_mode = 'velocity'
clean_start='-100km/s'
clean_nchan=(200)/5+1
clean_width='5km/s'
rest_freq='110.201353GHz'
out_frame='LSRK'

phase_center='J2000 09h47m15.40 67d54m59.00'
im_size=350
cell_size='1arcsec'

multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0
neg_component=0
usevconcat=False
spinterpmode='nearest'

# RUN SCRIPTS
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')