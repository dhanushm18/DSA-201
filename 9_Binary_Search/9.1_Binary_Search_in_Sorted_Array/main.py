# Binary Search in Sorted Array
# Topic: Binary Search
# Type: In-Session

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1,2,3,4,5], 3))              # Output: 2
    print(sol.search([-10,-3,0,4,8,12], 4))        # Output: 3
    print(sol.search([2,4,5,7,10], 6))             # Output: -1
