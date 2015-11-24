#listobs('n4254_e2.src.ms',antenna='0&&1')
#listobs('n4254_e2.src.ms',antenna='10&&11',field='10')
##
#    This will create three beams for CARMA data (BIMA/OVRO/CARMA)
##
os.system("rm -rf n4254_e2_bima*")
mstransform('n4254_e2.src.ms',outputvis='n4254_e2_bima.src.ms',
    datacolumn="data",spw='0:10',
    antenna='10&&11',field='10')
xu.carmapb('n4254_e2_bima.src.ms')    
clean('n4254_e2_bima.src.ms',
    imagename='n4254_e2_bima',
    restfreq='115.2712GHz',
    mode='channel',
    imagermode='mosaic',
    ftmachine='mosaic',
    niter=0,imsize=800,cell='0.25arcsec',minpb=0.01)
exportfits(imagename='n4254_e2_bima.flux',fitsimage='n4254_e2_bima.flux.fits')

os.system("rm -rf n4254_e2_ovro*")
mstransform('n4254_e2.src.ms',outputvis='n4254_e2_ovro.src.ms',
    datacolumn="data",spw='0:10',
    antenna='3&&4',field='10')
xu.carmapb('n4254_e2_ovro.src.ms')    
clean('n4254_e2_ovro.src.ms',
    imagename='n4254_e2_ovro',
    restfreq='115.2712GHz',
    mode='channel',
    imagermode='mosaic',
    ftmachine='mosaic',
    niter=0,imsize=800,cell='0.25arcsec',minpb=0.01)
exportfits(imagename='n4254_e2_ovro.flux',fitsimage='n4254_e2_ovro.flux.fits',overwrite=True)
 
os.system("rm -rf n4254_e2_carma*")
mstransform('n4254_e2.src.ms',outputvis='n4254_e2_carma.src.ms',
    datacolumn="data",spw='0:10',
    antenna='2&&10',field='10')
xu.carmapb('n4254_e2_carma.src.ms')    
clean('n4254_e2_carma.src.ms',
    imagename='n4254_e2_carma',
    restfreq='115.2712GHz',
    mode='channel',
    imagermode='mosaic',
    ftmachine='mosaic',
    niter=0,imsize=800,cell='0.25arcsec',minpb=0.01)
exportfits(imagename='n4254_e2_carma.flux',fitsimage='n4254_e2_carma.flux.fits',overwrite=True)
#exportfits(imagename='n4254_e2_carma.flux.pbcoverage',fitsimage='n4254_e2_carma.flux.pbcoverage.fits')



