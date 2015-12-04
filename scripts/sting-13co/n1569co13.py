# ---------- B+C+D ARRAY COMBINATION 

track_list=['D1','D2','D3','D4']
mirfile_list=[	'../../../../raw/co10/n1569/vis/ngc1569_D1_09aug14.13co.cal',
				'../../../../raw/co10//n1569/vis/ngc1569_D2_09aug15.13co.cal',
				'../../../../raw/co10/n1569/vis/ngc1569_D3_09aug19.13co.cal',
				'../../../../raw/co10/n1569/vis/ngc1569_D4_09aug24.13co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-230km/s'
    xp['clean_nchan']       =(20+230)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='110.201353GHz'
    xp['outframe']          ='LSRK'

#     xp=xu.ximport(xp)
#     xp=xu.xconsol(xp)

xp=xu.init()
 
# CONSOLIDATING 
xp['prefix']            ='n1569co13'
xp['prefix_comb']       =track_list     
 
xp['spwrgd']            ='spw'
xp['freqtol']           ='0.5MHz'
 
# IMAGING
xp['cleanmode']		 	='velocity'
xp['clean_start']	   	='-230km/s'
xp['clean_nchan']	   	=(20+230)/10+1
xp['clean_width']	   	='10km/s'
xp['restfreq']		  	='110.201353GHz'
xp['outframe']		  	='LSRK'

xp['phasecenter']       ='J2000 04h30m49.06 64d50m52.61'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =400
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