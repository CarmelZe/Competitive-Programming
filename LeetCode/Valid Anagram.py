# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:11:41 2022

@author: carme
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)
    
       
    
        