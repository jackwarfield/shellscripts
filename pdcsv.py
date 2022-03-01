#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python3.9
# For opening an ipython session with the target table loaded in pandas

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], low_memory=False)
print(df)
