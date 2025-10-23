# Factorial of a Number
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def factorial(self, n: int) -> int:
        # Iterative factorial to save space
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.factorial(5))               # Output: 120
    print(sol.factorial(0))               # Output: 1

