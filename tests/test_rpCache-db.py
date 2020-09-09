"""
Created on Jul 15 2020

@author: Joan Hérisson
"""

from module import Module
from rplibs import rpCache


class Test_DB(Module):
    __test__ = True

    obj = rpCache('localhost')
