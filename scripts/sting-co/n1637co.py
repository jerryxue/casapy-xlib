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
    
    execfile(xlib+'xinit.py')
    
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

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


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
