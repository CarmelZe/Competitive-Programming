# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:12:17 2022

@author: carme
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        y, x = 1, 0
        if n < 0:
            return False
        while y <= n:
            if y == n:
                return True
            y = 4 ** x
            x += 1