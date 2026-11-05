from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # using bfs
        dq, max_depth = deque([root]), 0
        while dq:
            for _ in range(len(dq)):
                curr_node = dq.popleft()

                if curr_node.left:
                    dq.append(curr_node.left)
                if curr_node.right:
                    dq.append(curr_node.right)
            
            max_depth += 1

        return max_depth
