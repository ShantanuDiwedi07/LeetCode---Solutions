# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # Step 1: find the middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now at the start of the second half

        # Step 2: reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # prev is now the head of the reversed second half

        # Step 3: compare first half and reversed second half
        left, right = head, prev
        while right:  # right is shorter or equal, safe to stop on it
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True