# PIPELINE DEFAULT PARAMETER SETTING
# xp is the dict containing pipeline setup parameters

xp={
# FILES NAME
'rawfiles':None,        # name(s) of the data files to be imported
'msfile':'',
'prepfile':'',
'srcfile':'',
'srcfile_comb':'',

# IMPORT DATA
'prefix':'test',
'importspw':'',
'importmirspw':'',
'importscan':'',  
'importcorr':'',
'importtimerange':'',
'importmode':'vla',   # import data mode
'importwidth':'1',
'importfield':'',
'importband':'',
'importmirarray':'CARMA',
'importmirnocal':False,
'importtimebin':'0s',

'starttime':'',       # import starttime
'stoptime':'',        # import stoptime

# OBS INFO
'source':'',
'fluxcal':'',
'passcal':'',
'phasecal':'',
'spw_source':'',
'spw_fluxcal':'',
'spw_passcal':'',
'spw_phasecal':'',
'uvrange_source':'',
'uvrange_fluxcal':'',
'uvrange_passcal':'',
'uvrange_phasecal':'',

# FLAGGING
'flagselect':[],
'flagspw':'',
'flagreset':True,
'flagtest':False,
'flagselect_default':["mode='shadow'"],

# BASELINE
'bcant':'',
'bctype':'antposvla',
'bcpara':[],

# CAL
'interpmode':['linear','nearest'],
'ref_ant':'15',
'evlacal':False,
'calwt':True,
'gaincurve':False,

#    gaincurvel will be turned on if:
#        * data were from VLA
#        * taken before 2001
# CONSOLIDATE
'prefix_comb':[],
'wtscale':[],
'usevconcat':False,
'spwrgd':'',    #    by default, we will regrid TOPO to outframe
                #    set spwgrd to True/False could overwrite the default

# CONTINUE SUBTRACTION
'fitspw':'',
'fitchans':'',
'fitorder':0,
'uvcs':False,
'imcs':False,
'freqtol':'',
'uvcs_combine':'spw',
'wtstat':False,
'wtstat_fitspw':'',
'hs':False,

# CLEANing
'restorbeam':[''],
'resmooth':'common',
'restorbeam_default':[''],
'restorbeam_method':'maximum',

'threshold_spec':'0.0mJy',
'threshold_cont':'0.0mJy',

'minpb':0.1,
'cleanspw':'',
'iterchan':False,
'phasecenter':'',
'spinterpmode':'linear',
'restfreq':'1420405752.0Hz',
'outframe':'BARY',
'allowchunk':False,

'imsize':512,
'cell':'4.0arcsec',

'clean_mask':0.2,
'niter':10000,
'sigcutoff_spec':2.0,
'sigcutoff_cont':2.0,

'imstat_box_spec':'',
'imstat_rg_spec':'',
'imstat_chan':'',
'imstat_box_cont':'',
'imstat_rg_cont':'',

'ftmachine':'ft',
'imagermode':None,

'multiscale':[],
'cyclefactor':1.5,
'clean_gain':0.1,
'clean_field':'',

'cleanweight':'briggs',
'cleanspw':'',
'iterchan':False,
'outertaper':[],
'cleanspec':True,
'wrobust':0.5,
'gridmode':'aprojection',
'cleanmode':'',
'mweight':False,
'psfmode':'clark',
'fitpsf':False,
'negcomponent':-1,
'cleancont':False,
'usescratch':False,

'clean_start':'',
'clean_width':1,
'clean_nchan':-1,

# PLOTTING
'plotformat':'pdf',

# INFOMATIVE
'email':'',     # NOTIFICATION EMAIL ADDRESS
'password':'',  # NOTIFICATION EMAIL PASSWORD
'version':'',   # SCRIPT VERSION
'log_listobs_msfile':'',
'keepcasaimage':True
}
