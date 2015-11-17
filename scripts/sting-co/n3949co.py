# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D1','D2','E1','C3','C4']
mirfile_list=[  '../../../../raw/co10/n3949/vis/ngc3949_C1_08nov06.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_C2_08nov08.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_D1_08aug16.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_D2_08aug19.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_E1_08oct03.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_C3_09oct12.co.cal',
                '../../../../raw/co10/n3949/vis/ngc3949_C4_09oct17.co.cal' ]
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='600km/s'
    xp['clean_nchan']       =(1000-600)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 11h53m41.4 +47d51m32.0'

    xp=xu.ximport(xp)
    xp=xu.xconsol(xp)

# CONSOLIDATING 
xp['prefix']            ='n3949co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='600km/s'
xp['clean_nchan']       =(1000-600)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 11h53m41.4 +47d51m32.0'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(2.0/1.0)) for x in [0.,2.,4.,9.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0

xu.xconsol(xp)

xp['ctag']              ='_robust'
xp['cleanweight']       ='briggs'
xu.xclean(xp)

xp['ctag']              ='_natural'
xp['cleanweight']       ='natural'
xu.xclean(xp)

# RUN SCRIPTS
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')