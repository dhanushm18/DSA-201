# Sort an Array Using Quick Sort
# Topic: Quick Sort
# Type: In-Session

from typing import List

class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1  # Index of smaller element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if nums[j] <= pivot:
                i += 1  # Increment index of smaller element
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
    def quickSort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            # pi is partitioning index
            pi = self.partition(nums, low, high)
            
            # Separately sort elements before and after partition
            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArray([5,2,3,1]))          # Output: [1,2,3,5]
    print(sol.sortArray([10,7,8,9,1,5]))     # Output: [1,5,7,8,9,10]
