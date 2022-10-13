# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:24:41 2022

@author: carme
"""
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        length = len(nums)
        output = []
        count = 0
        for i in nums:
            for j in range(length):
                if (nums[j]-i)<0:
                    count = count + 1
            output.append(count)
            count = 0
        return output