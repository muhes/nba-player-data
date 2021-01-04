# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:46:44 2021

@author: Muhes Ariyaratnam
"""

import unittest
import nba-evaluator

class TestEvaluator(unittest.TestCase):
    
    def testGetPlayerId(self):
        result = getPlayerId('LeBron James')
        self.assertEqual(result, 2544)
        
if __name__ == '__main__':
    unittest.main()
        

