# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:32:57 2022

@author: carme
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        x = head.next
        y = self.reverseList(x)
        head.next = None
        x.next = head

        return y