# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:56:09 2022

@author: carme
"""

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        first = [0] * (len(nums) + 1)
        for x in range(1, len(first)):
            first[x] = first[x-1] + nums[x-1]
        
        firstLenMax, secondLenMax, sol = first[firstLen], first[secondLen], first[firstLen+secondLen]
        for y in range(firstLen + secondLen + 1, len(first)):
            firstLenMax = max(firstLenMax, first[y-secondLen] - first[y-secondLen-firstLen])
            secondLenMax = max(secondLenMax, first[y-firstLen] - first[y-firstLen-secondLen])
            sol = max(sol, firstLenMax + first[y] - first[y-secondLen], secondLenMax + first[y] - first[y-firstLen])
        return sol