"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from _main     import Main
from brs_libs  import inchikeyMIRIAM


class Test_inchikeyMIRIAM(Main):
    __test__ = True

    def test_inchikeyMIRIAM(self):
        inchi = inchikeyMIRIAM()
        output_sbml = 'output.sbml'
        inchi.addInChiKey('data/e_coli_model.sbml', output_sbml)
        self.assertTrue(self._check_file_hash(output_sbml, '0a26fa7dfc49480f87f79292af26fda39d10398a08f32ab4163de3908f814b61'))
