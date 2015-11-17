# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D2','E1','C3','C4']
mirfile_list=[	'../../sdi/n3949/vis/ngc3949_C1_08nov06.13co.cal',
				'../../sdi/n3949/vis/ngc3949_C2_08nov08.13co.cal',
				'../../sdi/n3949/vis/ngc3949_D2_08aug19.13co.cal',
				'../../sdi/n3949/vis/ngc3949_E1_08oct03.13co.cal',
				'../../sdi/n3949/vis/ngc3949_C3_09oct12.13co.cal',
				'../../sdi/n3949/vis/ngc3949_C4_09oct17.13co.cal' ]
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	rawfiles=mirfile_list[i]
 	prefix=track_list[i]+'.src'
 	telescope=telescopes[i]
 	importmode='mir'
 	execfile(script_home+'ximport'+script_version+'.py')
 	
# ---------- IMAGE DATA 

prefix_combine=track_list
prefix='n3949co'

# CLEANING, IMAGING, & ANALYSIS
clean_mode = 'velocity'
clean_start='600km/s'
clean_nchan=(1000-600)/10+1 
clean_width='10km/s'
rest_freq='110.201353GHz'
out_frame='LSRK'

phase_center='J2000 11h53m41.4 +47d51m32.0'
im_size=350
cell_size='1arcsec'
clean_mask=0.5

multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0
neg_component=0

# RUN SCRIPTS
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')
