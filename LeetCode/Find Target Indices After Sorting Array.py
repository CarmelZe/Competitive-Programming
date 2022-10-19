# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:03:30 2022

@author: carme
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        lessThan = sum(x < target for x in nums)
        return [i for i in range(lessThan, lessThan + count)]