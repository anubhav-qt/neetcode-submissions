class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            curr1, curr2, dummy = list1, list2, ListNode(0)
            curr = dummy

            while curr1 and curr2:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr2 = curr2.next
                
                curr = curr.next
            
            curr.next = curr1 or curr2
            return dummy.next
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i - 1])
        
        return lists[-1]
