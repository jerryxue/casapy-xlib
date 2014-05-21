# ----------  Load Data ---------- 

track_list=['D1','D2','D3','C1','C2','C3','C4','C5','C6']
mirfile_list=[
                '../../../../raw/co10/n6503/vis/N6503_D1_08mar26.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_D2_08mar29.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_D3_08mar30.co.cal',           
                '../../../../raw/co10/n6503/vis/N6503_C1_09oct25.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_C2_09oct31.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_C3_09nov02.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_C4_09nov03.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_C5_09nov05.co.cal',
                '../../../../raw/co10/n6503/vis/N6503_C6_09nov07.co.cal',
                ]
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='-100km/s'
    xp['clean_nchan']       =(170+100)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    xp['phasecenter']       ='J2000 17h49m26.5 +70d08m39.6'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n6503co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='-100km/s'
xp['clean_nchan']       =(170+100)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'
    
xp['phasecenter']       ='J2000 17h49m26.5 +70d08m39.6'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        =0.25
xp['outertaper']        =['2arcsec']

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')
