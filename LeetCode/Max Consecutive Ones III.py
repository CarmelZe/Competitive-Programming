# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:10:36 2022

@author: carme
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, count, sol = 0, 0, 0, 0
        while left < len(nums) and right < len(nums):
            while right < len(nums):
                if nums[right] == 0 and count < k:
                    right += 1
                    count += 1
                elif nums[right] == 1:
                    right += 1
                else:
                    break
            
            sol = max(sol, right-left)
            if nums[left] == 0:
                count -= 1
            left += 1
        return sol