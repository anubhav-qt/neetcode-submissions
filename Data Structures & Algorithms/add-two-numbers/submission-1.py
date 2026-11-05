# a loop until both curr are not null
# add the vals and the carry number (initially 0)
# if carry then add the carry for the next iteration
# once one list reached null, keep adding the number and carry till the next list also reaches none

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry = 0
        dummy = ListNode()
        head = dummy

        while curr1 and curr2:
            sum12 = curr1.val + curr2.val + carry
            digit_to_add, carry = sum12 % 10, sum12 // 10
            head.next = ListNode(digit_to_add)
            head = head.next

            curr1, curr2 = curr1.next, curr2.next
        
        if curr1:
            while curr1:
                sum1 = curr1.val + carry
                digit_to_add, carry = sum1 % 10, sum1 // 10
                head.next = ListNode(digit_to_add)
                head = head.next
                curr1 = curr1.next
            if carry > 0:
                head.next = ListNode(carry)
            
            return dummy.next
        else:
            while curr2:
                sum2 = curr2.val + carry
                digit_to_add, carry = sum2 % 10, sum2 // 10
                head.next = ListNode(digit_to_add)
                head = head.next
                curr2 = curr2.next
            if carry > 0:
                head.next = ListNode(carry)
            
            return dummy.next
