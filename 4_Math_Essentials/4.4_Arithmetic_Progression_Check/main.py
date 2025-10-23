# Arithmetic Progression Check
# Topic: Math Essentials
# Type: Home Challenge

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array
        arr.sort()
        
        # Check if the difference between consecutive elements is constant
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.canMakeArithmeticProgression([3,5,1]))  # Output: True
    print(sol.canMakeArithmeticProgression([1,2,4]))  # Output: False
