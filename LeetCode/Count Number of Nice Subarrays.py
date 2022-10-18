# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:57:29 2022

@author: carme
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indices = [i for i in range(len(nums)) if nums[i] % 2 == 1]
        if k > len(odd_indices):
            return 0
        count = 0
        for end_index in range(k-1, len(odd_indices)):
            start_index = end_index - k + 1
            left = odd_indices[start_index] - odd_indices[start_index-1] if start_index-1 >= 0 else odd_indices[start_index] + 1
            right = odd_indices[end_index+1] - odd_indices[end_index] if end_index + 1 < len(odd_indices) else len(nums) - odd_indices[end_index]
            count += left * right
        return count