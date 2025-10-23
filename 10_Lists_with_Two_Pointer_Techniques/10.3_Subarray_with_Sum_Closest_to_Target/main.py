# Subarray with Sum Closest to Target
# Topic: Lists with Two Pointer Techniques
# Type: Home Challenge

class Solution:
    def closestPair(self, nums: list[int], target: int) -> list[int]:
        if not nums or len(nums) < 2:
            return []
            
        left, right = 0, len(nums) - 1
        min_diff = float('inf')
        result = [0, 0]
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            curr_diff = abs(curr_sum - target)
            
            # Update result if current difference is smaller
            if curr_diff < min_diff:
                min_diff = curr_diff
                result = [left, right]
            # If differences are equal, keep the pair with smaller first index
            elif curr_diff == min_diff and left < result[0]:
                result = [left, right]
                
            # Move pointers based on sum comparison
            if curr_sum < target:
                left += 1
            else:
                right -= 1
                
        return result

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.closestPair([-7,-3,2,5,10], 6))      # Output: [2,3]
    print(sol.closestPair([1,3,5,8,12], 16))       # Output: [3,4]
    print(sol.closestPair([-10,-5,-2,1], -9))      # Output: [0,2]

