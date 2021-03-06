# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D1','D2','D3','E1']
mirfile_list=['../../../../raw/co10/n4536/vis/ngc4536_C1_09apr24.13co.cal',
			'../../../../raw/co10/n4536/vis/ngc4536_C2_09apr26.13co.cal',
			'../../../../raw/co10/n4536/vis/ngc4536_D1_08jul25.13co.cal',
			'../../../../raw/co10/n4536/vis/ngc4536_D2_08jul29.13co.cal',
			'../../../../raw/co10/n4536/vis/ngc4536_D3_08aug02.13co.cal',
			'../../../../raw/co10/n4536/vis/ngc4536_E1_09jul19.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='1610km/s'
	xp['clean_nchan']	   =(2010-1610)/10+1
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

# 	xp=xu.ximport(xp)
# 	xp=xu.xconsol(xp)

xp=xu.init()

#   vrange tracks 
track_list=['C1','C2','E1']
 
# CONSOLIDATING 
xp['prefix']            ='../n4536/n4536co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']	   ='1610km/s'
xp['clean_nchan']	   =(2010-1610)/10+1
xp['clean_width']	   ='10km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 12h34m27.1 +02d11m16.00'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =300
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.05
xp['clean_mask']        =0.25
xp['multiscale']        =[int(x*(2.0/1.0)) for x in [0.,1.,4.]]
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
