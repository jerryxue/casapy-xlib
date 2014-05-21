#!/bin/csh -f
#
#   this script will load the CASA fits into MIR cubes
#   note:   we apply the msklev=2 masking extracted from the middle plane
#           to all planes
#
#	<n${gal}co.line.image>-<n${gal}co.line.res>=<n${gal}co.line.con>
#
#	running location:	/Volumes/data3/ruixue1/sting/msc/maps-mir

set msc_repo=".."
set msklev=2

foreach gal (   0337 0772 1156 1569 1637 2681 \
                2782 2976 3147 3198 3486 3593 \
                3949 4151 4254 4273 4536 4605 \
                4654 5371 5713 6503 6951)    

# load msc cubes
rm -rf n${gal}
mkdir n${gal}
foreach inp ( cm sen res image model flux )
	rm -rf n${gal}/n${gal}co.line.$inp.fits
	cp -rf $msc_repo/n${gal}/n${gal}co.line.$inp.fits n${gal}/n${gal}co.line.$inp.fits
	wcsfix.csh file=n${gal}/n${gal}co.line.$inp.fits frame='VELO-LSR'
	rm -rf n${gal}/n${gal}co.line.$inp.fits
end
rm -rf n${gal}/n${gal}co.line.cln
maths exp="<n${gal}/n${gal}co.line.model>/<n${gal}/n${gal}co.line.flux>" out=n${gal}/n${gal}co.line.cln

# create a msklev=2 masking IMAGE

set nmaps=`gethd in=n${gal}/n${gal}co.line.sen/naxis3`
set mi=`calc -i "$nmaps/2"`

rm -rf n${gal}/n${gal}co.line.sen0 n${gal}/n${gal}co.line.sen1 n${gal}/n${gal}co.line.sen2
imsub in=n${gal}/n${gal}co.line.sen out=n${gal}/n${gal}co.line.sen0 region="images($mi)"
set minval=`histo in=n${gal}/n${gal}co.line.sen0 | grep Min | awk '{print $3}'`
set clip=`calc "$msklev*$minval"`
maths exp="<n${gal}/n${gal}co.line.sen0>" mask="<n${gal}/n${gal}co.line.sen0>.lt.$clip" \
    out=n${gal}/n${gal}co.line.sen1
imblr in=n${gal}/n${gal}co.line.sen1 value=$clip out=n${gal}/n${gal}co.line.sen2

# use the masking image to mask cubes

foreach inp ( cm sen res image model flux )
rm -rf n${gal}/n${gal}co.line.${inp}msk
	maths exp="<n${gal}/n${gal}co.line.${inp}>" \
	     out=n${gal}/n${gal}co.line.${inp}msk \
	     mask="<n${gal}/n${gal}co.line.${inp}>/<n${gal}/n${gal}co.line.${inp}>*<n${gal}/n${gal}co.line.sen2>.lt.$clip" \
	     options=grow
	rm -rf n${gal}/n${gal}co.line.${inp}
	maths exp="<n${gal}/n${gal}co.line.${inp}msk>" out=n${gal}/n${gal}co.line.${inp} \
		region="mask(n${gal}/n${gal}co.line.${inp}msk)"
	rm -rf n${gal}/n${gal}co.line.${inp}msk
	minmax in=n${gal}/n${gal}co.line.${inp}
end

rm -rf n${gal}/n${gal}co.line.sen0 n${gal}/n${gal}co.line.sen1 n${gal}/n${gal}co.line.sen2
copyhd in=n${gal}/n${gal}co.line.cm out=n${gal}/n${gal}co.line.res items=bmaj,bmin,bpa,btype,bunit

rm -rf n${gal}/n${gal}co.line.con
maths exp="<n${gal}/n${gal}co.line.image>-<n${gal}/n${gal}co.line.res>" out=n${gal}/n${gal}co.line.con

end
