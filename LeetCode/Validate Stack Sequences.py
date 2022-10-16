# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:53:46 2022

@author: carme
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        intArr = []
        i = 0

        for num in pushed:
            intArr.append(num)
            while intArr and intArr[-1] == popped[i]:
                intArr.pop()
                i += 1

        return not intArr 
