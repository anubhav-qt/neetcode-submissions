class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root: TreeNode, max_parent=-101) -> None:
            if not root:
                return None

            if root.val >= max_parent:
                self.res += 1
                max_parent = root.val
            
            parent = max_parent
            dfs(root.left, parent)
            dfs(root.right, parent)
        
        dfs(root)
        return self.res
