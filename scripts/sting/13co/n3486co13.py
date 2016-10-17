# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','C4','C5','D1','D2','D3']
mirfile_list=['../../../../raw/co10/n3486/vis/ngc3486_C1_08may07.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_C2_08may15.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_C3_08may21.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_C4_08may23.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_C5_08may25.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_D1_10APR26.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_D2_10MAY14.13co.cal',
			'../../../../raw/co10/n3486/vis/ngc3486_D3_10MAY15.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	
	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='550km/s'
	xp['clean_nchan']	   =(810-550)/10+1
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

# 	xp=xu.ximport(xp)
# 	xp=xu.xconsol(xp)

#   vrange tracks 
track_list=['D1','D2','D3']

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='../n3486/n3486co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 ='velocity'
xp['clean_start']	   ='550km/s'
xp['clean_nchan']	   =(810-550)/10+1
xp['clean_width']	   ='10km/s'
xp['restfreq']		  ='110.201353GHz'
xp['outframe']		  ='LSRK'

xp['phasecenter']       ='J2000 11h00m23.9 +28d58m29.00'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =320
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.20
xp['clean_mask']        =0.25
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,1.,4.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

#xu.xconsol(xp)
# xu.xclean(xp)


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