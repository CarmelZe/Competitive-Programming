# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:31:24 2022

@author: carme
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if(nums[i]==0):
                nums.remove(nums[i])
                nums.append(0)
            else:
                continue