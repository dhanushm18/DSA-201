from typing import Optional, List

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def createMultilevelList(self, structure: List[List[int]]) -> Optional[Node]:
        """Helper method to create multilevel doubly linked list from structure
        structure is a list of lists where each inner list represents a level
        and None represents no connection between levels"""
        if not structure:
            return None
            
        # Create nodes for each level
        levels = []
        for level in structure:
            if level is None:
                levels.append(None)
                continue
                
            # Create nodes for current level
            prev = None
            level_head = None
            for val in level:
                curr = Node(val)
                if prev:
                    prev.next = curr
                    curr.prev = prev
                else:
                    level_head = curr
                prev = curr
            levels.append(level_head)
            
        # Connect levels with child pointers
        for i in range(len(levels)-1):
            if levels[i] is None or levels[i+1] is None:
                continue
                
            # Find node to attach child to (can be customized)
            curr = levels[i]
            curr.child = levels[i+1]
            
        return levels[0]
    
    def printList(self, head: Optional[Node]) -> List[List[int]]:
        """Helper method to print multilevel list structure"""
        result = []
        curr = head
        while curr:
            # Print current level
            level = []
            temp = curr
            while temp:
                level.append(temp.val)
                temp = temp.next
            result.append(level)
            
            # Move to child level if exists
            if curr.child:
                curr = curr.child
            else:
                break
                
        return result

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        """Flatten a multilevel doubly linked list"""
        if not head:
            return None
            
        # Keep track of current node
        current = head
        
        # Process all nodes
        while current:
            # If no child, move to next node
            if not current.child:
                current = current.next
                continue
                
            # Save pointer to child and next node
            child = current.child
            next_node = current.next
            
            # Connect current node with child
            current.next = child
            child.prev = current
            current.child = None  # Remove child pointer
            
            # Find end of child list
            tail = child
            while tail.next:
                tail = tail.next
                
            # Connect tail with next_node if exists
            if next_node:
                tail.next = next_node
                next_node.prev = tail
                
            # Move to next node
            current = child
            
        return head

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        # Test case 1: Basic case with one child
        [[1, 2, 3], [4, 5]],
        
        # Test case 2: Multiple levels
        [[1, 2], [3, 4], [5, 6]],
        
        # Test case 3: Single node with child
        [[1], [2]],
        
        # Test case 4: Empty list
        [],
        
        # Test case 5: No children
        [[1, 2, 3]],
        
        # Test case 6: Multiple children at different nodes
        [[1, 2, 3, 4], [5, 6], [7, 8]],
        
        # Test case 7: Complex structure
        [[1], [2, 3], [4], [5, 6, 7]]
    ]
    
    for i, structure in enumerate(test_cases):
        # Create multilevel list
        head = sol.createMultilevelList(structure)
        
        print(f"Test case {i + 1}:")
        print("Original structure:", structure)
        
        # Flatten the list
        flattened = sol.flatten(head)
        
        # Print result
        result = []
        curr = flattened
        while curr:
            result.append(curr.val)
            curr = curr.next
        print("Flattened list:", result)
        print()
