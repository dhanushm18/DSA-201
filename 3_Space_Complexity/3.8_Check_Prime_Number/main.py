# Check Prime Number
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        # Check up to square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPrime(7))                 # Output: True
    print(sol.isPrime(10))                # Output: False
