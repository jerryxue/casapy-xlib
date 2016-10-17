# ---------- B+C+D ARRAY COMBINATION 

track_list=['C0','C1','C2','C3','C4','C5','C6','B1','B2','B3','B4','B5']
mirfile_list=[  '../../../../raw/co10/bima/n4605/n4605/00jun16/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/00dec09/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/01mar09/n4605.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/01mar10/n4605.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/01mar12/n4605.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/01mar15/n4605.usb',
    '../../../../raw/co10/bima/n4605/n4605_C/01mar16/n4605.usb',
    '../../../../raw/co10/bima/n4605/n4605_B/01feb07/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_B/01feb20/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_B/01feb24/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_B/01feb26/n4605.lc.usb',
    '../../../../raw/co10/bima/n4605/n4605_B/01jan27/n4605.lc.usb']
telescopes=list('BIMA' for i in track_list)  

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='55km/s'
    xp['clean_nchan']       =44
    xp['clean_width']       ='5km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='../n4605/n4605co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='55km/s'
xp['clean_nchan']       =44
xp['clean_width']       ='5km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 12h40m00.0 +61d36m31.01'
xp['mosweight']         =True
xp['wnpixels']          =96

xp['imsize']            =256
xp['cell']              ='1arcsec'

xp['minpb']             =0.05
xp['clean_mask']        ='circle[[128pix,128pix],100pix]'
xp['clean_mask']        =0.1
xp['multiscale']        =[int(x*(2.5/1.0)) for x in [0.,1.,4.]]
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

#xu.sumwt(xp['prefix']+'.src.ms')

