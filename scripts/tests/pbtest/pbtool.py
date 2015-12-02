"""
vp.reset()
vp.setpbgauss(telescope='CARMA',
    halfwidth='1.20arcmin', maxrad='5arcmin', reffreq='100GHz',dopb=True)
bima=vp.getuserdefault('CARMA')
vp.setpbgauss(telescope='CARMA',
    halfwidth='1.98arcmin', maxrad='5arcmin', reffreq='100GHz',dopb=True)
ovro=vp.getuserdefault('CARMA')
vp.setuserdefault(bima, 'CARMA', 'BIMA')
vp.setuserdefault(ovro, 'CARMA', 'OVRO')
print "+"*70
vp.setuserdefault(-2,'CARMA','')
vp.summarizevps()
print "+"*70
os.system('rm -rf carma_miriad.pb')
vp.saveastable('carma_miriad.pb')
"""

vp.reset()
vp.setpbimage(telescope='CARMA',
    compleximage='carma_0_BIMA_0_0_180_360_0_45_90_80_100_120_GHz_gauss_VP.im',
    antnames=['CA1'])
os.system('rm -rf carma_miriad.pb')          
vp.saveastable('carma_miriad.pb')

# vp.setpbairy(telescope='CARMA', dopb=T, dishdiam='6.0m',
#              blockagediam='0.6m', maxrad='2arcmin',
#              reffreq='100GHz', dosquint=F)
# bima=vp.getuserdefault('CARMA')
# ovro=vp.setpbairy(telescope='CARMA', dopb=T, dishdiam='10.0m',
#              blockagediam='0.6m', maxrad='2arcmin',
#              reffreq='100GHz', dosquint=F)
# ovro=vp.getuserdefault('CARMA')
# vp.setuserdefault(vplistnum=0,telescope='CARMA',anttype='BIMA')
# vp.setpbgauss(telescope='CARMA', othertelescope='CARMA',
#     halfwidth='10.0arcmin', maxrad='20arcmin', reffreq='100GHz')
# vp.setuserdefault(vplistnum=1,telescope='CARMA',anttype='OVRO')
# vp.setpbgauss(telescope='CARMA', othertelescope='CARMA',
#     halfwidth='1.5arcmin', maxrad='20arcmin', reffreq='100GHz')
# vp.setuserdefault(vplistnum=-2,telescope='CARMA',anttype='FUN')
# vp.setpbgauss(telescope='OTHER', othertelescope='BONN',
#     halfwidth='1arcmin', maxrad='20arcmin', reffreq='1.4GHz')
# vp.setuserdefault(vplistnum=0,telescope='BONN',anttype='BIMA')

# print vp.getanttypes(telescope='CARMA')
# print vp.getuserdefault(telescope='CARMA',anttype='BIMA')
# print vp.getuserdefault(telescope='CARMA',anttype='OVRO')

#os.system('rm -rf test.pb')
#vp.reset()
#vp.saveastable('test.pb')
#vp.setpbantresptable(telescope='CARMA',antresppath='./AntennaResponses',dopb=True)
#vp.savetable('test.pb')





