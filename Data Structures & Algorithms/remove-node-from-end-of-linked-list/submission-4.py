class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = prev = head
        i = 1
        while i < n:
            p1 = p1.next
            i += 1
        
        while p1.next is not None:
            p1 = p1.next
            prev = p2
            p2 = p2.next
        
        if p2 == head:
            head = prev.next
        else:
            prev.next = p2.next

        return head
