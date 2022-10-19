# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:14:54 2022

@author: carme
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        sol = []
        nums2D = {v:i for i, v in enumerate(nums2)}
        for x in nums1:
            index=nums2D[x]+1
            while index < len(nums2) and x >= nums2[index]:
                index += 1
            if index == len(nums2):
                sol.append(-1)
            else:
                sol.append(nums2[index])
        return sol