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
        # first pass
        node_map = {None: None}
        curr = head

        while curr is not None:
            copy_curr = Node(curr.val)
            node_map[curr] = copy_curr
            curr = curr.next

        # second pass node_map[curr].next
        curr = head
        while curr is not None:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]
