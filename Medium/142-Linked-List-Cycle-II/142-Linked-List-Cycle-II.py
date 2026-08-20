class Solution(object):
    def detectCycle(self, head):
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None : 
            slow = slow.next 
            fast = fast.next.next 
            if slow is fast : 
                pointer = head 
                while slow is not pointer :
                    slow= slow.next 
                    pointer = pointer.next 
                return pointer 
        return None 
        
