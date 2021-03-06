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

mirfile_list=	[	'../../../../raw/co10/n2976/vis/ngc2976_C1_10SEP30.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C2_10OCT02.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C3_10OCT12.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C4_10OCT13.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C5_10OCT13.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C6_10OCT14.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C7_10OCT29.13co.cal',
					'../../../../raw/co10/n2976/vis/ngc2976_C8_10NOV01.13co.cal']


for i in range(0,len(mirfile_list)):
	
	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='-100km/s'
	xp['clean_nchan']	   =(200)/5+1
	xp['clean_width']	   ='5km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

	#xp=xu.ximport(xp)
	#xp=xu.xconsol(xp)

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='../n2976/n2976co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='-100km/s'
xp['clean_nchan']	   =(200)/5+1
xp['clean_width']	   ='5km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 09h47m15.40 67d54m59.00'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =750
xp['cell']              ='0.5arcsec'

xp['minpb']             =0.05
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(2.0/0.5)) for x in [0.,2.,4.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

#xu.xconsol(xp)
#xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xu.xclean(xp)
# xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
#xu.xclean(xp)
# xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
#xu.xclean(xp)
#os.system('cp -rf '+xp['prefix']+'_na.line.sens.log '+xp['prefix']+'_st.line.sens.log')
