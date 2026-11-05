# iterative dfs
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack, heights = [root], {None: (0, 0)}
        while stack:
            curr_node = stack[-1]

            if curr_node.right and curr_node.right not in heights:
                stack.append(curr_node.right)
            elif curr_node.left and curr_node.left not in heights:
                stack.append(curr_node.left)
            else:
                curr_node = stack.pop()

                leftHeight, leftDiameter = heights[curr_node.left]
                rightHeight, rightDiameter = heights[curr_node.right]
                heights[curr_node] = (1 + max(rightHeight, leftHeight), max(leftDiameter, rightDiameter, leftHeight + rightHeight))

        return heights[root][1]
