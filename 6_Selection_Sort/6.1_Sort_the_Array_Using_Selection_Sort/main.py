# Sort the Array Using Selection Sort
# Topic: Selection Sort
# Type: In-Session

class Solution:
    def selectionSort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Traverse through all array elements
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
                    
            # Swap the found minimum element with the first element
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.selectionSort([64,25,12,22,11]))  # Output: [11,12,22,25,64]
    print(sol.selectionSort([5,1,4,2,8]))       # Output: [1,2,4,5,8]
