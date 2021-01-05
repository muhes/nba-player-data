# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:46:44 2021

@author: Muhes Ariyaratnam
"""

import unittest
import nba_evaluator

class TestEvaluator(unittest.TestCase):
    
    def testTotalComparisonPlayer1(self):
        result = nba_evaluator.comparePlayers('LeBron James', 'Kyrie Irving', 'total', 2019)
        self.assertEqual(result['LeBron James']['PTS'], 1698.000000)
        
    def testTotalComparisonPlayer2(self):
        result = nba_evaluator.comparePlayers('LeBron James', 'Kyrie Irving', 'total', 2019)
        self.assertEqual(result['Kyrie Irving']['STL'], 27.000000)
    
    def testAverageComparisonPlayer1(self):
        result = nba_evaluator.comparePlayers('LeBron James', 'Kyrie Irving', 'average', 2019)
        self.assertEqual(result['LeBron James']['AST'], 10.208955223880597)
        
    def testAverageComparisonPlayer2(self):
        result = nba_evaluator.comparePlayers('LeBron James', 'Kyrie Irving', 'average', 2019)
        self.assertEqual(result['Kyrie Irving']['BLK'], 0.500000)
if __name__ == '__main__':
    unittest.main()
        

