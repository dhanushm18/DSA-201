# Minimum Swaps Using Selection Sort
# Topic: Selection Sort
# Type: Home Challenge

class Solution:
    def countSelectionSortSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        swaps = 0
        
        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            # Swap only if minimum element is not at its correct position
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
                swaps += 1
                
        return swaps

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.countSelectionSortSwaps([64,25,12,22,11]))  # Output: 3
    print(sol.countSelectionSortSwaps([1,2,3,4]))         # Output: 0
