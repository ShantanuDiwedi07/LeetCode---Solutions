class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while fast is not None and fast.next is not None:
            if fast.val == fast.next.val:
                while fast.next is not None and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        return dummy.next
        