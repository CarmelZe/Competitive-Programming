# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:21:50 2022

@author: carme
"""

class Solution:
    def sortSentence(self, s: str) -> str:
         splittedWord = s.split()
         word={}
         sol=''
         for i in splittedWord:
            word[i[-1]]= i[:-1]
         for i in sorted(word):
            sol=sol+''.join(word[i])+' '
         sol=sol[:-1]
         return sol