from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        dq = deque([root])
        while dq:
            curr_node = dq.popleft()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            if curr_node.right:
                dq.append(curr_node.right)
            if curr_node.left:
                dq.append(curr_node.left)
        
        return root
