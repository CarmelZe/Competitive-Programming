# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:11:47 2022

@author: carme
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        v = defaultdict(list)
        
        for i, num in enumerate(nums):
            if num in v:
                counter += len(v[num])
            v[num].append(i)
                
        return counter
            