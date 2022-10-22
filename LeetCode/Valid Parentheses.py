# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:15:11 2022

@author: carme
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        checkSigns = {'(' : ')', '[' : ']', '{' : '}'}
        newStack = []
        for i in s:
            if i in checkSigns.keys():
                newStack.append(i)
            else:
                if newStack == []:
                    return False
                a = newStack.pop()
                if i!= checkSigns[a]:
                    return False
        return newStack == []
    print(isValid(isValid, "("))