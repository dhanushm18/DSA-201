import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        # Define less than for ListNode to be used in heapq
        return self.val < other.val

class Solution:
    def createList(self, arr: List[int]) -> Optional[ListNode]:
        """Helper method to create linked list from array"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def printList(self, head: Optional[ListNode]) -> List[int]:
        """Helper method to convert linked list to array for printing"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge k sorted linked lists using min heap"""
        # Remove empty lists
        lists = [lst for lst in lists if lst]
        if not lists:
            return None
            
        # Initialize min heap with first node from each list
        # Store (value, list_index) pairs to handle duplicate values
        heap = []
        for i, node in enumerate(lists):
            heap.append((node.val, i, node))
        heapq.heapify(heap)
        
        # Create dummy head for result list
        dummy = ListNode(0)
        current = dummy
        
        # Keep track of next nodes for each list
        next_nodes = lists[:]
        
        # Process nodes until heap is empty
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add node to result list
            current.next = node
            current = current.next
            
            # If node has next, add it to heap
            if node.next:
                next_nodes[list_idx] = node.next
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        # Test case 1: Example from problem
        [[1,4,5], [1,3,4], [2,6]],
        
        # Test case 2: Empty lists
        [],
        
        # Test case 3: Single empty list
        [[]],
        
        # Test case 4: Multiple empty lists
        [[], [], []],
        
        # Test case 5: Single list
        [[1,2,3]],
        
        # Test case 6: Lists with duplicates
        [[1,1,1], [1,1,1]],
        
        # Test case 7: Mixed length lists
        [[1], [2,3], [4,5,6]]
    ]
    
    for i, lists_arr in enumerate(test_cases):
        # Convert arrays to linked lists
        lists = [sol.createList(arr) for arr in lists_arr] if lists_arr else []
        
        # Merge lists
        result = sol.mergeKLists(lists)
        
        print(f"Test case {i + 1}:")
        print(f"Input: {lists_arr}")
        print(f"Output: {sol.printList(result)}")
        print()
