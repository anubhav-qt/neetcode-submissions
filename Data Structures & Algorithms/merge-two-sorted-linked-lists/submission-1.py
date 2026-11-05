# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = list1, list2
        
        if not list1 and not list2:
            return None
        elif not list1:
            head = temp2
            temp2 = temp2.next
        elif not list2:
            head = temp1
            temp1 = temp1.next
        else:
            if temp1.val >= temp2.val:
                head = temp2
                temp2 = temp2.next
            else:
                head = temp1
                temp1 = temp1.next
        
        temp = head

        # iterating over the entire list1 till its empty
        while temp1:
            if temp2:
                if temp1.val >= temp2.val:
                    temp.next = temp2
                    temp = temp.next
                    temp2 = temp2.next
                else:
                    temp.next = temp1
                    temp = temp.next
                    temp1 = temp1.next
            else:
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
        
        while temp2:
            temp.next = temp2
            temp = temp.next
            temp2 = temp2.next
        
        temp.next = None

        return head
