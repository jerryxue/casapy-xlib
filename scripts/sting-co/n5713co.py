# ---------- B+C+D ARRAY COMBINATION

track_list=['C1','C3','E1','E2','D1','D2','D3']
mirfile_list=[  '../../../../raw/co10/n5713/vis/ngc5713_C1_09may14.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_C3_09jun03.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_E1_09jun13.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_E2_09jun23.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_D1_10APR20.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_D2_10MAY19.co.cal',
                '../../../../raw/co10/n5713/vis/ngc5713_D3_10MAY20.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1760km/s'
    xp['clean_nchan']       =(2040-1760)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 14h40m11.5 -00d17m20.3'

    xp=xu.ximport(xp)
    xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n5713co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='1760km/s'
xp['clean_nchan']       =(2040-1760)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 14h40m11.5 -00d17m20.3'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        =0.15
xp['multiscale']        =[int(x*(4.0/1.0)) for x in [0.,2.,4.,9.]]
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
# 
# # RUN SCRIPTS
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')
