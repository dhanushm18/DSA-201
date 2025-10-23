# Array Sorting with Duplicates
# Topic: Insertion Sort
# Type: Home Challenge

class Solution:
    def sortByParity(self, nums: list[int]) -> list[int]:
        # Maintain two pointers: one for even numbers placement
        even_pos = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current number is even, place it at even_pos
            if nums[i] % 2 == 0:
                # Swap current number with number at even_pos
                nums[i], nums[even_pos] = nums[even_pos], nums[i]
                even_pos += 1
                
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.sortByParity([3,1,2,4]))   # Output: [2,4,3,1] or any even-before-odd order
    print(sol.sortByParity([0,5,6,7]))   # Output: [0,6,5,7]

