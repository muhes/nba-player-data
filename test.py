# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:46:44 2021

@author: Muhes Ariyaratnam
"""

import unittest
import nba_evaluator

class TestEvaluator(unittest.TestCase):
    
    def testTotalComparison(self):
        result = nba_evaluator.comparePlayers('LeBron James', 'Kyrie Irving', 'total', 2019)
        self.assertEqual(result['LeBron James']['PTS'], 1698.000000)
        
if __name__ == '__main__':
    unittest.main()
        

