# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:02:14 2022

@author: carme
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sol, charP, charS = [], [0]*26, [0]*26
        
        if len(p) > len(s): 
            return sol
        
        for x in p:        
            charP[ord(x)-ord('a')] += 1

        for i in range(0, len(s)-len(p)+1): 
            if i == 0: 
                for j in range(i, i+len(p)):
                    charS[ord(s[j])-ord('a')] += 1       
            else: 
                charS[ord(s[i+len(p)-1])-ord('a')] += 1
                
            if charS == charP:
                sol.append(i)
            
            charS[ord(s[i])-ord('a')] -= 1
            
        return sol