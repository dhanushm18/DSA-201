# Quadratic Time (O(n²))
# Topic: Time & Space Complexity
# Type: Home Challenge

class Solution:
    def allPairs(self, arr: list[int]) -> list[tuple[int,int]]:
        result = []
        for i in arr:
            for j in arr:
                result.append((i,j))
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allPairs([1,2,3]))  # Output: (1,1),(1,2),(1,3),(2,1),...
    print(sol.allPairs([5,6]))    # Output: (5,5),(5,6),(6,5),(6,6)
    print(sol.allPairs([7]))      # Output: (7,7)

