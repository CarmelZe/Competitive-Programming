# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:19:21 2022

@author: carme
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first, last, maxLen = 0, 0, 0
        d = {}
        while last < len(fruits):
            d[fruits[last]] = last
            if len(d) >= 3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                first = min_val + 1
            maxLen = max(maxLen, last - first + 1)
            last += 1
        return maxLen
