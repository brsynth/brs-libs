"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from _main    import Main
from tempfile import TemporaryDirectory
from argparse import Namespace as argparse_Namespace

tempdir = TemporaryDirectory()


class Module(Main):
    __test__ = False

    mod_name  = 'rplibs'
    cls_name  = 'rpCache'
    func_name = 'generate_cache'
    args      = argparse_Namespace()
    args.outdir  = tempdir.name
    args.outdir  = 'cache-3.2'

    # Not possible to compare hashes since files contain dict that have to be sorted before comparing them and then fill up the memory
    # Size of gunzipped files
    files = [
    (args.outdir+'/'+'chebi_cid.json.gz', 2786801),
    (args.outdir+'/'+'cid_name.json.gz', 55787548),
    (args.outdir+'/'+'cid_strc.json.gz', 296896910),
    (args.outdir+'/'+'cid_xref.json.gz', 88383985),
    (args.outdir+'/'+'comp_xref.json.gz', 51059),
    (args.outdir+'/'+'deprecatedCID_cid.json.gz', 423443),
    (args.outdir+'/'+'deprecatedCompID_compid.json.gz', 89832),
    (args.outdir+'/'+'deprecatedRID_rid.json.gz', 1437122),
    (args.outdir+'/'+'inchikey_cid.json.gz', 20071352),
    (args.outdir+'/'+'rr_full_reactions.json.gz', 7643885),
    (args.outdir+'/'+'rr_reactions.json.gz', 84656878)
    ]

    def _check(self):
        from brs_utils import extract_gz
        from os import remove as os_rm
        for file, size in self.files:
            outfile = extract_gz(file, tempdir.name)
            self.assertTrue(Main._check_file_size(outfile, size))
            os_rm(outfile)
