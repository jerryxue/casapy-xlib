# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D2','D3','D4','D5','D6']
mirfile_list=['../../../../raw/co10/n3198/vis/ngc3198_C1_09apr13.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_C2_10MAR02.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_D2_09aug24.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_D3_09aug29.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_D4_09aug31.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_D5_10APR16.13co.cal',
			'../../../../raw/co10/n3198/vis/ngc3198_D6_10APR21.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='460km/s'
	xp['clean_nchan']	   =(860-460)/10+1
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

# 	xp=xu.ximport(xp)
# 	xp=xu.xconsol(xp)	

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='n3198co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='460km/s'
xp['clean_nchan']	   =(860-460)/10+1
xp['clean_width']	   ='10km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 10h19m54.92 +45d32m59.00'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =350
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(2.5/1.0)) for x in [0.,2.,4.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# xu.xconsol(xp)
# 
# xp['ctag']              ='_robust'
# xp['cleanweight']       ='briggs'
# xu.xclean(xp)
# 
# xp['ctag']              ='_natural'
# xp['cleanweight']       ='natural'
# xu.xclean(xp)

xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xu.xclean(xp)

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
xu.xclean(xp)

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
xu.xclean(xp)
