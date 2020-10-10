"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from _main     import Main
from brs_libs  import rpCache
from brs_utils import extract_gz
from os        import remove as os_rm


class Test_File(Main):
    __test__ = True

    def test_single_attr_db(self):
        rpcache = rpCache('localhost')
        for attr,length in self.attributes:
            with self.subTest(attr=attr, length=length):
                self.assertEqual(len(getattr(rpcache, attr)), length)

    def test_single_attr_file(self):
        rpcache = rpCache('file')
        for attr,length in self.attributes:
            with self.subTest(attr=attr, length=length):
                self.assertEqual(len(getattr(rpcache, attr)), length)

    def test_generate_cache(self):
        rpCache.generate_cache(self.outdir)
        for file,size in self.files:
            outfile = extract_gz(file, self.outdir)
            self.assertTrue(Main._check_file_size(outfile, size))
            os_rm(outfile)

    outdir = 'cache-3.2'

    # Not possible to compare hashes since files contain dict that have to be sorted before comparing them and then fill up the memory
    # Size of gunzipped files
    files = [
    (outdir+'/'+'chebi_cid.json.gz', 2786801),
    (outdir+'/'+'cid_name.json.gz', 55787548),
    (outdir+'/'+'cid_strc.json.gz', 296896910),
    (outdir+'/'+'cid_xref.json.gz', 88383985),
    (outdir+'/'+'comp_xref.json.gz', 51059),
    (outdir+'/'+'deprecatedCID_cid.json.gz', 423443),
    (outdir+'/'+'deprecatedCompID_compid.json.gz', 89832),
    (outdir+'/'+'deprecatedRID_rid.json.gz', 1437122),
    (outdir+'/'+'inchikey_cid.json.gz', 20071352),
    (outdir+'/'+'rr_full_reactions.json.gz', 7643885),
    (outdir+'/'+'rr_reactions.json.gz', 84656878)
    ]

    attributes = [
    ('chebi_cid',               123835),
    ('cid_name',                691482),
    ('cid_strc',                655676),
    ('cid_xref',                691494),
    ('comp_xref',               40),
    ('deprecatedCID_cid',       16267),
    ('deprecatedCompID_compid', 4370),
    ('deprecatedRID_rid',       53413),
    ('inchikey_cid',            332146),
    ('rr_full_reactions',       41970),
    ('rr_reactions',            229862)
    ]
