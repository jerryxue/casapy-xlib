track_list=['D1','D2','C1','C2','C3','C4','E2','E3','E4']
mirfile_list=[  '../../../../raw/co10/n4254/vis/ngc4254_D1_08jun08.co.cal',
                '../../../../raw/co10/n4254/vis/ngc4254_D2_08jun09.co.cal',
                '../../../../raw/co10/n4254/vis/n4254_C1_08OCT20.co.cal',
                '../../../../raw/co10/n4254/vis/n4254_C2_08OCT24.co.cal',
                '../../../../raw/co10/n4254/vis/n4254_C3_08OCT25.co.cal',
                '../../../../raw/co10/n4254/vis/n4254_C4_08OCT28.co.cal',
                '../../../../raw/co10/n4254/vis/ngc4254_E2_09jul02.co.cal',
                '../../../../raw/co10/n4254/vis/ngc4254_E3_09jul05.co.cal',
                '../../../../raw/co10/n4254/vis/ngc4254_E4_09jul19.co.cal']
telescopes=['CARMA']*len(track_list)

for i in range(0,len(mirfile_list)):
        
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']=telescopes[i]
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2265km/s'
    xp['clean_nchan']       =(2525-2265)/5+1
    xp['clean_width']       ='5km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'
    xp['niter']             =0
    xp['chanbin']           =3

    xp['phasecenter']       ='J2000 12h18m49.56 +14d24m58.50'
    xp['imsize']            =350
    xp['cell']              ='1arcsec'
    
    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n4254co'
xp['prefix_comb']       =track_list     

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2265km/s'
xp['clean_nchan']       =(2525-2265)/5+1
xp['clean_width']       ='5km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'

xp['phasecenter']       ='J2000 12h18m49.56 +14d24m58.50'
xp['mosweight']         =True
xp['imsize']            =450
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
