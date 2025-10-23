# Find First and Last Position of Element in Sorted Array
# Topic: Binary Search
# Type: In-Session


class Solution:
    def findFirst(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid  # Save potential result
                right = mid - 1  # Keep searching left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def findLast(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid  # Save potential result
                left = mid + 1  # Keep searching right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
            
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        
        return [first, last]

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5,7,7,8,8,10], 8))     # Output: [3,4]
    print(sol.searchRange([1,1,2,2,2,3,4], 2))    # Output: [2,4]
    print(sol.searchRange([1,3,3,3,4,5], 6))      # Output: [-1,-1]
