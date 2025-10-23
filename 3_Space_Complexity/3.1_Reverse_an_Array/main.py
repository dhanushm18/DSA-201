# Reverse an Array
# Topic: Space Complexity
# Type: In-Session

class Solution:
    def reverseArray(self, arr: list[int]) -> list[int]:
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseArray([1,2,3,4,5]))  # Output: [5,4,3,2,1]
    print(sol.reverseArray([10,20,30]))   # Output: [30,20,10]
