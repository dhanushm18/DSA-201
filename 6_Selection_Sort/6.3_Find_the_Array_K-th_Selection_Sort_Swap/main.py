# Find the Array K-th Selection Sort Swap
# Topic: Selection Sort
# Type: Home Challenge

class Solution:
    def selectionSortKthSwap(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        swap_count = 0
        
        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            
            # Swap if minimum element is not at its correct position
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
                swap_count += 1
                if swap_count == k:
                    # Return array after k-th swap
                    return nums
                
        # If k is greater than total swaps needed, return sorted array
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.selectionSortKthSwap([64,25,12,22,11], 2))  # Output: [11,12,25,22,64]