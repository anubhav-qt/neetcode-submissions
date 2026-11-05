class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = prev_node = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_node
        
        first_half, second_half = head, prev_node
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1

            first_half, second_half = temp1, temp2
