# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:04:10 2022

@author: carme
"""

class Solution: 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = end = head
        while end and end.next:
            start = start.next
            end = end.next.next
        return start