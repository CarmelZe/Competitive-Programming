# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:03:40 2022

@author: carme
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = len(s)
        newList = []
        sol = 0
        for x in range(count):
            for y in range(x, count):
                if(s[y] in newList):
                    newList.clear()
                    break
                else:
                    newList.append(s[y])
                    if(sol<y-x+1):
                        sol = y - x + 1
        return sol