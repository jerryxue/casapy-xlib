####
#   This test tries to regrid three partly overlapping spws into one with desired channel setup.
####    

os.system("rm -rf E4.src.ms")
os.system("rm -rf E4.src.ms.tmp")
t1=time.time()

option=1#1,2,3
import xu as xu

#############
# OPTION 1: MSTRANSFORM (combinespws=True/regridms=True)
#
# note: overlapping channels are flagged 
#############
if  option==1:
    mstransform(vis="E4.ms",outputvis="E4.src.ms",field="",spw="",
         antenna="",timerange="",scan="",array="",datacolumn='data',
         mode="velocity",nchan=53,start="2265km/s",width="5km/s",interpolation="linear",
         combinespws=True,regridms=True,
         phasecenter="",restfreq="115.2712GHz",outframe="LSRK",veltype="radio",hanning=False)
"""
2015-01-07 21:00:54    INFO    ++++++::::casa    E4.src.ms (1, 53, 28114)
2015-01-07 21:00:54    INFO    ++++++::::casa    poln: 0 type: 1
2015-01-07 21:00:54    INFO    ++++++::::casa    00000000000010000000000000000000000000110000000000000 28114/28114
"""
#############
# OPTION 2: MSTRANSFORM twice (combinespws=True)+(regridms=True)
#
# note: I can't get desired spw because the below override
#       *** Requested center of SPW 1.1435e+11 Hz is too large by 2.62591e+07 Hz 
#############

if  option==2:
    mstransform(vis="E4.ms",outputvis="E4.src.ms.tmp",field="",spw="",
         antenna="",timerange="",scan="",array="",datacolumn='data',
         mode="velocity",nchan=53,start="2265km/s",width="5km/s",interpolation="linear",
         combinespws=False,regridms=True,
         phasecenter="",restfreq="115.2712GHz",outframe="LSRK",veltype="radio",hanning=False)
    mstransform(vis="E4.src.ms.tmp",outputvis="E4.src.ms",datacolumn="data",field="",keepflags=False,combinespws=True)
