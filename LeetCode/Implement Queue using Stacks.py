# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:06:00 2022

@author: carme
"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.length += 1
        return None

    def pop(self) -> int:
        if self.stack2:
            self.length -= 1
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                self.length -= 1
                return self.stack2.pop()
            else:
                raise Exception()


    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2[-1]
            else:
                raise Exception()

    def empty(self) -> bool:
        return not bool(self.length)