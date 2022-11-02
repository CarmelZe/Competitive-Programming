# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:31:37 2022

@author: carme
"""

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
            sol = []
            x = deque()

            for num in sorted(changed):
                if x and num == x[0]:
                    x.popleft()
                else:
                    x.append(num * 2)
                    sol.append(num)

            return [] if x else sol