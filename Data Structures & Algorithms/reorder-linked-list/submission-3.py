class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding the first half of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the second half of the list
        second_half = slow.next
        slow.next = prev_node = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_node
        
        # alternately merging the first and second halves of the list
        first_half, second_half = head, prev_node
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2
