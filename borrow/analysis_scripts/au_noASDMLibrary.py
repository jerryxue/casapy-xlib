# This file contains functions that have been replaced in
# analysisUtils by newer functions which use the ASDM bindings
# library.  We need to keep these for usage on machines that do not
# have this library installed.  - Todd Hunter

import os
import math
from xml.dom import minidom

def readSoftwareVersionFromASDM_minidom(asdm):
    """
    Reads the software version from the ASDM's Annotation.xml table.
    - Todd Hunter
    """
    if (os.path.exists(asdm) == False):
        print "readSoftwareVersionFromASDM_minidom(): Could not find ASDM = ", asdm
        return(None)
    if (os.path.exists(asdm+'/Annotation.xml') == False):
        print "readSoftwareVersionFromASDM_minidom(): Could not find Annotation.xml. This dataset was probably taken prior to R10.6."
        return(None)

    xmlscans = minidom.parse(asdm+'/Annotation.xml')
    scandict = {}
    rowlist = xmlscans.getElementsByTagName("row")
    print '\n### Software version for ASDM: %s ###' % asdm
    for i,rownode in enumerate(rowlist):
        row = rownode.getElementsByTagName("issue")
        issue = str(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("details")
        details = str(row[0].childNodes[0].nodeValue)
        print "%s: %s" % (issue,details)
    return

def readStationFromASDM_minidom(sdmfile):
    """
    Reads the Station.xml file and returns a dictionary of all stations
    of the following format:
    mydict[0] = {'name': 'A085', position=[x,y,z]}
    -Todd Hunter
    """
    if (os.path.exists(sdmfile) == False):
        print "readStationFromASDM(): Could not find file = ", sdmfile
        return(None)
    xmlscans = minidom.parse(sdmfile+'/Station.xml')
    scandict = {}
    rowlist = xmlscans.getElementsByTagName("row")
    fid = 0
    stationName = 'unknown'
    mydict = {}
    for rownode in rowlist:
        stationPosition = []
        scandict[fid] = {}
        row = rownode.getElementsByTagName("stationId")
        stationId = int(str(row[0].childNodes[0].nodeValue).split('_')[-1])
        row = rownode.getElementsByTagName("name")
        stationName = str(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("position")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        for i in range(2,len(r)):
            stationPosition.append(float(r[i]))
        mydict[stationId] = {'name': stationName, 'position': stationPosition}
        fid +=1
    return(mydict)
    
def readStationsFromASDM_minidom(sdmfile, station=None):
    """
    Translates a station number (which start from 0) into the station name and
    position from the Station.xml file.  Useful for finding this information
    for weather stations.
    If station==None, then it builds and returns a dictionary where the key is
    the station name and the value is the geocentric [X,Y,Z] position.
    e.g. {'A001': [x,y,z]}
    - Todd Hunter
    """
    if (os.path.exists(sdmfile) == False):
        print "readStationFromASDM(): Could not find file = ", sdmfile
        return(None)
    xmlscans = minidom.parse(sdmfile+'/Station.xml')
    scandict = {}
    rowlist = xmlscans.getElementsByTagName("row")
    fid = 0
    stationName = 'unknown'
    if (station == None):
        mydict = {}
    for rownode in rowlist:
        stationPosition = []
        scandict[fid] = {}
        row = rownode.getElementsByTagName("stationId")
        stationId = int(str(row[0].childNodes[0].nodeValue).split('_')[-1])
        row = rownode.getElementsByTagName("name")
        stationName = str(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("position")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        for i in range(2,len(r)):
            stationPosition.append(float(r[i]))
        if (stationId == station):
            break
        elif (station == None):
            mydict[stationName] = stationPosition
        fid +=1
    if (station == None):
        return(mydict)
    else:
        return(stationName,stationPosition)

def getSubscanTimesFromASDM_minidom(asdm, field=''):
    """
    Reads the subscan information from the ASDM's Subscan.xml file and
    returns a dictionary of form:
    {scan: {subscan: {'field': '3c273, 'integrationTime': 2.016,
                      'numIntegration': 5, 'subscanLength': 10.08}}}
    where the scan numbers are the top-level keys.  The subscanLength is
    computed by the difference between endTime and startTime.  The integration
    time is computed by dividing the subscanLength by numIntegration.
    If the field name is specified, then limit the output to scans on this
    field.
    -- Todd Hunter
    """
    subscanxml = asdm + '/Subscan.xml'
    if (os.path.exists(subscanxml) == False):
        print "Could not open %s" % (subscanxml)
        return
    xmlscans = minidom.parse(subscanxml)
    rowlist = xmlscans.getElementsByTagName("row")
    scandict = {}
    scanNumbers = 0
    subscanTotalLength = 0
    for rownode in rowlist:
        row = rownode.getElementsByTagName("scanNumber")
        scanNumber = int(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("subscanNumber")
        subscanNumber = int(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("startTime")
        startTime = int(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("endTime")
        endTime = int(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("numIntegration")
        numIntegration = int(row[0].childNodes[0].nodeValue)
        row = rownode.getElementsByTagName("fieldName")
        fieldName = str(row[0].childNodes[0].nodeValue)
        if (field=='' or fieldName==field):
            subscanLength = (endTime-startTime)*1e-9
            subscanTotalLength += subscanLength
            integrationTime = subscanLength / (1.0*numIntegration)
            if (scanNumber not in scandict):
                if (scanNumber == 1):
                    scan1startTime = startTime
                scandict[scanNumber] = {}
                scanNumbers += 1
            scandict[scanNumber][subscanNumber] = {'subscanLength': subscanLength, 'numIntegration': numIntegration, 'integrationTime': integrationTime, 'field': fieldName, 'startTime':startTime*1e-9, 'endTime':endTime*1e-9}
    print "Found %d scans" % (scanNumbers)
    totalTime = (endTime-scan1startTime)*1e-9
    latency = totalTime - subscanTotalLength
    print "Total latency = %g/%g seconds = %g percent" % (latency, totalTime, latency*100/totalTime)
    return(scandict)

def readDecorrelationFromASDM_minidom(asdm):
    """
    -Todd Hunter
    """
    mydict = {}
    seeingxml = asdm + '/CalPhase.xml'
    if (os.path.exists(seeingxml) == False):
        print "Could not open %s" % (seeingxml)
        return
    xml = minidom.parse(seeingxml)
    rowlist = xml.getElementsByTagName("row")
    mydict['basebandName'] = []
    mydict['receiverBand'] = []
    mydict['numReceptor'] = []
    mydict['baselineLengths'] = []
    mydict['decorrelationFactor'] = []
    mydict['startValidTime'] = []
    mydict['endValidTime'] = []
    mydict['atmPhaseCorrection'] = []
    mydict['integrationTime'] = []
    mydict['azimuth'] = []
    mydict['elevation'] = []
    mydict['calDataId'] = []
    for rownode in rowlist:
        row = rownode.getElementsByTagName("startValidTime")
        mydict['startValidTime'].append(int(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("endValidTime")
        mydict['endValidTime'].append(int(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("atmPhaseCorrection")
        mydict['atmPhaseCorrection'].append(str(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("receiverBand")
        mydict['receiverBand'].append(str(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("basebandName")
        mydict['basebandName'].append(str(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("numReceptor")
        mydict['numReceptor'].append(int(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("calDataId")
        mydict['calDataId'].append(int(str(row[0].childNodes[0].nodeValue).split('_')[1]))
        row = rownode.getElementsByTagName("integrationTime")
        mydict['integrationTime'].append(float(row[0].childNodes[0].nodeValue)*1e-9)
        row = rownode.getElementsByTagName("baselineLengths")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        baselineLengths = []
        for i in range(2,len(r)):
            baselineLengths.append(float(r[i]))
        mydict['baselineLengths'].append(baselineLengths)
        row = rownode.getElementsByTagName("decorrelationFactor")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        decorrelationFactor = []
        for i in range(3,len(r)):
            decorrelationFactor.append(float(r[i]))
        mydict['decorrelationFactor'].append(decorrelationFactor)
        row = rownode.getElementsByTagName("direction")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        direction = []
        for i in range(2,len(r)):
            direction.append(float(r[i]))
        mydict['azimuth'].append(math.degrees(direction[0]))
        mydict['elevation'].append(math.degrees(direction[1]))
    print "Found %d measurements on %d baselines" % (len(mydict['atmPhaseCorrection']), len(mydict['baselineLengths'][0]))
    return mydict
    
    
def readSeeingFromASDM_minidom(asdm):
    """
    Reads information from CalSeeing.xml into a dictionary
    Returns a dictionary with the following keys:
    atmPhaseCorrection: AP_UNCORRECTED or AP_CORRECTED
    baselineLengths: typically 3 values (in meters)
    startValidTime: MJD nano seconds
    endValidTime: MJD nano seconds
    phaseRMS:  a value for each baselineLength (radians?) for each timestamp
    seeing: one value per timestamp (arcseconds)
    -Todd Hunter
    """
    mydict = {}
    seeingxml = asdm + '/CalSeeing.xml'
    if (os.path.exists(seeingxml) == False):
        print "Could not open %s" % (seeingxml)
        return
    xml = minidom.parse(seeingxml)
    rowlist = xml.getElementsByTagName("row")
    mydict['seeing'] = []
    mydict['phaseRMS'] = []
    mydict['startValidTime'] = []
    mydict['endValidTime'] = []
    mydict['atmPhaseCorrection'] = []
    mydict['baselineLengths'] = []
    mydict['phaseRMS'] = []
    for rownode in rowlist:
        row = rownode.getElementsByTagName("seeing")
        mydict['seeing'].append(float(row[0].childNodes[0].nodeValue)*206264.8)
        row = rownode.getElementsByTagName("startValidTime")
        mydict['startValidTime'].append(int(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("endValidTime")
        mydict['endValidTime'].append(int(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("atmPhaseCorrection")
        mydict['atmPhaseCorrection'].append(str(row[0].childNodes[0].nodeValue))
        row = rownode.getElementsByTagName("baselineLengths")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        baselineLengths = []
        for i in range(2,len(r)):
            baselineLengths.append(float(r[i]))
        mydict['baselineLengths'].append(baselineLengths)
        row = rownode.getElementsByTagName("phaseRMS")
        r = filter(None,(row[0].childNodes[0].nodeValue).split(' '))
        phaseRMS = []
        for i in range(2,len(r)):
            phaseRMS.append(float(r[i]))
        mydict['phaseRMS'].append(phaseRMS)
    print "Found %d measurements" % (len(mydict['atmPhaseCorrection']))
    return mydict
