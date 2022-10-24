# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:28:50 2022

@author: carme
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return(self.fib(n-1) + self.fib(n-2))