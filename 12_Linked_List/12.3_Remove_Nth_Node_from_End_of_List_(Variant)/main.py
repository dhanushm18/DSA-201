# Remove Nth Node from End of List (Variant)
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

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Find middle node using slow-fast pointer technique"""
        if not head or not head.next:
            return head
            
        # Initialize slow and fast pointers
        slow = fast = head
        prev = None
        
        # Move fast pointer twice as fast as slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        # Break the list into two halves
        if prev:
            prev.next = None
            
        return slow

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists"""
        # Create dummy node for easier handling
        dummy = ListNode(0)
        current = dummy
        
        # Compare and merge nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Attach remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Sort linked list using merge sort"""
        # Base cases
        if not head or not head.next:
            return head
            
        # Find middle and split list
        mid = self.getMid(head)
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge sorted halves
        return self.merge(left, right)

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [4, 2, 1, 3],
        [2, 1],
        [3, 3, 1, 2],
        [],
        [10, -1, 5, 0],
        [100, 50, 50, 25],
        [5]
    ]
    
    for arr in test_cases:
        # Create linked list
        head = sol.createList(arr)
        
        # Sort list
        result = sol.sortList(head)
        
        print(f"Input: {arr}")
        print(f"Output: {sol.printList(result)}")
        print()
