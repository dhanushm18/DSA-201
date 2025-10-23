# Power Detection
# Topic: Math Essentials
# Type: In-Session

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is positive and has exactly one bit set
        return n > 0 and (n & (n - 1)) == 0

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(1))   # Output: True
    print(sol.isPowerOfTwo(16))  # Output: True
    print(sol.isPowerOfTwo(3))   # Output: False
