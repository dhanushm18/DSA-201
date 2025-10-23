# Kth Largest Element Using Quick Sort
# Topic: Quick Sort
# Type: Home Challenge

from typing import List

class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left - 1
        
        for j in range(left, right):
            if nums[j] >= pivot:  # Changed comparison to handle largest elements
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
    
    def quickSelect(self, nums: List[int], left: int, right: int, k: int) -> int:
        if left <= right:
            pivot_idx = self.partition(nums, left, right)
            
            # If pivot is the k-th largest element
            if pivot_idx == k - 1:
                return nums[pivot_idx]
            # If pivot is greater than k, search in left subarray
            elif pivot_idx > k - 1:
                return self.quickSelect(nums, left, pivot_idx - 1, k)
            # If pivot is less than k, search in right subarray
            else:
                return self.quickSelect(nums, pivot_idx + 1, right, k)
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))       # Output: 5
    print(sol.findKthLargest([7,10,4,3,20,15], 3))    # Output: 10

