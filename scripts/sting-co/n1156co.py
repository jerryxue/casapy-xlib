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

    execfile(xlib+'xinit.py')
    
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

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

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
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        ='circle[[160pix,160pix],60pix]'

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')
