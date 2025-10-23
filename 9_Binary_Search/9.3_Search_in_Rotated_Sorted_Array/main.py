# Search in Rotated Sorted Array
# Topic: Binary Search
# Type: Home Challenge

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half must be sorted
            else:
                # Check if target is in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))        # Output: 4
    print(sol.search([6,7,8,1,2,3,4,5], 8))      # Output: 2
    print(sol.search([7,8,1,2,3,4,5,6], 5))      # Output: 6
