class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr_node = root
        while curr_node:
            if p.val > curr_node.val and q.val > curr_node.val:
                curr_node = curr_node.right
            elif p.val < curr_node.val and q.val < curr_node.val:
                curr_node = curr_node.left
            else:
                return curr_node
