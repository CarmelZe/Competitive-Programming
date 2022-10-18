# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:11:15 2022

@author: carme
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        LeftSum = 0
        tot = sum(nums)
        for x, y in enumerate(nums):
            RightSum = tot - LeftSum - y
            if RightSum == LeftSum:
                return x
            LeftSum += y
        return -1