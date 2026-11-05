# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_fast = head
        current_slow = head
        i = 0

        while current_fast:
            current_fast = current_fast.next
            
            if i % 2:
                current_slow = current_slow.next

            if current_fast == current_slow:
                return True

            i += 1
        
        return False
