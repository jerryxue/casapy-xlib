track_list=['D1','D2','D3','D4']
mirfile_list=[  '../../../../raw/co10/n1569/vis/ngc1569_D1_09aug14.co.cal',
                '../../../../raw/co10/n1569/vis/ngc1569_D2_09aug15.co.cal',
                '../../../../raw/co10/n1569/vis/ngc1569_D3_09aug19.co.cal',
                '../../../../raw/co10/n1569/vis/ngc1569_D4_09aug24.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-230km/s'
    xp['clean_nchan']       =(30+230)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'
    xp['niter']             =0
    xp['chanbin']           =0

    xp['phasecenter']       ='J2000 04h30m49.06 64d50m52.61'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n1569co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='-230km/s'
xp['clean_nchan']       =(30+230)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 04h30m49.06 64d50m52.61'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        ='circle[[160pix,160pix],60pix]'

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')
