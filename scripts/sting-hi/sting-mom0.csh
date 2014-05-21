#!/bin/csh -f
#
#   this script will produce mom0 maps for CASA products
#   e.g. mommsc.csh gal=0337
#   

set gal=

set fluxclip=4      # min allowed flux (Jy/bm km/s) for gaufits
set velclip=20      # max allowed velocity error (km/s) for gaufits
set fwhm=9          # FWHM of smoothed map for masking method
set nspan=3         # number of channels from peak to integrate for wmom0
set mom0fun=sqr     # Use n^2 (sqr) or log contours from mom-0 plots
set mom0lev=        # First contour level, default is 3-sigma
set psbox=          # custom box for plotting

set showplot=n
set tag="co"

foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

# the below part is copied from ccombine.csh

moment.csh file=n"$gal"${tag}.line.cm noisemap=n"$gal"${tag}.line.sen start=straight \
    nspan=$nspan interact='n' advskip='y' noplot='y' usecube='y'
moment.csh file=n"$gal"${tag}.line.cm noisemap=n"$gal"${tag}.line.sen start=mask \
    fwhm=$fwhm interact='n' usecube='y' noplot='y'
#moment.csh file=n"$gal"${tag}.line.cm noisemap=n"$gal"${tag}.line.sen start=gaufit \
#    fluxclip=$fluxclip velclip=$velclip
moment.csh file=n"$gal"${tag}.line.cm start=cleanup noplot='y'

# the below part is copied from ccombine.csh

set source=n${gal}${tag}.line

# Plot the mom-0 and peak brightness maps
if ($mom0fun == 'sqr') then
    set levs=1,4,9,16,25,36,49,81,100
else
    set levs=`awk -v del=$loglevs 'BEGIN {for (i=0;i<10;i++) printf "%3.1f,",10**(i*del); printf "%3.1f\n",10**(10*del)}'`
endif
set maxval=`histo in=$source.mmom0 | grep Max | awk '{print $3}'`
set mom0rms=`histo in=$source.dmom0.nse | grep Min | awk '{print $3}'`
echo "The rms of the dmom0 image is $mom0rms"
if ($mom0lev == '') then
    set mom0lev=`calc "2.0*$mom0rms"`
endif
mv $source.mmom0/mask $source.mmom0/mask1
cgdisp in=$source.mmom0,$source.mmom0 type=p,c \
    region=$psbox device=$source.mmom0.ps/cps \
    range=0,$maxval,lin,-8 slev=a,$mom0lev levs1=$levs \
    labtyp=hms,dms nxy=1,1 options=black,wedge,full cols1=1 csize=1 \
    lines=2,1 beamtyp=b,l
if ($showplot != 'n') then
    gv $source.mmom0.ps &
endif
mv $source.mmom0/mask1 $source.mmom0/mask

set crms=`histo in=$source.sen | grep Min | awk '{print $3}'`
set maxval=`histo in=$source.peak | grep Max | awk '{print $3}'`
cgdisp in=$source.peak,$source.peak type=p,c \
    region=$psbox device=$source.peak.ps/cps \
    range=0,$maxval,lin,-8 slev=a,$crms levs1=$levs \
    labtyp=hms,dms nxy=1,1 options=black,solneg2,wedge,full cols1=1 csize=1 \
    lines=2,1 beamtyp=b,l
if ($showplot != 'n') then
    gv $source.peak.ps &
endif
