# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:43:47 2022

@author: carme
"""

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int)
        size = len(nums) - k
        ans = nums[size]
        return ans