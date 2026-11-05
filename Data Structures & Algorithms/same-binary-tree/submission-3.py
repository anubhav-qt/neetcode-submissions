from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([[p, q]])
        while dq:
            curr1, curr2 = dq.popleft()
            if not curr1 and not curr2:
                continue
            elif not curr1:
                return False
            elif not curr2:
                return False

            if curr1.val != curr2.val:
                return False
            
            dq.append([curr1.left, curr2.left])
            dq.append([curr1.right, curr2.right])
        
        return True
