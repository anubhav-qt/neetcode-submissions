class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
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
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1, l2 = lists[i], lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(mergeTwoLists(l1, l2))
            lists = merged_lists
        
        return lists[0]
