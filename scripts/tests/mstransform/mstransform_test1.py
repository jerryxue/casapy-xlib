####
#   This test tries to regrid two partly overlapping spws into one with desired channel setup.
####
option=1#1,2,3,4
import xu as xu
    
os.system("rm -rf n0337d03.src.ms")
os.system("rm -rf n0337d03.src.ms.tmp")
t1=time.time()

#############
# OPTION 1: MSTRANSFORM (combinespws=True+regridms=True)
#
# note: overlapping channels are flagged..... 
#############
if  option==1:
    mstransform(vis="n0337d03.ms",monolithic_processing=False,outputvis="n0337d03.src.ms",createmms=False,separationaxis="spw",
        numsubms=64,disableparallel=False,ddistart=-1,tileshape=[0],field="NGC0337",
        spw="1,0",scan="",antenna="",correlation="",timerange="",
        intent="",array="",uvrange="",observation="",feed="",
        datacolumn="corrected",realmodelcol=False,keepflags=False,usewtspectrum=False,combinespws=True,
        chanaverage=False,chanbin=1,hanning=False,regridms=True,mode="velocity",
        nchan=107,start="1360.00km/s",width="5.2km/s",nspw=1,interpolation="linear",
        phasecenter="",restfreq="1420405752.0Hz",outframe="BARY",veltype="radio",timeaverage=False,
        timebin="0s",timespan="",maxuvwdistance=0.0)
"""
2015-01-07 19:36:15    INFO    ++++++::::casa    poln: 0 type: 4
2015-01-07 19:36:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111110000000000000000000000000000000000001111111 24387/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 204/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000001111111 179/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 76/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    poln: 1 type: 4
2015-01-07 19:36:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111110000000000000000000000000000000000001111111 24408/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 234/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000001111111 52/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 152/24846
2015-01-07 19:36:15    INFO    ++++++::::casa    
"""
#############
# OPTION 2: cvel2
#
# note: center channels are still flagged (cvel2 is using mstransform)
#############
if  option==2:
    
    cvel2(vis="n0337d03.ms",outputvis="n0337d03.src.ms",field="NGC0337",spw="",
        antenna="",timerange="",scan="",array="",datacolumn='corrected',
        mode="velocity",nchan=107,start="1360.00km/s",width="5.2km/s",interpolation="linear",
        phasecenter="",restfreq="1420405752.0Hz",outframe="BARY",veltype="radio",hanning=False)
"""
2015-01-07 20:16:02    INFO    ++++++::::casa    poln: 0 type: 4
2015-01-07 20:16:02    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111110000000000000000000000000000000000001111111 24387/26354
2015-01-07 20:16:02    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 204/26354
2015-01-07 20:16:02    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000001111111 179/26354
2015-01-07 20:16:02    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 1584/26354
2015-01-07 20:16:03    INFO    ++++++::::casa    poln: 1 type: 4
2015-01-07 20:16:03    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111110000000000000000000000000000000000001111111 24408/26354
2015-01-07 20:16:03    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 234/26354
2015-01-07 20:16:03    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111110000000000000000000000000000000000001111111 52/26354
2015-01-07 20:16:03    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 1660/26354
"""
#############
# OPTION 3: CVEL
#
# note: works fine even it's slower than mstransform()
#############
if  option==3:
    split(vis="n0337d03.ms",outputvis="n0337d03.src.ms.tmp",datacolumn="corrected",field="",spw="0,1",
        width=1,antenna="",timebin="0s",timerange="",scan="",
        intent="",array="",uvrange="",correlation="",observation="",
        combine="",keepflags=False,keepmms=False)
    cvel(vis="n0337d03.src.ms.tmp",outputvis="n0337d03.src.ms",passall=False,field="NGC0337",spw="",
        selectdata=True,antenna="",timerange="",scan="",array="",
        mode="velocity",nchan=107,start="1360.00km/s",width="5.2km/s",interpolation="linear",
        phasecenter="",restfreq="1420405752.0Hz",outframe="BARY",veltype="radio",hanning=False)
"""
2015-01-07 19:41:42    INFO    ++++++::::casa    n0337d03.src.ms (2, 107, 24846)
2015-01-07 19:41:42    INFO    ++++++::::casa    poln: 0 type: 4
2015-01-07 19:41:42    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111 24387/24846
2015-01-07 19:41:42    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 204/24846
2015-01-07 19:41:42    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000001111111 179/24846
2015-01-07 19:41:42    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 76/24846
2015-01-07 19:41:43    INFO    ++++++::::casa    poln: 1 type: 4
2015-01-07 19:41:43    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111 24408/24846
2015-01-07 19:41:43    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 234/24846
2015-01-07 19:41:43    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000001111111 52/24846
2015-01-07 19:41:43    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 152/24846
"""
#############
# OPTION 4: MSTRANSFORM twice (combinespws=True)+(regridms=True)
#
# note: works fine
#############
if  option==4:
    mstransform(vis="n0337d03.ms",monolithic_processing=False,outputvis="n0337d03.src.ms.tmp",createmms=False,separationaxis="spw",
        numsubms=64,disableparallel=False,ddistart=-1,tileshape=[0],field="NGC0337",
        spw="1,0",scan="",antenna="",correlation="",timerange="",
        intent="",array="",uvrange="",observation="",feed="",
        datacolumn="corrected",realmodelcol=False,keepflags=False,usewtspectrum=False,combinespws=False,
        chanaverage=False,chanbin=1,hanning=False,regridms=True,mode="velocity",
        nchan=107,start="1360.00km/s",width="5.2km/s",nspw=1,interpolation="linear",
        phasecenter="",restfreq="1420405752.0Hz",outframe="BARY",veltype="radio",timeaverage=False,
        timebin="0s",timespan="",maxuvwdistance=0.0)
    mstransform(vis="n0337d03.src.ms.tmp",outputvis="n0337d03.src.ms",datacolumn="data",field="",keepflags=False,combinespws=True)
"""
2015-01-07 19:47:15    INFO    ++++++::::casa    poln: 0 type: 4
2015-01-07 19:47:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111 24387/24846
2015-01-07 19:47:15    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 204/24846
2015-01-07 19:47:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000001111111 179/24846
2015-01-07 19:47:15    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 76/24846
2015-01-07 19:47:16    INFO    ++++++::::casa    poln: 1 type: 4
2015-01-07 19:47:16    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111 24408/24846
2015-01-07 19:47:16    INFO    ++++++::::casa    11000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111 234/24846
2015-01-07 19:47:16    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000001111111 52/24846
2015-01-07 19:47:16    INFO    ++++++::::casa    11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 152/24846
2015-01-07 19:47:16    INFO    ++++++::::casa    
"""

t2=time.time()
xu.news(t2-t1)

os.system("rm -rf n0337d03.src.ms.tmp")
listobs("n0337d03.src.ms")
xu.checkchflag("n0337d03.src.ms")