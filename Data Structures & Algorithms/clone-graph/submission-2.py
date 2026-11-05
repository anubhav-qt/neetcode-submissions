class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy_map = {}

        def clone(node: Optional["Node"]) -> Optional["Node"]:
            if node in copy_map:
                return copy_map[node]

            copy = Node(node.val)
            copy_map[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node) if node else None
