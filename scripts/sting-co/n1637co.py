# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','D1','D2','D3','D4','D5']
mirfile_list=['../../../../raw/co10/n1637/vis/ngc1637_C1_09oct18.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_C2_09nov08.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_C3_09nov10.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_D1_09aug03.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_D2_09aug07.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_D3_09aug18.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_D4_09aug20.co.cal',
            '../../../../raw/co10/n1637/vis/ngc1637_D5_09aug25.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='590km/s'
    xp['clean_nchan']       =(840-590)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 04h41m28.20 -02d51m29.00'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n1637co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='590km/s'
xp['clean_nchan']       =(840-590)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 04h41m28.20 -02d51m29.00'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(2.5/1.0)) for x in [0.,2.,4.,9.]]
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
# 
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')

xu.carmapb(xp['prefix']+'.src.ms',effdish=True)

xp['ctag']              ='_ro'
xp['cleanweight']       ='briggs'
xu.xclean(xp)

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
xu.xclean(xp)

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
xu.xclean(xp)
