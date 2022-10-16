# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:39:06 2022

@author: carme
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        reverse = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                while stack:
                    popp = stack.pop()
                    if popp != '(':
                        reverse.append(popp)
                    else:
                        break
                for x in reverse:
                    stack.append(x)
                reverse = []
        return ''.join(stack)