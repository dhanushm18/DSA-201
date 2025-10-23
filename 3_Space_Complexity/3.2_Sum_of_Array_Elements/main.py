# Sum of Array Elements
# Topic: Space Complexity
# Type: In-Session

class Solution:
    def sumArray(self, arr: list[int]) -> int:
        total = 0
        for num in arr:
            total += num
        return total

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.sumArray([1,2,3]))          # Output: 6
    print(sol.sumArray([-5,10,-3]))       # Output: 2

