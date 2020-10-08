"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

# from module_rpCache import Module
from _main     import Main
from brs_libs  import rpCache
from tempfile  import TemporaryDirectory
from brs_utils import extract_gz
from os        import remove as os_rm


class Test_File(Main):
    __test__ = True

    def test_generate_cache(self):
        outdir = TemporaryDirectory().name
        outdir = 'cache-3.2'
        # Not possible to compare hashes since files contain dict that have to be sorted before comparing them and then fill up the memory
        # Size of gunzipped files
        files = [
        (outdir+'/'+'chebi_cid.json.gz',               2786801),
        (outdir+'/'+'cid_name.json.gz',                55787548),
        (outdir+'/'+'cid_strc.json.gz',                296896910),
        (outdir+'/'+'cid_xref.json.gz',                88383985),
        (outdir+'/'+'comp_xref.json.gz',               51059),
        (outdir+'/'+'deprecatedCID_cid.json.gz',       423443),
        (outdir+'/'+'deprecatedCompID_compid.json.gz', 89832),
        (outdir+'/'+'deprecatedRID_rid.json.gz',       1437122),
        (outdir+'/'+'inchikey_cid.json.gz',            20071352),
        (outdir+'/'+'rr_full_reactions.json.gz',       7643885),
        (outdir+'/'+'rr_reactions.json.gz',            84656878)
        ]
        for file, size in self.files:
            outfile = extract_gz(file, outdir)
            self.assertTrue(Main._check_file_size(outfile, size))
            os_rm(outfile)

    def check(self, attr, value_equal):
        for sm in ['file', 'localhost']:
            with self.subTest(sm=sm):
                rpcache = rpCache(sm, [attr])
                rpcache._check_or_load_cache_in_memory()
                self.assertEqual(len(getattr(rpcache, attr)), value_equal)

    def test_deprecatedCID_cid(self):
        attr = 'deprecatedCID_cid'
        self.check(attr, 16267)

    def test_deprecatedRID_rid(self):
        attr = 'deprecatedRID_rid'
        self.check(attr, 53413)

    def test_cid_strc(self):
        attr = 'cid_strc'
        self.check(attr, 655676)

    def test_cid_name(self):
        attr = 'cid_name'
        self.check(attr, 691482)

    def test_cid_xref(self):
        attr = 'cid_xref'
        self.check(attr, 691494)

    def test_chebi_cid(self):
        attr = 'chebi_cid'
        self.check(attr, 123835)

    def test_rr_reactions(self):
        attr = 'rr_reactions'
        self.check(attr, 229862)

    def test_inchikey_cid(self):
        attr = 'inchikey_cid'
        self.check(attr, 332146)

    def test_comp_xref(self):
        attr = 'comp_xref'
        self.check(attr, 40)

    def test_deprecatedCompID_compid(self):
        attr = 'deprecatedCompID_compid'
        self.check(attr, 4370)

    def test_rr_full_reactions(self):
        attr = 'rr_full_reactions'
        self.check(attr, 41970)
