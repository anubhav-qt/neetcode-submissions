class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            max_path = max(left + right + node.val, max_path)
            return node.val + max(left, right)
        
        dfs(root)
        return max_path
