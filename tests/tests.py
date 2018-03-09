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
from Assignment.ClassAndInput import *

class Test(unittest.TestCase):
    
    
    def test_lightcounter(self):
        
        '''Testing the counter works in the class i set up'''
        
        lightcounter = 0
        result = lightTest(5)
        result.count()
        self.assert_(result.count() == 0)
        
    def test_command(self):  
        
        '''testing the various commands in the file'''
            
        a = lightTest(5)
        a.command("turn on", 1, 1,4 ,4)
        for row in a.lights:
          print(row)
          self.assert_(a.count()==16)
        print()
        print("testing turn on", a.count())
        
        print()
        
        a.command("turn off", 0, 0, 1, 1)
        for row in a.lights:
            print(row)
            self.assert_(a.count() == 15)
        print()
        print("testing turn off", a.count())
        
        print()

        a.command("switch", 0, 0, 1, 1)
        for row in a.lights:
            print(row)
            self.assert_(a.count() == 19)
        print()
        print("testing switch", a.count())
        
        print()
        
        
    def test_wrong(self):
        
        '''testing that the code can handle incorrect inputs'''
        
        a = lightTest(5)
        a.command("tworn on", 1, 1, 4 ,4)
        for row in a.lights:
          print(row)
          self.assert_(a.count()==0)
        print()
        print("testing tworn on", a.count())
        
        print()
        
        a.command("swootch on", 1, 1, 4 ,4)
        for row in a.lights:
          print(row)
          self.assert_(a.count()==0)
        print()
        print("testing tworn off", a.count())
        
        
        print()
        
        a.command("Turn on", 1, 1, 4 ,4)
        for row in a.lights:
          print(row)
          self.assert_(a.count()==0)
        print()
        print("testing Turn on", a.count())
        
        
    def test_cordinates(self):
        
        '''Testing that the code can handle negative cordinates'''
        
        a = lightTest(5)
        a.command("turn on", -1, -1, 4 ,4)
        for row in a.lights:
          print(row)
        print()
        print("testing cordinates", a.count())
        print()
        self.assert_(a.count()==25)
               
if __name__ == '__main__':
    unittest.main

    