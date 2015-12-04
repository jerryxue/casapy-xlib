# ---------- IMPORT DATA

track_list=['C1','C2','D1','D2','D3','D4','D5','E1']
mirfile_list=[	'../../../../raw/co10/n6951/vis/ngc6951_C1_08apr15.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_C2_08apr17.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_D1_08jul02.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_D2_08jul07.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_D3_08jul12.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_D4_08jul14.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_D5_08jul15.13co.cal',
				'../../../../raw/co10/n6951/vis/ngc6951_E1_09jul20.13co.cal']
telescopes=list('CARMA' for i in track_list)


track_list=['n6951co13']
mirfile_list=['../../../../raw/co10/n6951/vis/ngc6951_E1_09jul20.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='1230km/s'
	xp['clean_nchan']	   =(1620-1230)/10
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

  	#xp=xu.ximport(xp)
 	#xp=xu.xconsol(xp)

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='n6951co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='1230km/s'
xp['clean_nchan']	   =(1620-1230)/10
xp['clean_width']	   ='10km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 20h37m14.1 +66d06m20.0'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(7.0/1.0)) for x in [0.,2.,4.0]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

#xu.xconsol(xp)
# 
# xp['ctag']              ='_robust'
# xp['cleanweight']       ='briggs'
# xu.xclean(xp)
# 
# xp['ctag']              ='_natural'
# xp['cleanweight']       ='natural'
# xu.xclean(xp)

#xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
#xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
#xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
#xu.xclean(xp)
os.system('cp -rf '+xp['prefix']+'_na.line.sens.log '+xp['prefix']+'_st.line.sens.log')
