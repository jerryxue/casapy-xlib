# ---------- IMPORT DATA

track_list=['C1','C2','D1','D2','D5','D6','D7','E1']
mirfile_list=['../../sdi/n3147/vis/ngc3147_C1_08apr05.13co.cal',
				'../../sdi/n3147/vis/ngc3147_C2_08apr07.13co.cal',
				'../../sdi/n3147/vis/ngc3147_D1_08mar09.13co.cal',
				'../../sdi/n3147/vis/ngc3147_D2v2_08mar19.13co.cal',
				'../../sdi/n3147/vis/ngc3147_D5_10sep02.13co.cal',
				'../../sdi/n3147/vis/ngc3147_D6_10sep11.13co.cal',
				'../../sdi/n3147/vis/ngc3147_D7_10sep12.13co.cal',
				'../../sdi/n3147/vis/ngc3147a_E1_09jul12.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	rawfiles=mirfile_list[i]
 	prefix=track_list[i]+'.src'
 	telescope=telescopes[i]
 	importmode='mir'
 	execfile(script_home+'ximport'+script_version+'.py')
 	
# ---------- IMAGE DATA

track_list=['C1','C2',
			'D1','D2',
			'D5','D6','D7','E1']

# TRACK INFO
prefix_combine=track_list
prefix='n3147co13'

# CLEANING, IMAGING, & ANALYSIS
clean_mode = 'velocity'
clean_start='2520km/s'
clean_nchan=(3070-2520)/10+1
clean_width='10km/s'
rest_freq='110.201353GHz'
out_frame='LSRK'

phase_center='J2000 10h16m53.60 +73d24m03.00'
im_size=350
cell_size='1arcsec'

multi_scale=[0,4,12]
clean_gain=0.3
cycle_factor=5.0
neg_component=0

# RUN SCRIPTS
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')

