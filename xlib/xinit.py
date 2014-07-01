################################################################################
#    DEFAULT SETTING
#    note: this file could be tailored for a specific project
################################################################################

xp={
'rawfiles':None,            # Name(s) of the data file(s) to be imported
'msfile':'',
'prepfile':'',
'srcfile':'',
'srcfile_comb':'',

# IMPORT DATA
'prefix':'test',            # Pre-name of reduction files
'importmode':'vla',         # Data importing mode
                            # 'vla':    import data in the VLA archive format
                            # 'uvfits': import data from a uvfits file
                            # 'evla':   import data from a EVLA ASDM file
                            # 'mir':    import data in the MIRIAD format using MIRIAD
                            # 'miriad': import data in the MIRAID format using 
                            #           CARMAFILLER (experimental.. you have to compile CASACORE
                            #           and FILLER on your system.)
                            # 'ms':     copy/split data from a MS file, leave the orginal file untouched
'importspw':'',             # MS spectral windows to be imported (note: spw starts with 1 in MIRIAD, e.g. '1,2,7')
'importmirspw':'',          # MIRIAD spectral windows to ve imported 
'importscan':'',            # Select the scans to be imported
'importcorr':'',            # Select the correlations to be imported
'importtimerange':'',       # Select the timerange to be imported
'importchanbin':1,          # pre-channel averaging during data importing 
'importfield':'',           # Select the fields to be imported
'importband':'',            # Select the band to be imported
'importmirarray':'CARMA',   # Select the array name when importing MIRIAD files (CARMA, BIMA, SMA)
'importmirnocal':False,     # Dont apply the gain table in MIRIAD files when importing data
'importtimebin':'0s',       # pre-time averaging during data importing
'importmirline':'',         # regridding the MIRIAD spectral windows before importing data

'starttime':'',             # start time to search for data (only for importmode='vla')
'stoptime':'',              # end time to search for data (only for importmode='vla')

# OBS INFO
'source':'',                # target name
'fluxcal':'',               # flux calibrator name
'passcal':'',               # passband calibrator name (if passcal=='', passcal=fluxcal)
'phasecal':'',              # phase calibrator name
'spw_source':'',            # spw for source
'spw_fluxcal':'',           # spw for fluxcal
'spw_passcal':'',           # spw for passcal
'spw_phasecal':'',          # spw for phasecal
'uvrange_source':'',        # uvrange of source used for calibrations
'uvrange_fluxcal':'',       # uvrange of fluxcal used for calibrations (check the VLA CALIBRATOR MANUAL)
'uvrange_passcal':'',       # uvrange of passcal used for calibrations (check the VLA CALIBRATOR MANUAL)
'uvrange_phasecal':'',      # uvrange of phasecal used for calibrations (check the VLA CALIBRATOR MANUAL)
'bpcopy':True,              # perform bandpass transfer
                            # default: bpcopy will be performed if spw from passband doesn't match that from phasecal/source/fluxcal
#
# Note for bandpass mapping across different spws:
#    For BP tables in old format, bandpass is defined in channel, which makes the bandpass transfer between different spws
#    relatively easy. For BP tables in new format, the bandpass solution is defined in frequency with spectral_window_id table
#    in the file. Even you use spwmap and interp, the interpolation and mapping will still be done in freuency-wise.
#    If you consider the passband response is roughly associated with each channel rather than frequency, the spw mapping and
#    interpolation will be meaningless.
#    Here, we use xu.bpcopy() to mirror the bandpass from one spw to another by copying the data table and replace spw tag,
#    which work better than typical spw mapping.
#    The issues happens after CASA adopted new calibration table formats, and was the major reason for the quality degrading
#    in the new stinghi data.
#
# FLAGGING
'flagselect':[],            # flagging before calibration
'flagselect_cal':[],        # flagging after calibration
'flagspw':'',               # flagging based on spw selecting (kept for historical reasons)
                            # flagging edge channel is important for merging spws because overlapping region 
                            # is still equally weighted in CVEL() although MSTRANSFORM() may take care of it in future. 
'flagreset':True,           # reset flagging to the orginal status 
                            # if False, flagging will be accumulated after each run of xcal.py.
'flagtest':False,           # abort processing after flagging
'flagselect_default':[],    # default flagging
                            # examples:
                            #    [mode='shadow']       shadow flagging (will crash flagcmd in B1950 in v4.2)
                            #                          by default, importvla & importevla will flag shadowed antennas. 
                            #    ["antenna='*&&&'"]    flagging auto-correlation.
'dirtol':'',
'freqtol':'',

# BASELINE
'bcant':'',                 # for baseline corrections (useless for HI) here is an example:
'bctype':'antposvla',       # bcant='VA06,VA02,VA03,VA07,VA10,VA11,VA16,VA17,VA18,VA19'
'bcpara':[],                # bcpara=[  -0.0063, -0.0205,  0.0102,
#                                        0.0000,  0.0003, -0.0007,
#                                       -0.0011,  0.0003, -0.0005,
#                                       -0.0013,  0.0000,  0.0000,
#                                       -0.0013,  0.0004,  0.0000,
#                                       -0.0007,  0.0000,  0.0000,
#                                        0.0000, -0.0006,  0.0000,
#                                       -0.0008,  0.0000,  0.0000,
#                                        0.0000, -0.0004,  0.0000,
#                                        0.0000, -0.0004,  0.0000]

# CAL
'interpmode':['linear','nearest'],
'ref_ant':'15',                 # reference antenna name
'calwt':True,                   # set False only for data taken with unreliable weighting info...
'syscal':'default',             # syscal='default': automatically choose the best "system-based" calibration based on the datase type
                                #                   gaincurvel will be turned on if: * data were from VLA & * taken before 2001
                                # syscal=''       : no system pre-calibration
                                # syscal='tsys'...: bring up tsys table .
'scalsmooth':False,             # only tested for EVLA data
'scalsmoothtime':60,            # only tested for EVLA data

'flagtsys':True,                # flagging based on Tsys (only tested for EVLA data)
'flagtsys_range':[5.0,1000.0],  # flagging based on Tsys

# CONSOLIDATE

'spwrgd':'',                # if spwrgd='spw', we will regrid spw to the clean setup
                            # if spwrgd='', we will keep the native spw
                            # 
                            # * clean()/concat() can't work with a dataset with TOPO+LSRK or TOPO+BARY frames
                            # if spwrgd='frame', we will only transform the spw frame to the desired one, which
                            # might help resolve the above issue when combing multiple tracks with various frames.
                            # spwgrd='spw' will also help to reduce the vis data size to the mininmal required:
                            # 
                            # * If the splitted vis already has the channel rebinned, CLEAN() will be speeded up
                            #   because a smaller number vis records were handled during the major cycle.
                            
                            # * (this has been corrected in v4.2.1)
                            #   If two corrs setup are in one spw (which may happen when two tracks with different 
                            #   corr-config were regridding to the same channel setup), CLEAN() will consider
                            #   one corr and ignore another corr. You want to void two corr-setup in one spw
                            #   -> avoid regridding dual-pol and single-pol tracks into the same channel setup.
                            #
'spwrgd_method':'cvel',     # choose the regridding task: CVEL() or MSTRANSFORM() (not stable now)
                            # cvel() may not work properly when combing spws with different polns.
                            # mstransform() may drop edge channels  
'combinespws':True,         # combine spws when regridding spws
'chanbin':0,                
'hs':False,                 # hanning smooth when preparing MS for imaging.
'unchflag':False,           # unflag records with several channel flagged, so each channel has the same flagging
                            # this will be like slop=1 in MIRIAD in some sense 
                            

# CONTINUE SUBTRACTION FOR INDIVIDUAL TRACK
'fitorder':0,               # polynomial order for fitting the continuum
                            # high-order polynomial may work better of the continuum source
                            # is off-center when uvcs=True (Sault 1994)
'uvcs':False,               # continumm subtraction before imaging
'fitspw':'',                # spw selecting for continumm subtraction after imaging
'imcs':False,               # continumm subtraction after imaging
'fitchans':'',              # channel selecting for continumm subtraction after imaging (e.g., fitchans='1~7;79~85')
'uvcs_combine':'spw',       # data axes to combine for the continuum estimate
                            # combine='spw' --> form spw-merged continuum estimate

# COMBING MSs FROM INDIVIDUAL TRACK
'prefix_comb':[],           # names of MS files to be combined 
'freqtol':'',               # frequency tolerant when combing spws.
'usevconcat':False,         # using virtual concat (which is not 
'scalewt':False,            # scaling weight using the WEIGHT_SCALING value saved in MSs during CONCAT()
'visweightscale':[],        # scaling weight using a specified value rather than the WEIGHT_SCALING value in MSs
'scalewt_fitspw':'',        # the data range used to calculate the WEIGHT_SCALING value, default: fitspw
'scalewt_uvrange':'',       # the data range used to calculate the WEIGHT_SCALING value, not implemented
'scalewt_minsamp':2,        # the minimal number of channels required for a reliable sigma/weight calculation 

# CLEAN
'restorbeam':[''],              # use a specified restor beam for imaging
'resmooth':True,                # smooth the channel-dependent beam to a common resolution
'restorbeam_default':[''],      # not useful any more
'restorbeam_method':'maximum',  # not useful any more


'minpb':0.1,                # masked out the region with pb response < minbp
'cleanspw':'',
'phasecenter':'',           # imaging phasecenter, e.g.'J2000 12h18m49.6 14d24m59.01' or '2' (=fieldid2)
'spinterpmode':'linear',    # spectral gridding interpolation mode in CLEAN
'restfreq':'1420405752.0Hz',# rest frequency for imaging (default: 1420.405752MHz)
'outframe':'BARY',          # frame of the output image
'allowchunk':False,

'imsize':2**5*10,           # imaging size (numbers of pixels)
'cell':'8.0arcsec',         # imaging pixel size.
'clean_mask':0.2,           # 0.2:     a clean box with pb response higher 0.2
                            # True:    a clean box with pb response higher <minpb>
                            # [0,0,511,511]:    a clean box specified by bl/tr
                            # 'cleanbox.txt'    a cleanbox file   
'niter':10000,              # clean iteration threshold
'sigcutoff_spec':2.0,       # <sigcutoff_spec>*<sig> is the default threshold value for spectral-cube CLEAN
'sigcutoff_cont':2.0,       # <sigcutoff_cont>*<sig> is the default threshold value for continuum MFS CLEAN
'threshold_spec':'0.0mJy',  # threshold for spec cleaning, the default value is <sigcutoff_spec>*<sig>
'threshold_cont':'0.0mJy',  # threshold for mfs cleaning, the default values is <sigcutoff_cont>*<sig>

'imstat_box_spec':'',       # a box selected for RMS calculations, default: inner quarters
'imstat_rg_spec':'',        # a region selected for RMS calculations
'imstat_chan':'',           # 
'imstat_box_cont':'',       # a box selected for the RMS calculations, default: inner quarters
'imstat_rg_cont':'',        # a region selected for RMS calculations

'imagermode':None,          # imagermode for clean, options include: 'csclean', 'mosaic' 
                            # 'mosaic' must be be used if your science target is in 
                            # multiple fields or it's heterogeneous-array observation.
                            # 'csclean' for single point+homogeneous array data.
                            # by default, it will automatically choose the best option after inspecting the data
'ftmachine':'ft',           # For CARMA, you must always use ftmachine='mosaic', because it is a heterogeneous array.
                            # by default, it will automatically choose the best option after inspecting the data
'multiscale':[],            # using multi-scale clean is not the default setting
                            # multi_scale=[0,1,3,10,30] is recommened, and units is pixel
'cyclefactor':1.5,
'clean_gain':0.1,           # gain factor for clean, 
                            # for multiscale clean, clean_gain can be higher (e.g. 0.7)
'clean_field':'',

'cleanweight':'briggs',     # e.g. 'briggs', 'uniform' or 'natural'
'cleanspw':'',
'iterchan':False,
'outertaper':[],            # taper function for weighting
'cleanspec':True,           # imaging spectral line?
'wrobust':0.5,              # robust weight "R" parameter
'gridmode':'aprojection',

'cleanmode':'channel',      # e.g. "channel" or "velocity"
'clean_start':'',           # first channel/velocity to clean
'clean_width':1,            # number of input channels to average or the velocity width for each image plane 
'clean_nchan':-1,           # number of planes in the output image
'keepcasaimage':True,       # keep a copy casa images after exporting them to FITS

'mosweight':False,          # mosweight in CLEAN()
                            # ????
                            # mosweight=True equivalent as
                            # 
                            #   inverting each pointing by its own weights and 1/noise^2-weight each pointing in mosaicing
                            #   this is similar with MIRAID/MOSSDI and will give more weight to higher sensitivity fields 
                            #   in the overlap regions.(good for sting-co)
                            #   will produce an image optimzed local SNR, but scarify the uniformity 
                            #   of noise and psf across the whole mosaicing pattern. Usually it will produce a slight larger
                            #   beam.
                            # 
                            # mosweight=True is closer to MIRAID's linear-mosaicing approach becaue each pointig are
                            # inverted independently (less phase bluring). 
                            # Although the primary pattern & the weight for each pointing (from integration time) are still embeded in the
                            # the basic weight and the additional PB pattern convolved during UV gridding.                            
                            #   ??
                            #   Since a global UV sampling density function doesn't make much sense when combing
                            #   multiple tracks with several pointing because the phase-shifting from different point 
                            #   will reduce local sensitiviy by bluring phase information.
                            #   ??
                            #
                            # mosweight=False  equivalent as
                            #   inverting each pointing and equal-weight each pointing
                            #   weights from vis in each weight are used in absolute sense afer gridding them into 
                            #   the common regridding UV frame.
                            #
                            # ???
                            # MOSWEIGHT determines whether to calculate the gridding weights for each field independently
                            # or together, so mosweight doesn't matter for natural weighting.
                            #
                            #
                            # If the UV coverage is very different, it might doesn't much difference.
                            # ????
'psfmode':'clark',          # psfmode in CLEAN()
'fitpsf':False,             # out-of-date, not verified
'negcomponent':-1,          # allowed number of negative component for CLEAN components at the largest scale
'cleancont':False,          # imaging continuum using MFS
'usescratch':False,         # create model column when CLEAN()


# PLOTTING
'plotformat':'pdf',         # out-of-date, not verified

# INFOMATIVE
'email':'',                 # notification email address
'password':'',              # notification email password
'version':'',               # script versaion, not implemented
'log_listobs_msfile':'',    # not implemented
}
