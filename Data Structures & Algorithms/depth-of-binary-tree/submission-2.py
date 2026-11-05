class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using dfs iterative
        if not root:
            return 0
        
        max_depth, stack = 0, [[root, 1]]
        while stack:
            curr_node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if curr_node.left:
                stack.append([curr_node.left, depth + 1])
            if curr_node.right:
                stack.append([curr_node.right, depth + 1])

        return max_depth
