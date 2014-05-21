# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','C4','C5','D1','D2','D3','D4','D5','D6']
mirfile_list=[  '../../../../raw/co10/n5371/vis/ngc5371_C1_09may11.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_C2_09may12.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_C3_09may13.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_C4_09may14.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_C5_09may18.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D1_10APR16.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D2_10APR17.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D3_10APR18.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D4_10APR21.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D5_10MAY06.co.cal',
                '../../../../raw/co10/n5371/vis/ngc5371_D6_10MAY11.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2360km/s'
    xp['clean_nchan']       =(2750-2360)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 13h55m39.9 +40d27m41.99'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n5371co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2360km/s'
xp['clean_nchan']       =(2750-2360)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 13h55m39.9 +40d27m41.99'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        =0.10

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')
