#!/usr/bin/env python

from sys      import argv
from .rpCache import rpCache


def gen_cache(outdir):
    rpCache.generate_cache(outdir)
    exit(0)


def _cli():
    pass


if __name__ == '__main__':
    if '--gen_cache' in argv[1:]:
        gen_cache()
    else:
        _cli()
