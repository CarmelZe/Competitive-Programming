# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = {}
        num = ListNode(0)
        num.next = head

        while head != None:
            counter[head.val] = counter.get(head.val, 0) + 1
            head = head.next
        
        head = num.next
        prevNum = num

        while head != None:
            if counter[head.val] > 1:
                prevNum.next = head.next
            else:
                prevNum = head
            head = head.next

        return num.next