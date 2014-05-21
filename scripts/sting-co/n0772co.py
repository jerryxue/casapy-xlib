track_list=['D1','D2','D3','D4','C1','C2','C3','C4','C5','C6','C7','E1']
mirfile_list=[  '../../../../raw/co10/n0772/vis/ngc772_D1_09feb22.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772_D2_09feb23.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772_D3_09feb27.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772b_D4v2_09mar01.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C1_09apr13.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C2_09apr21.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C3_09apr25.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C4_09apr27.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C5_09may03.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C6_09may05.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_C7_09may07.co.cal',
                '../../../../raw/co10/n0772/vis/ngc772c_E1_09jul21.co.cal' ]
telescopes=['CARMA']*len(track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']='CARMA'
    
    xp['spwrgd']             ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2150km/s'
    xp['clean_nchan']       =(2720-2150)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'
    
    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 

xp['prefix_comb']       =track_list
xp['prefix']            ='n0772co'

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2150km/s'
xp['clean_nchan']       =(2720-2150)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'

xp['phasecenter']       ='J2000 01h59m19.58 +19d00m27.10'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,3,9]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        =0.25
xp['niter']             =0
xp['resmooth']          =False

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')