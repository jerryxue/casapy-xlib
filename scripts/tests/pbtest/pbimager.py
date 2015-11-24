os.system('rm -rf bima.pb')
os.system('rm -rf ovro.pb')

im.open('n4254_e2_bima.src.ms') #<--- just 6m x 6m Data
im.defineimage(nx=100, ny=100, cellx='1arcsec',celly='1arcsec' , stokes="I")
im.weight('natural')
im.setvp(dovp=T, usedefaultvp=False,vptable='carma_miriad.pb')
im.setoptions(ftmachine='mosaic', padding=1.0)
im.makeimage(type='pb',image='bima.pb')
exportfits('bima.pb','bima_pb.fits',overwrite=True)

im.open('n4254_e2_ovro.src.ms') #<--- just 10m x 10m Data
im.defineimage(nx=100, ny=100, cellx='1arcsec',celly='1arcsec' , stokes="I")
im.weight('natural')
im.setvp(dovp=T, usedefaultvp=False,vptable='carma_miriad.pb')
im.setoptions(ftmachine='mosaic', padding=1.0)
im.makeimage(type='pb',image='ovro.pb')
exportfits('ovro.pb','ovro_pb.fits',overwrite=True)

im.makeimage(type='psf',image='test.psf')
#im.makeimage(type='psf',image='test.psf')
