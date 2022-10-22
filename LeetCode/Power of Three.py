# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 18:38:06 2022

@author: carme
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        y,x = 1,0
        while y <= n:
            if y == n:
                return True
            x += 1
            y = 3 ** x
        return False
            