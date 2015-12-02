# ---------- IMPORT DATA

mirfile_list=filesearch("../../../../raw/co10/n0772//vis/*.13co.cal")
track_list=[w.split('_')[1] for w in mirfile_list]
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
	
	xp=xu.init()
	
	xp['rawfiles']=mirfile_list[i]
	xp['prefix']=track_list[i]
	xp['importmode']='mir'
	xp['importmirarray']=telescopes[i]
	
	xp['spwrgd']			='spw'
	xp['cleanmode']		 ='velocity'
	xp['clean_start']	   ='2150km/s'
	xp['clean_nchan']	   =(2720-2150)/10+1
	xp['clean_width']	   ='10km/s'
	xp['restfreq']		  ='110.201353GHz'
	xp['outframe']		  ='LSRK'

	#xp=xu.ximport(xp)
	#xp=xu.xconsol(xp)

# ---------- IMAGE DATA

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n0772co13'
xp['prefix_comb']       =track_list     

xp['spwrgd']            ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2150km/s'
xp['clean_nchan']       =(2720-2150)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='110.201353GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.20
xp['multiscale']        =[int(x*(1.75/1.0)) for x in [0.,2.,4.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

#xu.xconsol(xp)

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
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

