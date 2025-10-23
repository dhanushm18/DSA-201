# Remove Nth Node from End of List
# Topic: Linked List
# Type: Home Challenge
from typing import Optional, List

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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node to handle edge case of removing head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize fast and slow pointers
        fast = slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Remove nth node by updating next pointer
        slow.next = slow.next.next
        
        return dummy.next

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 1),
        ([10, 20, 30, 40], 4),
        ([5, 5, 5, 5, 5], 3),
        ([100, 200, 300], 1)
    ]
    
    for arr, n in test_cases:
        # Create linked list
        head = sol.createList(arr)
        
        # Remove nth node from end
        result = sol.removeNthFromEnd(head, n)
        
        print(f"Input: {arr}, n = {n}")
        print(f"Output: {sol.printList(result)}")
        print()
