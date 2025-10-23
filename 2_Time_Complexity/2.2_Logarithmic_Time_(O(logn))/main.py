# Logarithmic Time (O(logn))
# Topic: Time & Space Complexity
# Type: In-Session

class Solution:
    def divideUntilOne(self, n: int) -> int:
        steps=0
        while n>1:
            n=n//2
            steps=steps+1

        return steps
        

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.divideUntilOne(16))  # Output: 4
    print(sol.divideUntilOne(8))   # Output: 3
    print(sol.divideUntilOne(1))   # Output: 0
    print(sol.divideUntilOne(100)) # Output: 6

