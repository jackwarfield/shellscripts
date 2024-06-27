#! /usr/local/Caskroom/miniconda/base/envs/astro/bin/python3.9
# Read the exptime from header of HST image
### import statements ###
import argparse as ap
from glob import glob

from astropy.io import fits
from numpy import mean

### main function ###
def main(args: ap.Namespace) -> int:
    fn = args.filename
    ext = args.extension
    fl = sorted(glob(fn))

    et = []
    for fn in fl:
        with fits.open(fn) as hdu:
            et_i = hdu[ext].header['exptime']
            et += [et_i]
            print(f'{fn}\t{et_i}')
    print(f'\nNumber of images: {len(et)}')
    print(f'Mean Exp. Time: {mean(et):.0f} seconds')

    return 0


###############################################################################
###############################################################################

if __name__ == '__main__':
    s = 'Print the exposure time of an hst image.'
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
