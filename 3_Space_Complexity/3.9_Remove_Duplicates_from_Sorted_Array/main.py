# Remove Duplicates from Sorted Array
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        if not arr:
            return 0
            
        # Two pointer technique
        write_pos = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                arr[write_pos] = arr[i]
                write_pos += 1
        return write_pos

# Demo
if __name__ == '__main__':
    sol = Solution()
    arr = [1,1,2,2,3]
    length = sol.removeDuplicates(arr)
    print(length)                        # Output: 3
    print(arr[:length])                   # Output: [1,2,3]

