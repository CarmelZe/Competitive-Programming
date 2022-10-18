# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:17:24 2022

@author: carme
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, tot = 0, 0
        temp = {0:1}
        for x in nums:
            tot += x
            if temp.get(tot-k):
                count += temp[tot-k]              
            if temp.get(tot):
                temp[tot] += 1
            else:
                temp[tot] = 1
        return count