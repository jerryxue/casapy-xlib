#!/bin/csh -f

#imcat.csh gal=3147 beam12=5.5
#imcat.csh gal=0772 beam12=5.0

### OVERRIDE ABOVE PARAMETERS IF GIVEN ON COMMAND LINE
foreach par ( $* )
   set check=`echo $par | awk -F= '{print NF}'`
   if ( "$check" >= 2 ) set $par
end

# Convert fits cubes into miriad cubes
foreach i (1 2 3 4 5)
	foreach inp (cm image model res psf flux sen)
	rm -rf n${gal}co.v$i.line.$inp
	fits in=../v${i}/n${gal}co.v$i.line.$inp.fits out=n${gal}co.v$i.line.$inp op=xyin
	end
	copyhd in=n${gal}co.v$i.line.cm out=n${gal}co.v$i.line.res items=bmaj,bmin,bpa,btype,bunit
end


# Merged cubes by imcatting four spectral chunks
foreach i (1 2 3 4 5)
	rm -rf n${gal}co.v$i.con
	maths exp="<n${gal}co.v$i.line.image>-<n${gal}co.v$i.line.res>" out=n${gal}co.v$i.line.con
    foreach inp (cm image res con)
        rm -rf n${gal}co.v$i.line.$inp.smo
        convol map=n${gal}co.v$i.line.$inp out=n${gal}co.v$i.line.$inp.smo \
            fwhm=$beam12 options=final
    end
	set sigold=`histo in=n${gal}co.v$i.line.sen region='im(1)'|grep Min|awk '{print $3}'`
	set signew=`sigest in=n${gal}co.v$i.line.image.smo|grep Est|awk '{print $4} '`
	set fac=`calc -f f8.5 "$signew/$sigold"`
	rm -rf n${gal}co.v$i.line.sen.smo
	maths exp="<n${gal}co.v$i.line.sen>*$fac" out=n${gal}co.v$i.line.sen.smo
end


foreach inp (cm image res sen con)
    rm -rf n${gal}co.line.$inp
    imcat in="n${gal}co.v?.line.$inp.smo" out=n${gal}co.line.$inp axis=3
end
foreach inp (model psf flux)
    rm -rf n${gal}co.line.$inp
    imcat in="n${gal}co.v?.line.$inp" out=n${gal}co.line.$inp axis=3
end

rm -rf n${gal}co.*.line.*.smo

foreach inp (cm image model res psf flux sen con)
	rm -rf n${gal}co.line.$inp.fits
	minmax in=n${gal}co.line.$inp
	fits in=n${gal}co.line.$inp out=n${gal}co.line.$inp.fits op=xyout
	rm -rf n${gal}co.v[1-5].line.$inp
	rm -rf n${gal}co.line.$inp
end


# foreach line (co 13co)
#     moment.csh file=$gal.$line.cmmsk noisemap=$gal.$line.cmnse start=straight \
#         nspan=3 interact=n usecube=y
#     moment.csh file=$gal.$line.cmmsk noisemap=$gal.$line.cmnse start=mask \
#         fwhm=9 interact=n usecube=y
#     moment.csh file=$gal.$line.cmmsk noisemap=$gal.$line.cmnse start=gaufit \
#         fluxclip=4 velclip=20 usecube=y
#     moment.csh file=$gal.$line.cmmsk start=cleanup
# end



