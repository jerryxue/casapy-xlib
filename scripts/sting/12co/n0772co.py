track_list=['D1','D2','D3','D4','C1','C2','C3','C4','C5','C6','C7','E1']
mirfile_list=[  '../../../../raw/co10/n0772/vis/ngc772_D1_09feb22.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772_D2_09feb23.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772_D3_09feb27.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772b_D4v2_09mar01.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C1_09apr13.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C2_09apr21.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C3_09apr25.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C4_09apr27.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C5_09may03.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C6_09may05.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C7_09may07.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_E1_09jul21.co.cal' ]
telescopes=['CARMA']*len(track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']='CARMA'
    
    xp['spwrgd']             ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2150km/s'
    xp['clean_nchan']       =(2720-2150)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'
    
    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 

xp['prefix_comb']       =track_list
xp['prefix']            ='../n0772/n0772co'

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2150km/s'
xp['clean_nchan']       =(2720-2150)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'

xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =320
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.05
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,1.,3.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0


# RUN SCRIPTS
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
# xu.mossen(vis=xp['prefix']+'.src.ms',
#           log=xp['prefix']+xp['ctag']+'.line.sens.log',
#           nchan=xp['clean_nchan'],ftmachine='mosaic',
#           mosweight=True,imsize=xp['imsize'],
#           weight=xp['cleanweight'])