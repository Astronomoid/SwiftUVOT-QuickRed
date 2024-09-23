import glob
import subprocess
from astropy.io import fits


swift_filters = ['uw2','um2','uw1','uuu','ubb','uvv']
log_file = open('logs_src_bkg.dat', 'a+')

def uvot_mag(obsID='000', filt='uw2', src_reg='sn.reg', bkg_reg='bkg.reg'):
    file_structure = './'+obsID+'/uvot/image/'
    infile_name = file_structure+'sw'+obsID+filt+'_sk.img.gz'
    expmap_name = file_structure+'sw'+obsID+filt+'_ex.img.gz'
    outfile_name = 'sw'+obsID+filt+'_bkgn_mag1.fits'
    
    command = (f'uvotsource image={infile_name}+1 srcreg={src_reg} '
              f'bkgreg={bkg_reg} sigma=5 zerofile=CALDB coinfile=CALDB '
               f'psffile=CALDB lssfile=CALDB syserr=NO frametime=DEFAULT '
               f'apercorr=CURVEOFGROWTH output=ALL outfile={outfile_name} '
               f'cleanup=yes  chatter=1')
               
    file1 = fits.open(infile_name)
    headers = file1[1].header
    ASPCORR = headers['ASPCORR']
    
    shell_ex = command.split()
    if ASPCORR == 'DIRECT':
        subprocess.run(shell_ex, stdout=log_file, text=True)


folders_list = list(glob.glob('000*'))
#src_list = list(glob.glob('star*'))
folders_list.sort()
#src_list.sort()

for names in folders_list:
    for filters in swift_filters:
        try:
            uvot_mag(obsID=names, filt=filters, src_reg='sn.reg', bkg_reg='bkg.reg')
        except:
            None
