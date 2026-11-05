# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prev_node = None
        temp = head
        next_node = temp.next

        while temp != None:
            temp.next = prev_node
            prev_node = temp
            temp = next_node
            if temp != None:
                next_node = temp.next

        return prev_node
