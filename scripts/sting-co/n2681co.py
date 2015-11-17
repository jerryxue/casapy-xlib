track_list=['n2681co']
mirfile_list=[  '../../../../raw/co10/n2681/vis/ngc2681_C1_08may13.co.cal'  ]
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='560km/s'
    xp['clean_nchan']       =(820-560)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 8h53m32.7 +51d18m48.99'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n2681co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='560km/s'
xp['clean_nchan']       =(820-560)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 8h53m32.7 +51d18m48.99'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =640
xp['cell']              ='0.5arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(1.5/0.5)) for x in [0.,2.,4.,9.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0


# RUN SCRIPTS

#xu.xconsol(xp)

xp['ctag']              ='_robust'
xp['cleanweight']       ='briggs'
xu.xclean(xp)

xp['ctag']              ='_natural'
xp['cleanweight']       ='natural'
xu.xclean(xp)

# 
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')
