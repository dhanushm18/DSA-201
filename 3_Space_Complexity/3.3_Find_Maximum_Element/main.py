# Find Maximum Element
# Topic: Space Complexity
# Type: In-Session

class Solution:
    def maxElement(self, arr: list[int]) -> int:
        # Initialize max with first element
        max_elem = arr[0]
        for num in arr[1:]:
            if num > max_elem:
                max_elem = num
        return max_elem

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxElement([3,7,2,9,5]))    # Output: 9
    print(sol.maxElement([-10,-5,-1]))    # Output: -1
