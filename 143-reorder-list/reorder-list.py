# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: find middle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse second half
        prev = None
        curr = slow
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: merge two halves
        p1 = head
        p2 = prev
        while p2.next is not None:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next