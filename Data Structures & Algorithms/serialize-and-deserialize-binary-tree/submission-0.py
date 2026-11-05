class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                res.append('N#')
                return

            res.append(str(root.val) + '#')
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ''.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split('#')
        self.i = 0

        return self.build_tree(values)
    
    def build_tree(self, values: List[str]) -> Optional[TreeNode]:
        value = values[self.i]
        self.i += 1

        if value == "N":
            return None
        
        node = TreeNode(int(value))
        node.left = self.build_tree(values)
        node.right = self.build_tree(values)

        return node
