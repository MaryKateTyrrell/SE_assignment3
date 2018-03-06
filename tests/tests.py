    #!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Mary Kate Tyrrell"
__copyright__ = "Mary Kate Tyrrell"
__license__ = "mit"

import sys
sys.path.append('.')

import pytest
import unittest
import pandas as pd
import numpy as np
from ClassAndInput import *

class Test(unittest.TestCase):
    
    '''def test_lightcounter(self):
        
        Testing the counter works in the class i set up 
        
        lightcounter = 0
        result = settingUpClass.lightTest(5)
        result.lightcounter
        self.assert_(result.lightcounter == 0)'''
        
        
a = lightTest(5)
for row in a.lights:
    print(row)
    c = "turn on"
a.command("turn on", 1, 1,4 ,4)
print(a.count())

''''a.command("turn off", 0, 0, 1, 1)
print(a.count())

a.command("switch", 0, 0, 1, 1)
print(a.count())'''


for row in a.lights:
    print(row)
         
if __name__ == '__main__':
    unittest.main

    