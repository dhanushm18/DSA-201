class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """Initialize LRU cache with given capacity"""
        self.capacity = capacity
        self.cache = dict()  # key -> node mapping
        
        # Create dummy head and tail nodes
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove a node from the doubly linked list"""
        # Update prev and next pointers to skip this node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add_to_front(self, node: Node) -> None:
        """Add a node right after the dummy head"""
        # Connect node to head and head's next
        node.prev = self.head
        node.next = self.head.next
        
        # Update head's next and its prev to point to new node
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Get value for key and mark as most recently used"""
        if key in self.cache:
            node = self.cache[key]
            # Remove from current position
            self._remove(node)
            # Add to front (most recently used)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """Put key-value pair in cache, evicting LRU item if needed"""
        # If key exists, update its value
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add_to_front(node)
        else:
            # If at capacity, remove LRU item (tail.prev)
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            # Create new node and add to front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

# Demo
if __name__ == "__main__":
    # Test cases
    def run_test_case(operations, values):
        cache = None
        results = []
        
        for op, val in zip(operations, values):
            if op == "LRUCache":
                cache = LRUCache(val[0])
                results.append(None)
            elif op == "put":
                cache.put(val[0], val[1])
                results.append(None)
            elif op == "get":
                results.append(cache.get(val[0]))
        return results

    # Test Case 1: Basic operations
    ops1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    vals1 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    print("Test Case 1:")
    print("Operations:", ops1)
    print("Values:", vals1)
    print("Results:", run_test_case(ops1, vals1))
    print()

    # Test Case 2: Update existing key
    ops2 = ["LRUCache", "put", "put", "get", "put", "get", "get"]
    vals2 = [[2], [1, 1], [1, 2], [1], [3, 3], [1], [3]]
    print("Test Case 2:")
    print("Operations:", ops2)
    print("Values:", vals2)
    print("Results:", run_test_case(ops2, vals2))
    print()

    # Test Case 3: Capacity 1
    ops3 = ["LRUCache", "put", "put", "get", "put", "get"]
    vals3 = [[1], [2, 1], [3, 2], [2], [4, 4], [1]]
    print("Test Case 3:")
    print("Operations:", ops3)
    print("Values:", vals3)
    print("Results:", run_test_case(ops3, vals3))
