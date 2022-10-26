# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:49:02 2022

@author: carme
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left= 0 
        temp = 0 
        right = len(nums)-1 
        
        while temp <= right:
            if nums[temp] == 0:
                nums[left],nums[temp]= nums[temp],nums[left] 
                left += 1 
                temp += 1  
                
            elif nums[temp] == 2:
                nums[temp],nums[right]  = nums[right],nums[temp] 
                right -= 1 
                
            else:
                temp += 1 