class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyMap = {}
        self.LRU, self.MRU = Node(0, 0), Node(0, 0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del node
    
    def insert(self, node):
        prev, nxt = self.MRU.prev, self.MRU
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.remove(self.keyMap[key])
            self.insert(self.keyMap[key])
            return self.keyMap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            self.remove(self.keyMap[key])
        self.keyMap[key] = Node(key, value)
        self.insert(self.keyMap[key])

        if len(self.keyMap) > self.cap:
            lru = self.LRU.next
            self.remove(lru)
            del self.keyMap[lru.key]

        
