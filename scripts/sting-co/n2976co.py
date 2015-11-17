track_list=['bima'+str(i+1) for i in range(24)]+['C'+str(i+1) for i in range(8)]
telescopes=['bima']*24+['CARMA']*8
# 5th & 6th tracks have strange flagging
#track_list=['bima'+str(i+1) for i in range(22)]+['C'+str(i+1) for i in range(8)]
#telescopes=['bima']*22+['CARMA']*8
mirfile_list= [ '../../../../raw/co10/bima/n2976/n2976/old/n2976.1.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976/old/n2976.2.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976_C/01apr01/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976_C/01apr30/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976_C/01may02/n2976.lc.usb',#
                '../../../../raw/co10/bima/n2976/n2976_C/01may08/n2976.lc.usb',#
                '../../../../raw/co10/bima/n2976/n2976_C/01may27/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976_C/01jun02/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976_C/01jun04/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/n2976/01jun21/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976/01jun23/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976_B/02feb26/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976_B/02mar02/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976_B/02mar03/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976_B/02mar04/n2976.usb',
                '../../../../raw/co10/bima/n2976/n2976_B/02mar08/n2976.usb',
                '../../../../raw/co10/bima/n2976/c115.2976n/03may20.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/c115.2976n/03may12.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/c115.2976n/03may14.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/d115.2976n/03jun30.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/c115.2976s/03may11.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/c115.2976s/03may17.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/c115.2976s/03may19.raw/n2976.lc.usb',
                '../../../../raw/co10/bima/n2976/d115.2976s/03jul01.raw/n2976.lc.usb',
                '../../../../raw/co10/n2976/vis/ngc2976_C1_10SEP30.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C2_10OCT02.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C3_10OCT12.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C4_10OCT13.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C5_10OCT13.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C6_10OCT14.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C7_10OCT29.co.cal',
                '../../../../raw/co10/n2976/vis/ngc2976_C8_10NOV01.co.cal']

for i in range(0,len(mirfile_list)):

    xp=xu.init()
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-100km/s'
    xp['clean_nchan']       =(200)/5+1
    xp['clean_width']       ='5km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'
    xp['fitspw']            ='*:0~2;38~40'

    xp['phasecenter']       ='J2000 09h47m15.40 67d54m59.00'

    xp=xu.ximport(xp)
    xp=xu.xconsol(xp)

xp=xu.init()

# CONSOLIDATING 
xp['prefix']            ='n2976co'
xp['prefix_comb']       =track_list     
xp['scalewt']           =True

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='-100km/s'
xp['clean_nchan']       =(200)/5+1
xp['clean_width']       ='5km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 09h47m15.40 67d54m59.00'
xp['mosweight']         =True
xp['imsize']            =450
xp['cell']              ='1arcsec'

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
# 
# # RUN SCRIPTS
# execfile(xlib+'xconsol.py')
# execfile(xlib+'xclean.py')
# xu.sumwt(xp['prefix']+'.src.ms')