# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:39:47 2022

@author: carme
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        i = 0
        j = len(height)-1
        while(i<j):
            if height[i] <= height[j]:
                result = height[i] * (j-i)
                i += 1
            else:
                result = height[j] * (j-i)
                j -= 1
            if result > maxWater: maxWater = result
        return maxWater
                
