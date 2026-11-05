"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# first pass: store original node as key, copy its val as the val of the newly created node with next and random as null
# second pass: go through fill the next and random values in each node

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # first pass
        node_map = {}
        curr = head

        while curr is not None:
            copy_curr = Node(curr.val)
            node_map[curr] = copy_curr
            curr = curr.next

        # second pass
        for node, copy in node_map.items():
            copy.next = node_map[node.next] if node.next is not None else None
            copy.random = node_map[node.random] if node.random is not None else None
        
        return node_map[head]
