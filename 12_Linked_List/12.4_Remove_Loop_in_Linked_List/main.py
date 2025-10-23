
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def createListWithLoop(self, arr: List[int], pos: int) -> ListNode:
        """Helper method to create linked list with a loop at given position"""
        if not arr:
            return None
            
        # Create nodes
        head = ListNode(arr[0])
        current = head
        nodes = [head]  # Store nodes to create loop later
        
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
            nodes.append(current)
            
        # Create loop if pos is valid
        if pos >= 0 and pos < len(nodes):
            current.next = nodes[pos]
            
        return head

    def detectAndFindStartOfLoop(self, head: ListNode) -> Optional[ListNode]:
        """Detect cycle and find the start node of the loop using Floyd's algorithm"""
        if not head or not head.next:
            return None
            
        # Step 1: Detect cycle using slow and fast pointers
        slow = fast = head
        has_cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
                
        # If no cycle found, return None
        if not has_cycle:
            return None
            
        # Step 2: Find start of cycle
        # Reset one pointer to head and move both one step at a time
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow

    def removeLoop(self, head: ListNode) -> None:
        """Remove loop in the linked list"""
        if not head or not head.next:
            return
            
        # Find start of loop
        loop_start = self.detectAndFindStartOfLoop(head)
        
        # If no loop exists, return
        if not loop_start:
            return
            
        # Find node pointing to loop start
        current = loop_start
        while current.next != loop_start:
            current = current.next
            
        # Break the loop
        current.next = None

    def printList(self, head: ListNode) -> List[int]:
        """Helper method to print list and return values"""
        result = []
        current = head
        visited = set()  # To prevent infinite loop while printing
        
        while current and id(current) not in visited:
            result.append(current.val)
            visited.add(id(current))
            current = current.next
            
        return result

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1, 3, 4, 2], 1),      # Loop to second node
        ([1, 2, 3, 4], -1),     # No loop
        ([5, 6, 7, 8], 0),      # Loop to first node
        ([1, 2], 1),            # Loop between two nodes
        ([1], -1),              # Single node, no loop
        ([1], 0),               # Single node with self-loop
        ([1, 2, 3, 4, 5], 2)    # Loop to middle node
    ]
    
    for arr, pos in test_cases:
        # Create linked list with loop
        head = sol.createListWithLoop(arr, pos)
        
        print(f"Input array: {arr}, Loop position: {pos}")
        print(f"Before removing loop: ", end="")
        # Only print first occurrence of each node to avoid infinite loop
        print(sol.printList(head))
        
        # Remove loop
        sol.removeLoop(head)
        
        print(f"After removing loop: {sol.printList(head)}")
        print()
