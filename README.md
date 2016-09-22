
### CASA-xlib

The CASA-based data reduction pipeline for the STING-HI project

This repository contains various CASA modules written in Python for the data reduction in the STING-CO/HI project. Although most of codes are written as a pipeline for this project, I do write them as general as possible, so the entire packages can be easily adopted for large interferometer projects. Some highlights of useful general purpose CASA modules include:

* xutils.py/sumwt

* xutils.py/importmir

* xutils.py/carmapb

* xutils.py/getuvlist

* xutils.py/exportcasalog

* xutils.py/copyweight

* xutils.py/checkchflag

* xutils.py/scalewt

* xutils.py/bpcopy

* xutils.py/checkuvrange


### Install


Download the update-to-date version of this library using the following command:

    git clone http://github.com/r-xue/casapy-xlib.git

Check out the comment section in /xlib/init.py for the setup details

Examples:

    VLA 21cm HI data reduction  -- scripts/sting-hi/n4254hi.py
    CARMA CO 1-0 imaging        -- scripts/sting-co/n4254co.py
