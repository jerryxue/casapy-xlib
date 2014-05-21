track_list=['C1','C2','D1','D2','D5','D6','D7','E1']
mirfile_list=[  '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_C1_08apr05.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_C2_08apr07.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_D1_08mar09.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_D2v2_08mar19.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_D5_10sep02.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_D6_10sep11.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147_D7_10sep12.co.cal',
                '/Volumes/Scratch/reduc/sting-co/n3147/vis/ngc3147a_E1_09jul12.co.cal']
telescopes=list('CARMA' for i in track_list)

for i in range(0,len(mirfile_list)):
    execfile(xlib+'xinit.py')
    
    xp['rawfiles']=mirfile_list[i]
    xp['prefix']=track_list[i]
    xp['importmode']='mir'
    xp['importmirarray']='CARMA'
    
    xp['spwrgd']            ='spw'
    xp['cleanmode']         ='velocity'
    xp['clean_start']       ='2520km/s'
    xp['clean_nchan']       =(3070-2520)/10+1
    xp['clean_width']       ='10km/s'
    xp['restfreq']          ='115.2712GHz'
    xp['outframe']          ='LSRK'

    execfile(xlib+'ximport.py')
    execfile(xlib+'xconsol.py')

execfile(xlib+'xinit.py')

# CONSOLIDATING 
xp['prefix']            ='n3147co'
xp['prefix_comb']       =track_list

xp['spwrgd']             ='spw'
xp['freqtol']           ='0.5MHz'

# IMAGING
xp['cleanmode']         ='velocity'
xp['clean_start']       ='2520km/s'
xp['clean_nchan']       =(3070-2520)/10+1
xp['clean_width']       ='10km/s'
xp['restfreq']          ='115.2712GHz'
xp['outframe']          ='LSRK'

xp['phasecenter']       ='J2000 10h16m53.60 +73d24m03.00'
xp['mosweight']         =True
xp['imsize']            =2**5*10
xp['cell']              ='1arcsec'

xp['multiscale']        =[0,4,12]
xp['clean_gain']        =0.3
xp['cyclefactor']       =5.0
xp['negcomponent']      =0
xp['minpb']             =0.10
xp['clean_mask']        =0.25

# RUN SCRIPTS
execfile(xlib+'xconsol.py')
execfile(xlib+'xclean.py')
xu.sumwt(xp['prefix']+'.src.ms')