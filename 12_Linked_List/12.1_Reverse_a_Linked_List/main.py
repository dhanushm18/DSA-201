# Reverse a Linked List
# Topic: Linked List
# Type: In-Session

from typing import Optional, List

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative approach using three pointers"""
        if not head or not head.next:
            return head
            
        prev = None
        current = head
        
        while current:
            # Store next node
            next_node = current.next
            # Reverse current node's pointer
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = next_node
            
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive approach"""
        # Base case: empty list or single node
        if not head or not head.next:
            return head
            
        # Recursive case: reverse the rest of the list
        rest = self.reverseListRecursive(head.next)
        
        # Set head node's next's next to point to head
        head.next.next = head
        # Set head's next to None to avoid cycle
        head.next = None
        
        return rest

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
        [10, 20, 30],
        [5, 5, 5]
    ]
    
    for arr in test_cases:
        # Create linked list
        head = sol.createList(arr)
        
        # Test iterative solution
        reversed_head = sol.reverseList(sol.createList(arr))
        print(f"Input: {arr}")
        print(f"Output (Iterative): {sol.printList(reversed_head)}")
        
        # Test recursive solution
        reversed_head_recursive = sol.reverseListRecursive(sol.createList(arr))
        print(f"Output (Recursive): {sol.printList(reversed_head_recursive)}")
        print()
