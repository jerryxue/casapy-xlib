# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','C2','C3','D1','D2','D3']
mirfile_list=['../../../../raw/co10/n3593/vis/ngc3593_C1_09oct11.co.cal',
            '../../../../raw/co10/n3593/vis/ngc3593_C2_09oct15.co.cal',
            '../../../../raw/co10/n3593/vis/ngc3593_C3_09oct16.co.cal',
            '../../../../raw/co10/n3593/vis/ngc3593_D1_10APR10.co.cal',
            '../../../../raw/co10/n3593/vis/ngc3593_D2_10APR17.co.cal',
            '../../../../raw/co10/n3593/vis/ngc3593_D3_10APR22.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='450km/s'
    xp['clean_nchan']       =(820-450)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 11h14m37.00 +12d49m03.60'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n3593co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='450km/s'
xp['clean_nchan']       =(820-450)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 11h14m37.00 +12d49m03.60'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        =0.10
"""
xp['prefix']            ='n3593co_scl'
xp['clean_start']       ='500km/s'
xp['clean_nchan']       =(770-500)/10+1
xp['clean_width']       ='10km/s'
"""
# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')