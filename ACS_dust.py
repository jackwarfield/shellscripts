#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python3.9
# Query the SFD dustmap via mwdust at a given ra,dec for all ACS filters

### import statements ###
import argparse as ap
import os
import sys

import mwdust
from astropy import units as u
from astropy.coordinates import SkyCoord

class HiddenPrints:
  def __enter__(self):
    self._original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
  def __exit__(self, exc_type, exc_val, exc_tb):
    sys.stdout.close()
    sys.stdout = self._original_stdout

### main function ###
def main(args: ap.Namespace) -> int:
  r,d = args.ra,args.dec

  if args.units == "hms":
    c = SkyCoord(ra=r, dec=d, unit=(u.hourangle, u.deg))
    l = c.galactic.l.value
    b = c.galactic.b.value
  elif (args.units == "deg") or (args.units == "degrees"):
    c = SkyCoord(ra=r, dec=d, unit=(u.deg, u.deg))
    l = c.galactic.l.value
    b = c.galactic.b.value

  filts = ['ACS clear',
    'ACS F435W',
    'ACS F475W',
    'ACS F550M',
    'ACS F555W',
    'ACS F606W',
    'ACS F625W',
    'ACS F775W',
    'ACS F814W',
    'ACS F850LP',
    ]
  
  print(f"Coefficients for\n(ra,dec)=({r},{d})\n(l,b)=({l},{b})\n")
  for f in filts:
    with HiddenPrints():
      coeff = mwdust.SFD(filter=f)(l,b,1)
    print(f"{f:10} {coeff[0]}")

  return 0

###############################################################################
###############################################################################

if __name__ == "__main__":
  s = "Gives ACS A_(filter) coefficients at a given RA,Dec from SFD1998 map."
  parser = ap.ArgumentParser(description=s)
  _= parser.add_argument(
      "-r",
      "--ra",
      help="Right Ascension of Object",
      default="",
      type=str,
      )
  _= parser.add_argument(
      "-d",
      "--dec",
      help="Declination of Object",
      default="",
      type=str,
      )
  _= parser.add_argument(
      "-u",
      "--units",
      help="hms (default) or degrees",
      default="hms",
      type=str,
      )

  args = parser.parse_args()

  raise SystemExit(main(args))
