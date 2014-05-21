# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','C4']
mirfile_list=['../../../../raw/co10/n2782/vis/ngc2782_C1_08may19.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C2_08may31.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C3_08jun01.co.cal',
            '../../../../raw/co10/n2782/vis/ngc2782_C4_08jun03.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2410km/s'
    xp['clean_nchan']       =(2670-2410)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 09h14m05.10 40d06m49.00'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n2782co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2410km/s'
xp['clean_nchan']       =(2670-2410)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 09h14m05.10 40d06m49.00'
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