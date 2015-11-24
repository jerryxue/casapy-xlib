track_list=['C1','D1','D2','D3','D4','D5','D6']
mirfile_list=[  '../../../../raw/co10/n1156/vis/ngc1156_C1_08apr23.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D1_08mar18.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D2_08mar28.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D3_08jun22.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D4_08jul10.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D5_08jul12.co.cal',
                '../../../../raw/co10/n1156/vis/ngc1156_D6_08jul13.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='245km/s'
    xp['clean_nchan']       =(505-245)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 2h59m42.2 25d14m14.00'

    #xp=xu.ximport(xp)
    #xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n1156co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='245km/s'
xp['clean_nchan']       =(505-245)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 2h59m42.2 25d14m14.00'
xp['mosweight']         =True
xp['wnpixels']          =128
xp['imsize']            =400
xp['cell']              ='1.0arcsec'

xp['minpb']             =0.10
xp['clean_mask']        ='circle[[200pix,200pix],75pix]'
xp['multiscale']        =[int(x*(2.5/1.0)) for x in [0.,2.,4.,9.]]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0



# RUN SCRIPTS

#xu.xconsol(xp)

# xp['ctag']              ='_robust'
# xp['cleanweight']       ='briggs'
# xu.xclean(xp)
# 
# xp['ctag']              ='_natural'
# xp['cleanweight']       ='natural'
# xu.xclean(xp)
#xu.sumwt(xp['prefix']+'.src.ms')


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
