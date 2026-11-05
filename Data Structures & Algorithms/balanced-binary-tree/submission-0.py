class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.balanced = True
        def dfs(root: Optional[TreeNode]) -> int:
            if not root or self.balanced == False:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) > 1:
                self.balanced = False
                return 0
            
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.balanced
