class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_node, stack, i = root, [], 0

        while (curr_node or stack) and (i < k):
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                res = curr_node.val
                i += 1
                curr_node = curr_node.right
        
        return res
