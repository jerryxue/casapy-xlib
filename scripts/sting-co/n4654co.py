# ---------- B+C+D ARRAY COMBINATION 

track_list=['C1','D1','D2','D3','D4']
mirfile_list=[  '../../../../raw/co10/n4654/vis/ngc4654_C1_10MAR20.co.cal',
                '../../../../raw/co10/n4654/vis/ngc4654_D1_10APR23.co.cal',
                '../../../../raw/co10/n4654/vis/ngc4654_D2_10MAY09.co.cal',
                '../../../../raw/co10/n4654/vis/ngc4654_D3_10MAY10.co.cal',
                '../../../../raw/co10/n4654/vis/ngc4654_D4_10MAY12.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='850km/s'
    xp['clean_nchan']       =(1240-850)/5+1
    xp['clean_width']       ='5km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 12h43m56.6 +13d07m36.0'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')


execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n4654co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='850km/s'
xp['clean_nchan']       =(1240-850)/5+1
xp['clean_width']       ='5km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 12h43m56.6 +13d07m36.0'
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