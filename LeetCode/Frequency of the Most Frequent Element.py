# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:05:43 2022

@author: carme
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 1

        while right < len(nums):
            k -= (nums[right] - nums[right-1]) * (right - left)

            if k < 0:
                k += nums[right] - nums[left]
                left += 1

            right += 1

        return right - left