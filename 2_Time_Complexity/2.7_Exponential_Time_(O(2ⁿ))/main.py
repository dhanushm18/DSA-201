# Exponential Time (O(2ⁿ))
# Topic: Time & Space Complexity
# Type: Home Challenge


class Solution:
    def allSubsets(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        result = []
        # Generate all possible combinations using binary numbers
        for i in range(2**n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(arr[j])
            result.append(subset)
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allSubsets([1,2]))      # Output: [], [1], [2], [1,2]
    print(sol.allSubsets([3]))        # Output: [], [3]
    print(sol.allSubsets([1,2,3]))    # Output: 8 subsets

