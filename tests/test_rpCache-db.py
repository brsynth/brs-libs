"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from module_rpCache import Module
from brs_libs       import rpCache


class Test_DB(Module):
    __test__ = True

    obj = rpCache('localhost')
