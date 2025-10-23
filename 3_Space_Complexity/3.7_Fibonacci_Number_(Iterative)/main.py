# Fibonacci Number (Iterative)
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def fibonacci(self, n: int) -> int:
        # Handle base cases
        if n <= 1:
            return n
            
        # Use two variables to track previous numbers
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.fibonacci(6))               # Output: 8
    print(sol.fibonacci(0))               # Output: 0

