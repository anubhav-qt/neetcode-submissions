# recursive dfs
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # function to find the max height at a node and also update the the max_diameter in each iteration
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right) # diameter check

            return 1 + max(left, right) # 1 + the height of the deeper subtree

        dfs(root)
        return self.res
