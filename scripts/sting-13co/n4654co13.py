# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','D1','D2','D3','D4']
mirfile_list=[	'../../../../raw/co10/n4654/vis/ngc4654_C1_10MAR20.13co.cal',
				'../../../../raw/co10/n4654/vis/ngc4654_D1_10APR23.13co.cal',
				'../../../../raw/co10/n4654/vis/ngc4654_D2_10MAY09.13co.cal',
				'../../../../raw/co10/n4654/vis/ngc4654_D3_10MAY10.13co.cal',
				'../../../../raw/co10/n4654/vis/ngc4654_D4_10MAY12.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='850km/s'
	xp['clean_nchan']	   =(1240-850)/5+1
	xp['clean_width']	   ='5km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

	xp=xu.ximport(xp)
	xp=xu.xconsol(xp)

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='n4654co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='850km/s'
xp['clean_nchan']	   =(1240-850)/5+1
xp['clean_width']	   ='5km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 12h43m56.6 +13d07m36.0'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =350
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(2.0/1.0)) for x in [0.,2.,4.,9.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

xu.xconsol(xp)

xp['ctag']              ='_robust'
xp['cleanweight']       ='briggs'
xu.xclean(xp)

xp['ctag']              ='_natural'
xp['cleanweight']       ='natural'
xu.xclean(xp)
