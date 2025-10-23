# Constant Time (O(1))
# Topic: Time & Space Complexity
# Type: In-Session

class Solution:
    def maxOfTwo(self, a: int, b: int) -> int:
        return max(a,b)

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxOfTwo(7, 12))     # Output: 12
    print(sol.maxOfTwo(-5, -10))   # Output: -5
    print(sol.maxOfTwo(100, 100))  # Output: 100
