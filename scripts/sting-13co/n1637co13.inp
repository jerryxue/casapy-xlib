# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','D1','D2','D3','D4','D5']
mirfile_list=['../../sdi/n1637/vis/ngc1637_C1_09oct18.13co.cal',
			'../../sdi/n1637/vis/ngc1637_C2_09nov08.13co.cal',
			'../../sdi/n1637/vis/ngc1637_C3_09nov10.13co.cal',
			'../../sdi/n1637/vis/ngc1637_D1_09aug03.13co.cal',
			'../../sdi/n1637/vis/ngc1637_D2_09aug07.13co.cal',
			'../../sdi/n1637/vis/ngc1637_D3_09aug18.13co.cal',
			'../../sdi/n1637/vis/ngc1637_D4_09aug20.13co.cal',
			'../../sdi/n1637/vis/ngc1637_D5_09aug25.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	rawfiles=mirfile_list[i]
 	prefix=track_list[i]+'.src'
 	telescope=telescopes[i]
 	importmode='mir'
 	execfile(script_home+'ximport'+script_version+'.py')
 	

# TRACK INFO
prefix_combine=track_list
prefix='n1637co13'

# CLEANING, IMAGING, & ANALYSIS
clean_mode = 'velocity'
clean_start='590km/s'
clean_nchan=(840-590)/10+1
clean_width='10km/s'
rest_freq='110.201353GHz'
out_frame='LSRK'

phase_center='J2000 04h41m28.20 -02d51m29.00'
im_size=350
cell_size='1arcsec'

multi_scale=[0,3,9]
clean_gain=0.3
cycle_factor=5.0
neg_component=0

# RUN SCRIPTS
execfile(script_home+'xmerge'+script_version+'.py')
execfile(script_home+'xclean'+script_version+'.py')