# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:31:57 2022

@author: carme
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        for interval in sorted(intervals, key=lambda x:x[0]):
            if sol and interval[0] <= sol[-1][1]:
                sol[-1][1] = max(sol[-1][1], interval[1])
            else:
                sol.append(interval)
        return sol