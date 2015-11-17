# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','C4']
mirfile_list=['../../../../raw/co10/n2782/vis/ngc2782_C1_08may19.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C2_08may31.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C3_08jun01.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C4_08jun03.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2410km/s'
    xp['clean_nchan']       =(2670-2410)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 09h14m05.10 40d06m49.00'

    xp=xu.ximport(xp)
    xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n2782co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2410km/s'
xp['clean_nchan']       =(2670-2410)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 09h14m05.10 40d06m49.00'
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


# RUN SCRIPTS

xu.xconsol(xp)

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