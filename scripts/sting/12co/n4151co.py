# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D1','D2']
mirfile_list=['../../../../raw/co10/n4151/vis/ngc4151_C1_08apr26.co.cal',
            '../../../../raw/co10/n4151/vis/ngc4151_C2_08apr28.co.cal',
            '../../../../raw/co10/n4151/vis/ngc4151_D1_08mar01.co.cal',
            '../../../../raw/co10/n4151/vis/ngc4151_D2_08mar02.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='870km/s'
    xp['clean_nchan']       =(1130-870)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

#     xp=xu.ximport(xp)
#     xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='../n4151/n4151co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='870km/s'
xp['clean_nchan']       =(1130-870)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 12h10m32.60 +39d24m21.00'
xp['mosweight']         =True
xp['wnpixels']          =0
xp['imsize']            =320
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.05
xp['clean_mask']        =1./3.
xp['multiscale']        =[int(x*(2.5/1.0)) for x in [0.,1.,5.]]
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

# RUN SCRIPTS
#xp=xu.xconsol(xp)
#xp=xu.xclean(xp)
