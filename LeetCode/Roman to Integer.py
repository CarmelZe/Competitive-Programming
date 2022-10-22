# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:11:38 2022

@author: carme
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        
        lengthS = len(s)
        count = lengthS - 1
        sol = 0
        
        while count >= 0:
            if count<lengthS-1 and romanDict[s[count]] < romanDict[s[count+1]]:
                sol -= romanDict[s[count]]
            else:
                sol += romanDict[s[count]]
            count-=1
        return sol
    romanToInt(romanToInt,"IV")
        