class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = None
        prev_node = None

        while second_half:
            next_node = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_node
        
        second_half = prev_node
        first_half = head

        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2
