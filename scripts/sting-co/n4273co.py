# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','C5','C6','D1','D2','D3']
mirfile_list=['../../../../raw/co10/n4273/vis/ngc4273_C1_10MAR10.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_C2_10MAR11.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_C3_10MAR13.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_C5_10MAR18.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_C6_10MAR19.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_D1_10MAY17.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_D2_10MAY27.co.cal',
            '../../../../raw/co10/n4273/vis/ngc4273_D3_10MAY28.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2180km/s'
    xp['clean_nchan']       =(2580-2180)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 12h19m56.06 +05d20m35.90'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n4273co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2180km/s'
xp['clean_nchan']       =(2580-2180)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 12h19m56.06 +05d20m35.90'
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

# xu.xconsol(xp)
# 
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

xp['ctag']              ='_na'
xp['cleanweight']       ='natural'
xu.xclean(xp)

xp['ctag']              ='_st'
xp['cleanweight']       ='natural'
xp['multiscale']        =[]
xu.xclean(xp)

# 
# # RUN SCRIPTS
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')