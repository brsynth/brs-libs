"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from unittest import TestCase
from tempfile import TemporaryDirectory
from _main    import Main
from brs_libs import inchikeyMIRIAM
from os       import path as os_path


class Test_inchikeyMIRIAM(TestCase):

    def test_inchikeyMIRIAM(self):
        inchi = inchikeyMIRIAM()
        with TemporaryDirectory() as tempd:
            output_sbml = os_path.join(tempd, 'output.sbml')
            inchi.addInChiKey(os_path.join('data','e_coli_model.sbml'), output_sbml)
            self.assertTrue(Main._check_file_hash(output_sbml, '0a26fa7dfc49480f87f79292af26fda39d10398a08f32ab4163de3908f814b61'))
