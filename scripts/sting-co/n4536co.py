# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','D1','D2','D3','E1']
mirfile_list=['../../../../raw/co10/n4536/vis/ngc4536_C1_09apr24.co.cal',
            '../../../../raw/co10/n4536/vis/ngc4536_C2_09apr26.co.cal',
            '../../../../raw/co10/n4536/vis/ngc4536_D1_08jul25.co.cal',
            '../../../../raw/co10/n4536/vis/ngc4536_D2_08jul29.co.cal',
            '../../../../raw/co10/n4536/vis/ngc4536_D3_08aug02.co.cal',
            '../../../../raw/co10/n4536/vis/ngc4536_E1_09jul19.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):

    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='1610km/s'
    xp['clean_nchan']       =(2010-1610)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 12h34m27.1 +02d11m16.00'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n4536co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='1610km/s'
xp['clean_nchan']       =(2010-1610)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 12h34m27.1 +02d11m16.00'
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
