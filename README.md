# SwiftUVOT-QuickRed
Script to quickly read through various downloaded obsID for Swift/UVOT and perform aperture photometry on Level2 files.
1. bkg.reg --> sample background region file to be created from ds9 in fk5 coordinates
2. date_jd.dat --> Output of uvot_jd_date.py to estimated date and jd for the given observation ID folders
3. logs_src_bkg.dat --> A log of terminal output while running the UVOT tasks
4. sn.reg --> Sample source region file to be created from ds9 in fk5 coordinates on which photometry is required
5. uvot_jd_date.py --> Script to get date and JD from files for verification
6. uvot_mag_src.py --> Script to perform photometry on UVOT images using sn.reg and bkg.reg files
