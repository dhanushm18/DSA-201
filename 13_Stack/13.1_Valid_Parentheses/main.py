# Valid Parentheses
# Topic: Stack
# Type: In-Session

class Solution:
    def isValid(self, s: str) -> bool:
        # Map of closing brackets to their corresponding opening brackets
        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Process each character in the string
        for char in s:
            # If it's a closing bracket
            if char in brackets_map:
                # Stack is empty or top of stack doesn't match
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                # Match found, pop the opening bracket
                stack.pop()
            # If it's an opening bracket, push to stack
            else:
                stack.append(char)
        
        # Valid only if all brackets are matched (stack is empty)
        return len(stack) == 0

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        "()",        # Simple valid case
        "()[]{}",    # Multiple valid pairs
        "(]",        # Mismatched brackets
        "([)]",      # Invalid nesting
        "{[]}",      # Valid nested brackets
        ")(",        # Invalid order
        "(((",       # Unclosed brackets
        "",          # Empty string
        "{",         # Single opening bracket
        "}",         # Single closing bracket
        "((()))",    # Multiple nested pairs
        "(){}}{",    # Invalid multiple pairs
    ]
    
    for s in test_cases:
        result = sol.isValid(s)
        print(f'Input: "{s}"')
        print(f"Output: {result}")
        print()

