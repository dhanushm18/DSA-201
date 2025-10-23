# Sort a Linked List
# Topic: Merge Sort
# Type: Home Challenge

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getMid(self, head: ListNode) -> ListNode:
        # Use slow and fast pointer to find middle
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None
        return slow
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Merge two sorted linked lists
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next:
            return head
            
        # Split the list into two halves
        mid = self.getMid(head)
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the sorted halves
        return self.merge(left, right)

# Demo
if __name__ == '__main__':
    # Helper function to convert list to linked list
    def list_to_linked(lst):
        dummy = ListNode(0)
        cur = dummy
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
    
    # Helper function to convert linked list to list
    def linked_to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    
    sol = Solution()
    head = list_to_linked([4,2,1,3])
    sorted_head = sol.sortList(head)
    print(linked_to_list(sorted_head))  
