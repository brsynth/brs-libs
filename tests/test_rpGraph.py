"""
Created on June 17 2020

@author: Joan Hérisson
"""

from _main    import Main
from unittest import TestCase
from brs_libs import rpSBML
from brs_libs import rpGraph
from os       import path     as os_path
from json     import load     as json_load
from tempfile import NamedTemporaryFile
from io       import open     as io_open


class Test_rpGraph(TestCase):

    # To avoid limit in dictionaries comparison
    maxDiff = None

    def setUp(self):
        # load a rpSBML file
        self.rpsbml       = rpSBML(os_path.join(os_path.dirname(__file__),
                                                'data', 'rpsbml.xml')     )
		self.rpgraph = rpGraph(self.rpsbml)

    def test_onlyConsumedSpecies(self):
        self.assertCountEqual(self.rpgraph.onlyConsumedSpecies(True, True), ['MNXM89557__64__MNXC3', 'MNXM1__64__MNXC3', 'MNXM6__64__MNXC3', 'MNXM3__64__MNXC3'])
        self.assertCountEqual(self.rpgraph.onlyConsumedSpecies(True, False), ['MNXM89557__64__MNXC3', 'MNXM1__64__MNXC3'])

    #onlyProducedSpecies
    def test_onlyProducedSpecies(self):
        self.assertCountEqual(self.rpgraph.onlyProducedSpecies(True, True), ['TARGET_0000000001__64__MNXC3', 'MNXM9__64__MNXC3', 'MNXM5__64__MNXC3', 'MNXM7__64__MNXC3', 'MNXM20__64__MNXC3', 'MNXM13__64__MNXC3'])
        lf.assertCountEqual(self.rpgraph.onlyProducedSpecies(True, False), ['TARGET_0000000001__64__MNXC3'])
