class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        
        def dfs(node: Optional[TreeNode], lower_bound=float("-inf"), upper_bound=float("inf")) -> None:
            if not node:
                return
            
            if not (lower_bound < node.val < upper_bound):
                self.valid = False
                return
            
            lb, ub = lower_bound, upper_bound
            dfs(node.left, lb, node.val)
            dfs(node.right, node.val, ub)
        
        dfs(root)
        return self.valid
