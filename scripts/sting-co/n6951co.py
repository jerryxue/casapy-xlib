# ---------- IMPORT DATA

track_list=['C1','C2','D1','D2','D3','D4','D5','E1']
mirfile_list=[  '../../../../raw/co10/n6951/vis/ngc6951_C1_08apr15.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_C2_08apr17.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_D1_08jul02.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_D2_08jul07.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_D3_08jul12.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_D4_08jul14.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_D5_08jul15.co.cal',
                '../../../../raw/co10/n6951/vis/ngc6951_E1_09jul20.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1230km/s'
    xp['clean_nchan']       =(1620-1230)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 20h37m14.1 +66d06m20.0'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n6951co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='1230km/s'
xp['clean_nchan']       =(1620-1230)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 20h37m14.1 +66d06m20.0'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =600
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.25
#xp['clean_mask']        ='circle[[300pix,300pix],120pix]'
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,2.,4.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

# xu.xconsol(xp)

# xu.carmapb(xp['prefix']+'.src.ms',effdish=False)
# 
# xp['ctag']              ='_robust'
# xp['cleanweight']       ='briggs'
# xu.xclean(xp)
#  
# xp['ctag']              ='_natural'
# xp['cleanweight']       ='natural'
# xu.xclean(xp)
# 
# xp['ctag']              ='_regular'
# xp['cleanweight']       ='natural'
# xp['multiscale']        =[]
# xu.xclean(xp)

#xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

# because loose mosaic patterns, we can't push to larger scales.
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,2.,4.]]

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xp['threshold_spec']    ='70mJy'
#xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
xp['threshold_spec']    ='70mJy'
#xu.xclean(xp)
xu.mossen(vis=xp['prefix']+'.src.ms',
          log=xp['prefix']+xp['ctag']+'.line.sens.log',
          nchan=xp['clean_nchan'],ftmachine='mosaic',
          mosweight=True,imsize=xp['imsize'],
          weight=xp['cleanweight'])

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['threshold_spec']    ='70mJy'
xp['multiscale']        =[]
#xu.xclean(xp)
os.system('cp -rf '+xp['prefix']+'_na.line.sens.log '+xp['prefix']+'_st.line.sens.log')

# RUN SCRIPTS
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')