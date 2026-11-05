class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        dummy = ListNode()
        head = dummy

        while curr1 or curr2 or carry:
            sum12 = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + (carry)
            digit_to_add, carry = sum12 % 10, sum12 // 10
            head.next = ListNode(digit_to_add)
            head = head.next

            curr1, curr2 = curr1.next if curr1 else None, curr2.next if curr2 else None
            
        return dummy.next
