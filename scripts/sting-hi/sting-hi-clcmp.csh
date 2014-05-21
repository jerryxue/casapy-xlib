#!/bin/csh -f 
#/Volumes/data3/ruixue1/hi/msc-clcmp


goto n4254

n4254:
fits in=../msc-ref/ngc4254.mom0.fits out=n4254hi.ref.mmom0 op=xyin
fits in=../msc-products/himom/n4254hi.line.mmom0.fits out=n4254hi.line.mmom0 op=xyin

puthd in=n4254hi.ref.mmom0/bmaj value=37.70,arcsec
puthd in=n4254hi.ref.mmom0/bmin value=32.95,arcsec
puthd in=n4254hi.ref.mmom0/bpa value=0.0
puthd in=n4254hi.ref.mmom0/bunit value="JY/BEAM.KM/S"

matcher.csh tin=n4254hi.ref.mmom0 im="n4254hi.line.mmom0" \
			bsize="same" axes="1,2"
goto n4654

n4654:
fits in=../msc-ref/ngc4654.mom0.fits out=n4654hi.ref.mmom0 op=xyin
fits in=../msc-products/himom/n4654hi.line.mmom0.fits out=n4654hi.line.mmom0 op=xyin

puthd in=n4654hi.ref.mmom0/bmaj value=16.14,arcsec
puthd in=n4654hi.ref.mmom0/bmin value=15.51,arcsec
puthd in=n4654hi.ref.mmom0/bpa value=0.0
puthd in=n4654hi.ref.mmom0/bunit value="JY/BEAM.KM/S"

matcher.csh tin=n4654hi.ref.mmom0 im="n4654hi.line.mmom0" \
			bsize="same" axes="1,2"
goto n2976


n2976:
fits in=../msc-ref/NGC_2976_NA_MOM0_THINGS.FITS out=tmp op=xyin
maths exp="<tmp>/1000.0" out=n2976hi.ref.mmom0
rm -rf tmp

fits in=../msc-products/himom/n2976hi.line.mmom0.fits out=n2976hi.line.mmom0 op=xyin

puthd in=n2976hi.ref.mmom0/bmaj value=7.407,arcsec
puthd in=n2976hi.ref.mmom0/bmin value=6.42,arcsec
puthd in=n2976hi.ref.mmom0/bpa value=72
puthd in=n2976hi.ref.mmom0/bunit value="JY/BEAM.KM/S"

matcher.csh tin=n2976hi.ref.mmom0 im="n2976hi.line.mmom0" \
			bsize="same" axes="1,2"
goto end


end:
