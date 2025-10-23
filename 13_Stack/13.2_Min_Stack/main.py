# Min Stack
# Topic: Stack
# Type: In-Session

class MinStack:
    def __init__(self):
        """Initialize your data structure here"""
        self.stack = []        # Main stack for values
        self.min_stack = []    # Stack to track minimums
        
    def push(self, val: int) -> None:
        """Push element val onto stack"""
        self.stack.append(val)
        
        # If min_stack is empty or val is less than or equal to current minimum
        # push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        """Removes the element on top of the stack"""
        if not self.stack:
            return
            
        # If popped value is the current minimum, also pop from min_stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
            
        self.stack.pop()
        
    def top(self) -> int:
        """Get the top element"""
        if self.stack:
            return self.stack[-1]
        return None
        
    def getMin(self) -> int:
        """Retrieve the minimum element in the stack"""
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Demo
if __name__ == "__main__":
    def test_min_stack(operations, values):
        min_stack = None
        results = []
        
        for op, val in zip(operations, values):
            if op == "MinStack":
                min_stack = MinStack()
                results.append(None)
            elif op == "push":
                min_stack.push(val[0])
                results.append(None)
            elif op == "pop":
                min_stack.pop()
                results.append(None)
            elif op == "top":
                results.append(min_stack.top())
            elif op == "getMin":
                results.append(min_stack.getMin())
                
        return results
    
    # Test cases
    test_cases = [
        # Test case 1: Example from problem
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []]
        ),
        
        # Test case 2: Pushing same values
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [1], [1], [1], [], [], []]
        ),
        
        # Test case 3: Ascending values
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [1], [2], [3], [], [], []]
        ),
        
        # Test case 4: Descending values
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [3], [2], [1], [], [], []]
        ),
        
        # Test case 5: Complex sequence
        (
            ["MinStack", "push", "push", "getMin", "push", "getMin", "pop", "getMin"],
            [[], [0], [1], [], [-1], [], [], []]
        )
    ]
    
    for i, (operations, values) in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        print("Operations:", operations)
        print("Values:", values)
        print("Results:", test_min_stack(operations, values))
        print()
