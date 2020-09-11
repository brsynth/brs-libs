"""
Created on June 17 2020

@author: Joan Hérisson
"""

from unittest import TestCase

from brs_libs import rpSBML

# Cette classe est un groupe de tests. Son nom DOIT commencer
# par 'Test' et la classe DOIT hériter de unittest.TestCase.
class Test_rpSBML(TestCase):

    def test_initEmpty(self):
        rpsbml = rpSBML('rpSBML_test')

    # def test_print_rpSBML(self):
    #     rpsbml = rpSBML('rpSBML_test')
    #     rpsbml.genericModel(
    #             'RetroPath_Pathway_test',
    #             'RP_model_test',
    #             cache.comp_xref[compid],
    #             'MNXC3',
    #             999999,
    #             0)
    #     print(rpsbml)
