# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:49:15 2022

@author: carme
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
 
        if lenNums == 0 or nums is None:
            return nums
        sol = [1] * lenNums 
 
        for i in range(1, lenNums):
            sol[i] = nums[i - 1] * sol[i - 1]
        right = 1
    
        for i in range(lenNums - 1, -1, -1):
            sol[i] *= right
            right *= nums[i]
    
        return sol