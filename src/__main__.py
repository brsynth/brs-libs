#!/usr/bin/env python

from sys      import argv
from brs_libs.rpCache import rpCache
from brs_libs.rpCache import add_arguments as rpCache_add_args
from argparse import ArgumentParser as argparse_ArgParser

def gen_cache(outdir):
    rpCache.generate_cache(outdir)
    exit(0)


def _cli():
    pass

def _add_arguments(parser):
    parser = rpCache_add_args(parser)
    return parser


def build_parser():
    parser = argparse_ArgParser('Add the missing cofactors to the monocomponent reactions to the SBML outputs of rpReader')
    parser = _add_arguments(parser)
    return parser

if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    if args.cache_dir:
        print("rpCache is going to be generated into " + args.cache_dir)
        gen_cache(args.cache_dir)
    else:
        _cli()
