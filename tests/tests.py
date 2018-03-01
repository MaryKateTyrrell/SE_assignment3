#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Mary Kate Tyrrell"
__copyright__ = "Mary Kate Tyrrell"
__license__ = "mit"

import pytest
import unittest
import pandas as pd
import numpy as np
import settingUpClass

class Test(unittest.TestCase):
    
    def test_lightcounter(self):
        
        '''Testing the counter works in the class i set up '''
        
        lightcounter = 0
        result = settingUpClass.lightTest(5)
        result.lightcounter
        self.assert_(result.lightcounter == 0)
        
        
    
    


    