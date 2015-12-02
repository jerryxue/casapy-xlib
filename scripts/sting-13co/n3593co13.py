# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','D1','D2','D3']
mirfile_list=['../../../../raw/co10/n3593/vis/ngc3593_C1_09oct11.13co.cal',
			'../../../../raw/co10/n3593/vis/ngc3593_C2_09oct15.13co.cal',
			'../../../../raw/co10/n3593/vis/ngc3593_C3_09oct16.13co.cal',
			'../../../../raw/co10/n3593/vis/ngc3593_D1_10APR10.13co.cal',
			'../../../../raw/co10/n3593/vis/ngc3593_D2_10APR17.13co.cal',
			'../../../../raw/co10/n3593/vis/ngc3593_D3_10APR22.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='450km/s'
	xp['clean_nchan']	   =(820-450)/10+1
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

# 	xp=xu.ximport(xp)
# 	xp=xu.xconsol(xp)

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='n3593co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='450km/s'
xp['clean_nchan']	   =(820-450)/10+1
xp['clean_width']	   ='10km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 11h14m37.00 +12d49m03.60'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =350
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,2.,4.]]
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