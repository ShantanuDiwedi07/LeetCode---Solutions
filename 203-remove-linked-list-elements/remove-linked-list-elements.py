# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev = None 
        curr = head 
        while curr :
            if curr.val == val:
                if prev is None:
                    head = curr.next  
                    curr = curr.next
                else :
                    prev.next = curr.next
                    curr = curr.next
            else :
                next_node = curr.next
                prev = curr
                curr= next_node
        return head
        