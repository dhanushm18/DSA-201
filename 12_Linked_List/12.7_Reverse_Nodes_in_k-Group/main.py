from typing import List, Optional

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

    def reverseGroup(self, head: ListNode, k: int) -> tuple[ListNode, ListNode]:
        """Helper method to reverse k nodes starting from head"""
        # Initialize pointers for reversal
        prev = None
        curr = head
        next_node = None
        count = 0
        
        # Reverse k nodes
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
            
        # Return new head (prev) and next group's head (next_node)
        return prev, next_node

    def countNodes(self, head: ListNode) -> int:
        """Helper method to count number of nodes"""
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse nodes in k-group"""
        # Handle base cases
        if not head or k <= 1:
            return head
            
        # Count total nodes to determine number of groups
        count = self.countNodes(head)
        
        # Initialize dummy node to handle head changes
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        # Process all complete groups
        while count >= k:
            curr_group_start = prev_group_end.next
            
            # Reverse current group
            next_group_start = curr_group_start
            for i in range(k-1):
                next_group_start = next_group_start.next
            
            next_group_remainder = next_group_start.next
            next_group_start.next = None
            
            # Get new head and connect with previous group
            new_group_head, _ = self.reverseGroup(curr_group_start, k)
            prev_group_end.next = new_group_head
            curr_group_start.next = next_group_remainder
            
            # Update pointers for next iteration
            prev_group_end = curr_group_start
            count -= k
            
        return dummy.next
    
# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3,4,5], 2),    # Standard case
        ([1,2,3,4,5], 3),    # Groups of 3
        ([1,2,3,4,5], 1),    # k=1, no reversal
        ([1], 1),            # Single node
        ([1,2], 2),          # Exactly k nodes
        ([1,2,3], 4),        # k larger than list length
        ([1,2,3,4,5,6], 3),  # Multiple complete groups
        ([1,2,3,4,5,6,7], 3) # Incomplete last group
    ]
    
    for i, (arr, k) in enumerate(test_cases):
        # Create input list
        head = sol.createList(arr)
        
        # Reverse in k-groups
        result = sol.reverseKGroup(head, k)
        
        print(f"Test case {i + 1}:")
        print(f"Input: array = {arr}, k = {k}")
        print(f"Output: {sol.printList(result)}")
        print()