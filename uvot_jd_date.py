import glob
from astropy.io import fits

swift_filters = ['uw2','um2','uw1','uuu','ubb','uvv']
log_file = open('date_jd.dat', 'a+')

def uvot_mag(obsID='121', filt='uw2'):
    file_structure = './'+obsID+'/uvot/image/'
    infile_name = file_structure+'sw'+obsID+filt+'_sk.img.gz'
    file1 = fits.open(infile_name)
    headers = file1[1].header
    DATE_OBS = headers['DATE-OBS']
    MET = headers['TSTART']
    JD = 51910 + float(MET)/86400.0 + 2400000.5
    Phase = JD 
    ASPCORR = headers['ASPCORR']
    return DATE_OBS, JD, Phase, ASPCORR

folders_list = list(glob.glob('000*'))
#src_list = list(glob.glob('star*'))
folders_list.sort()
#src_list.sort()

for names in folders_list:
    for filters in swift_filters:
        try:
            date_obs, JD, Phase, acorr = uvot_mag(obsID=names, filt=filters)
            string = f"{names}\t{date_obs}\t{JD:.3f}\t{Phase:.3f}\t{acorr}\n"	
            log_file.write(string)
        except:
            None

log_file.close()
