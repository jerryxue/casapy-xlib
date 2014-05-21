#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
import casac
import string
from taskinit import casalog
#from taskmanager import tm
import task_alignbyvel
def alignbyvel(infile='', outfile='', template='', overwrite=True):

        """regrid an image to match a template image in velocity

        alignbyvel: align one cube to the velocity axis of another.

        The new coordinate system is drawn from the template image.

    	Keyword arguments:
    	infile -- 
    	template -- 
    	outfile -- 
        async -- Run task in a separate process (return CASA prompt)
                default: False; example: async=True


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['outfile'] = outfile
        mytmp['template'] = template
        mytmp['overwrite'] = overwrite
        pathname="file:///users/aleroy/akl_python/akl_tasks/"
        trec = casac.cu.torecord(pathname+'alignbyvel.xml')

        casalog.origin('alignbyvel')
        if trec.has_key('alignbyvel') and casac.cu.verify(mytmp, trec['alignbyvel']) :
	    result = task_alignbyvel.alignbyvel(infile, outfile, template, overwrite)

	else :
	  result = False
        return result
