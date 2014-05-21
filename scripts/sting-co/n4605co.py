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
    
    execfile(xlib+'xinit.py')
    
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

    xp['phasecenter']       ='J2000 12h40m00.0 +61d36m31.01'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n4605co'
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
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        ='circle[[160pix,160pix],100pix]'


# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')

