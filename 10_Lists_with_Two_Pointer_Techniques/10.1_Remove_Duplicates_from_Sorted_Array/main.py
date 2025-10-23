# Remove Duplicates from Sorted Array
# Topic: Lists with Two Pointer Techniques
# Type: In-Session

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # Initialize the pointer for unique elements
        write_pos = 1
        
        # Iterate through the array starting from second element
        for i in range(1, len(nums)):
            # If current element is different from previous element
            if nums[i] != nums[i-1]:
                # Place it at write_pos and increment write_pos
                nums[write_pos] = nums[i]
                write_pos += 1
                
        return write_pos

# Demo
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    print(sol.removeDuplicates(nums))               # Output: 2
    print(nums[:2])                                 # Output: [1,2]
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))              # Output: 5
    print(nums[:5])                                # Output: [0,1,2,3,4]
