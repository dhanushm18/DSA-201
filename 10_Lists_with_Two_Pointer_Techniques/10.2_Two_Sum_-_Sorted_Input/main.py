# Two Sum - Sorted Input
# Topic: Lists with Two Pointer Techniques
# Type: In-Session


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            
            if curr_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return []  # No solution found

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))             # Output: [1,2]
    print(sol.twoSum([1,2,3,4,4,9,56,90], 8))     # Output: [4,5]