"""
2015-01-07 21:05:18    INFO    mstransform::::casa    
2015-01-07 21:05:18    INFO    mstransform::::casa+    ##########################################
2015-01-07 21:05:18    INFO    mstransform::::casa+    ##### Begin Task: mstransform        #####
2015-01-07 21:05:18    INFO    mstransform::::casa    mstransform(vis="E4.ms",monolithic_processing=False,outputvis="E4.src.ms.tmp",createmms=False,separationaxis="auto",
2015-01-07 21:05:18    INFO    mstransform::::casa+            numsubms=64,disableparallel=False,ddistart=-1,tileshape=[0],field="",
2015-01-07 21:05:18    INFO    mstransform::::casa+            spw="",scan="",antenna="",correlation="",timerange="",
2015-01-07 21:05:18    INFO    mstransform::::casa+            intent="",array="",uvrange="",observation="",feed="",
2015-01-07 21:05:18    INFO    mstransform::::casa+            datacolumn="data",realmodelcol=False,keepflags=True,usewtspectrum=False,combinespws=False,
2015-01-07 21:05:18    INFO    mstransform::::casa+            chanaverage=False,chanbin=1,hanning=False,regridms=True,mode="velocity",
2015-01-07 21:05:18    INFO    mstransform::::casa+            nchan=53,start="2265km/s",width="5km/s",nspw=1,interpolation="linear",
2015-01-07 21:05:18    INFO    mstransform::::casa+            phasecenter="",restfreq="115.2712GHz",outframe="LSRK",veltype="radio",timeaverage=False,
2015-01-07 21:05:18    INFO    mstransform::::casa+            timebin="0s",timespan="",maxuvwdistance=0.0)
2015-01-07 21:05:18    INFO    mstransform::::casa    Parse regridding parameters
2015-01-07 21:05:18    INFO    MSTransformManager::parseMsSpecParams    Input file name is E4.ms
2015-01-07 21:05:18    INFO    MSTransformManager::parseMsSpecParams    Output file name is E4.src.ms.tmp
2015-01-07 21:05:18    INFO    MSTransformManager::parseMsSpecParams    Data column is DATA
2015-01-07 21:05:18    INFO    MSTransformManager::parseMsSpecParams    Tile shape is [0]
2015-01-07 21:05:18    INFO    MSTransformManager::parseRefFrameTransParams    Regrid MS is activated
2015-01-07 21:05:18    INFO    MSTransformManager::parseRefFrameTransParams    Rest frequency is 115.2712GHz
2015-01-07 21:05:18    INFO    MSTransformManager::parseRefFrameTransParams    Output reference frame is LSRK
2015-01-07 21:05:18    INFO    MSTransformManager::parseRefFrameTransParams    Interpolation method is linear
2015-01-07 21:05:18    INFO    MSTransformManager::parseFreqSpecParams    Mode is velocity
2015-01-07 21:05:18    INFO    MSTransformManager::parseFreqSpecParams    Number of channels is 53
2015-01-07 21:05:18    INFO    MSTransformManager::parseFreqSpecParams    Start is 2265km/s
2015-01-07 21:05:18    INFO    MSTransformManager::parseFreqSpecParams    Width is 5km/s
2015-01-07 21:05:18    INFO    MSTransformManager::parseFreqSpecParams    Velocity type is radio
2015-01-07 21:05:18    INFO    MSTransformManager::open    Select data
2015-01-07 21:05:18    INFO    MSTransformManager::checkDataColumnsToFill    Adding DATA column to output MS 
2015-01-07 21:05:18    INFO    MSTransformManager::open    Create output MS structure
2015-01-07 21:05:18    INFO    MSTransformManager::checkFillWeightSpectrum    Optional column WEIGHT_SPECTRUM found in input MS will be written to output MS
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwSubTable    Regridding SPW with Id 0
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Input SPW:    63 channels, first channel = 1.143153620e+11 Hz, last channel = 1.143759089e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Calculate frequencies in output reference frame 
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs     Channels equidistant in vrad
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Central frequency (in output frame) = 1.1435e+11 Hz == 2.395e+06 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Width of central channel (in output frame) = 1.92252e+06 Hz == 5000 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Number of channels = 53
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Total width of SPW (in output frame) = 1.01893e+08 Hz
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Lower edge = 1.14299e+11 Hz, upper edge = 1.14401e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Output SPW:    53 channels, first channel = 1.143003291e+11 Hz, last channel = 1.144002999e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwSubTable    Regridding SPW with Id 1
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Input SPW:    63 channels, first channel = 1.142639968e+11 Hz, last channel = 1.143245437e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Calculate frequencies in output reference frame 
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs    *** Requested center of SPW 1.1435e+11 Hz is too large by 2.62591e+07 Hz
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+    *** Reset to maximum possible value 1.14325e+11 Hz Channels equidistant in vrad
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Central frequency (in output frame) = 1.14325e+11 Hz == 2.46075e+06 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Width of central channel (in output frame) = 1.92252e+06 Hz == 5000 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Number of channels = 53
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Total width of SPW (in output frame) = 1.01893e+08 Hz
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Lower edge = 1.14274e+11 Hz, upper edge = 1.14376e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Output SPW:    53 channels, first channel = 1.142750465e+11 Hz, last channel = 1.143750174e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwSubTable    Regridding SPW with Id 2
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Input SPW:    63 channels, first channel = 1.143667272e+11 Hz, last channel = 1.144272741e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Calculate frequencies in output reference frame 
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs    *** Requested center of SPW 1.1435e+11 Hz is smaller than minimum possible value by 1.59244e+07 Hz
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+    *** Reset to minimum possible value 1.14366e+11 Hz Channels equidistant in vrad
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Central frequency (in output frame) = 1.14366e+11 Hz == 2.35358e+06 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Width of central channel (in output frame) = 1.92252e+06 Hz == 5000 m/s radio velocity
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Number of channels = 53
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Total width of SPW (in output frame) = 1.01893e+08 Hz
2015-01-07 21:05:18    INFO    MSTransformRegridder::calcChanFreqs+     Lower edge = 1.14315e+11 Hz, upper edge = 1.14417e+11 Hz
2015-01-07 21:05:18    INFO    MSTransformManager::regridSpwAux    Output SPW:    53 channels, first channel = 1.143162535e+11 Hz, last channel = 1.144162244e+11 Hz
2015-01-07 21:05:18    INFO    ParallelDataHelper::::casa    Apply the transformations
2015-01-07 21:05:29    INFO    ParallelDataHelper::::casa    ##### End Task: mstransform          #####
2015-01-07 21:05:29    INFO    ParallelDataHelper::::casa+    ##########################################
"""

#############
# OPTION 3: cvel
#
# note: it works fine even its slower
#############
if  option==3:
    cvel(vis="E4.ms",outputvis="E4.src.ms",passall=False,field="",spw="",
         selectdata=True,antenna="",timerange="",scan="",array="",
         mode="velocity",nchan=53,start="2265km/s",width="5km/s",interpolation="linear",
         phasecenter="",restfreq="115.2712GHz",outframe="LSRK",veltype="radio",hanning=False)
"""
2015-01-07 20:57:11    INFO    ++++++::::casa    E4.src.ms (1, 53, 28114)
2015-01-07 20:57:11    INFO    ++++++::::casa    poln: 0 type: 1
2015-01-07 20:57:11    INFO    ++++++::::casa    00000000000000000000000000000000000000000000000000000 28114/28114
"""    

t2=time.time()
xu.news(t2-t1)

os.system("rm -rf E4.src.ms.tmp")
listobs("E4.src.ms")
xu.checkchflag("E4.src.ms")