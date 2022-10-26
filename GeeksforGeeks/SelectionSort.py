# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:43:39 2022

@author: carme
"""

 #User function Template for python3

class Solution: 
    #def select(self, arr, i):
        # code here 
    
    def selectionSort(self, arr,n):
        for x in range(n):
            min_index = x
 
            for j in range(x + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            (arr[x], arr[min_index]) = (arr[min_index], arr[x])
 