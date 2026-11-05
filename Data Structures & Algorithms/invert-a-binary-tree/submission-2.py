from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        stack = [root]
        while stack:
            curr_node = stack.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
        
        return root
