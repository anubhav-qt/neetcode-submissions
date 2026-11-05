class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        second_half = slow.next
        prev = slow.next = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        
        # merging according to the pattern
        first_half, second_half = head, prev
        while second_half:
            next1, next2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = next1

            first_half, second_half = next1, next2
