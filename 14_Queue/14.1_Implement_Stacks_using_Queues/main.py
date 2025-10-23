# Implement Stacks using Queues
# Topic: Queue
# Type: In-Session

from collections import deque
from typing import List

class MyStack:
    def __init__(self):
        """Initialize data structure"""
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
        
    def push(self, x: int) -> None:
        """Push element x onto stack"""
        # Always push to q1
        self.q1.append(x)
        
    def pop(self) -> int:
        """Removes the element on top of the stack and returns that element"""
        if self.empty():
            return None
            
        # Move all elements except last from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        # Get the last element (top of stack)
        result = self.q1.popleft()
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return result
        
    def top(self) -> int:
        """Get the top element"""
        if self.empty():
            return None
            
        # Move all elements except last from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        # Get the last element (top of stack)
        result = self.q1[0]
        
        # Move last element to q2
        self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
        return result
        
    def empty(self) -> bool:
        """Returns whether the stack is empty"""
        return len(self.q1) == 0

def run_test(operations: List[str], values: List[List[int]]) -> List[any]:
    """Helper function to run test cases"""
    stack = None
    results = []
    
    for op, val in zip(operations, values):
        if op == "MyStack":
            stack = MyStack()
            results.append(None)
        elif op == "push":
            stack.push(val[0])
            results.append(None)
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "empty":
            results.append(stack.empty())
            
    return results

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Test case 1: Basic operations
        (
            ["MyStack", "push", "push", "top", "pop", "empty"],
            [[], [1], [2], [], [], []]
        ),
        
        # Test case 2: Push and pop all elements
        (
            ["MyStack", "push", "push", "pop", "pop", "empty"],
            [[], [5], [10], [], [], []]
        ),
        
        # Test case 3: Empty stack operations
        (
            ["MyStack", "empty", "push", "top"],
            [[], [], [3], []]
        ),
        
        # Test case 4: Multiple push and pop operations
        (
            ["MyStack", "push", "push", "push", "top", "pop", "pop", "empty"],
            [[], [7], [8], [9], [], [], [], []]
        ),
        
        # Test case 5: Single element operations
        (
            ["MyStack", "push", "top", "pop", "empty", "push", "empty"],
            [[], [1], [], [], [], [2], []]
        )
    ]
    
    for i, (operations, values) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print("Operations:", operations)
        print("Values:", values)
        results = run_test(operations, values)
        print("Results:", results)
