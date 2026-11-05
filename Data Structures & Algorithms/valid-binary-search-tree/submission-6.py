class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], lower_bound=float("-inf"), upper_bound=float("inf")) -> bool:
            if not node:
                return True
            
            if not (lower_bound < node.val < upper_bound):
                return False
            
            lb, ub = lower_bound, upper_bound
            return (dfs(node.left, lb, node.val) and dfs(node.right, node.val, ub))
        
        return dfs(root)
