from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            dq = deque([[p, q]])
            while dq:
                curr1, curr2 = dq.popleft()
                if (curr1 and not curr2) or (curr2 and not curr1):
                    return False
                
                if curr1 and curr2:
                    if curr1.val != curr2.val:
                        return False
                    dq.append([curr1.left, curr2.left])
                    dq.append([curr1.right, curr2.right])
            
            return True
        
        dq = deque([root])
        while dq:
            curr_node = dq.popleft()
            if curr_node.val == subRoot.val and isSameTree(curr_node, subRoot):
                return True
            
            if curr_node.left:
                dq.append(curr_node.left)
            if curr_node.right:
                dq.append(curr_node.right)
        
        return False
