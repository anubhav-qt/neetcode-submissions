# how to keep track of least recently used:
# hash map = {key: (value, node)}
# nodes of a doubly linked list, where the node in the start is the least recently used and in the end is the most recently used
# when using put to update the value of an existing key, the value and node both will be updated, the node will go to the start and the prev and next nodes will connect to each other

class DoubleNode():
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: DoubleNode(key, value)
        self.left, self.right = DoubleNode(0, 0), DoubleNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DoubleNode(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
