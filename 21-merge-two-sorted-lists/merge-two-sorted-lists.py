class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 is not None else list2
        
        return dummy.next     
