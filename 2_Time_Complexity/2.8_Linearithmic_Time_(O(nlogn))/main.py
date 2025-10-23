# Linearithmic Time (O(nlogn))
# Topic: Time & Space Complexity
# Type: Home Challenge

class Solution:
    def halveAndPrint(self, n: int) -> None:
        while n >= 1:
            print(*range(1, n+1))
            n = n // 2

# Demo
if __name__ == '__main__':
    sol = Solution()
    sol.halveAndPrint(8)
    # Output:
    # 1 2 3 4 5 6 7 8
    # 1 2 3 4
    # 1 2
    # 1

