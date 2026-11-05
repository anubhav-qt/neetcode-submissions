from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False
        
        dq =deque([[p, q]])
        while dq:
            curr1, curr2 = dq.popleft()
            if curr1.val != curr2.val:
                return False
            
            if curr1.left or curr2.left:
                if not curr1.left or not curr2.left:
                    return False
                dq.append([curr1.left, curr2.left])
            if curr1.right or curr2.right:
                if not curr1.right or not curr2.right:
                    return False
                dq.append([curr1.right, curr2.right])
        
        return True
