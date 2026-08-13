class Node:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.lru = Node(key=None, value=None)  # dummy
        self.tail = self.lru
        self.length = 0
        self.capacity = capacity
        self.hashmap = {}
    
    def add_node(self, node):
        # Check if this is the tail and if it is, shift the tail pointer back
        if self.tail == node and self.length > 1:
            self.tail = node.prev

        node.next = self.lru.next
        if self.lru.next:  # if next is not None
            self.lru.next.prev = node
        self.lru.next = node
        node.prev = self.lru
    
    def remove_node(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
    
    def move_to_front(self, node):
        self.remove_node(node)
        self.add_node(node)

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # remove the node
            node = self.hashmap[key]
            self.move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # does the key exist?
        if key in self.hashmap:
            # update the key
            node = self.hashmap[key]
            node.value = value
            self.move_to_front(node)
            return
        
        if self.length == self.capacity:
            # remove the LRU node
            new_tail = self.tail.prev
            self.remove_node(self.tail)
            del self.hashmap[self.tail.key]
            self.tail = new_tail
        else:
            self.length += 1
            
        # Add the new key
        node = Node(key=key, value=value)
        self.hashmap[key] = node
        self.add_node(node)

        if self.length == 1:  # If this is the first node added
            self.tail = node
        
        

        
