
### Patch/Hack for the Official CASA codes

The original codes were usually in a software path like this:

    casa-release-4.7.0-el7/lib/python2.7/

Just replace them with the modified version here.

### CASA Version 4.7.0-REL (r38335)

    cleanheper.py
    task_clean.py

*   fix a minor issue that image tables could be left open / locked after CLEAN
(reported to the Helpdesk).
*   fix a problem that .flux was always masked at PB<0.1 when imagermode='csclean'.
