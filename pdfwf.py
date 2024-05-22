#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python3.9
# For opening an ipython session with the target table loaded in pandas
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rc('xtick', top=True, direction='in', labelsize=15)
plt.rc('ytick', right=True, direction='in', labelsize=15)
plt.rc('font', family='Arial')

scarlet = '#bb0000'
grey = '#666666'
rotorange = '#E57200'
jeffblue = '#232D4B'

fn = sys.argv[1]
df = pd.read_fwf(fn, header=None)
print(df)
