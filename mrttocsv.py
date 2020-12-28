#! /usr/local/bin/python3 
# Convert machine-readable journal tables to csv files.
# alias mrttocsv="[path]/mrttocsv.py"
import sys
import glob
from astropy.io import ascii
import pandas as pd

for arg in sys.argv[1:]:
    filelist = glob.glob(arg) 
    for fname in filelist:
        df = ascii.read(arg)
        df = df.to_pandas()
        df.to_csv (arg+".csv", index=False)
