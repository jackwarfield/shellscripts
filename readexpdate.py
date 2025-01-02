#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python
# Read the date-obs from header of HST image
### import statements ###
import argparse as ap
from glob import glob

from astropy.io import fits
from astropy.time import Time


### main function ###
def main(args: ap.Namespace) -> int:
    fn = args.filename
    ext = args.extension
    fl = sorted(glob(fn))

    for fn in fl:
        with fits.open(fn) as hdu:
            dateobs = hdu[ext].header['date-obs']
            decyear = Time(dateobs).decimalyear
            print(f'{fn}\t{dateobs}\t{decyear:.4f}')

    return 0


###############################################################################
###############################################################################

if __name__ == '__main__':
    s = 'Print the date of observation of an hst image.'
    parser = ap.ArgumentParser(description=s)
    _ = parser.add_argument(
        '-f',
        '--filename',
        help='Name of file (wildcards are allowed).',
        default='./*.fits',
        type=str,
    )
    _ = parser.add_argument(
        '-e',
        '--extension',
        help='Header extension in hdu (default is 0)',
        default=0,
        type=int,
    )

    args = parser.parse_args()

    raise SystemExit(main(args))
