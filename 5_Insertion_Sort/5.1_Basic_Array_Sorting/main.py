# Basic Array Sorting
# Topic: Insertion Sort
# Type: In-Session

class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        # Start from the second element
        for i in range(1, len(nums)):
            key = nums[i]
            # Move elements that are greater than key to one position ahead
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.insertionSort([5,2,3,1]))        # Output: [1,2,3,5]
    print(sol.insertionSort([10,7,8,9,1]))    # Output: [1,7,8,9,10]
