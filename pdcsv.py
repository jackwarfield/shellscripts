#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python3.9
# For opening an ipython session with the target table loaded in pandas
import sys

import numpy as np
import pandas as pd

fn = sys.argv[1]
if '.pkl' in fn:
    df = pd.read_picle(fn)
else:
    df = pd.read_csv(fn, low_memory=False)
print(df)
