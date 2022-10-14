# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:50:42 2022

@author: carme
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
             if x == "+":
                 stack.append(stack.pop() + stack.pop())
             elif x == "-":
                 num1, num2 = stack.pop(), stack.pop()
                 stack.append(num2 - num1)
             elif x == "*":
                 stack.append(stack.pop() * stack.pop())
             elif x == "/":
                 num1, num2 = stack.pop(), stack.pop()
                 stack.append(int(num2 / num1))
             else:
                 stack.append(int(x))
        return stack[0]