# Sort an Array Using Merge Sort
# Topic: Merge Sort
# Type: In-Session

from typing import List

class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        # Compare elements from both arrays and merge them in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def mergeSort(self, arr: List[int]) -> List[int]:
        # Base case: arrays of length 0 or 1 are already sorted
        if len(arr) <= 1:
            return arr
            
        # Divide array into two halves
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        
        # Merge the sorted halves
        return self.merge(left, right)

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeSort([5,2,3,1]))       # Output: [1,2,3,5]
    print(sol.mergeSort([10,7,8,9,1]))    # Output: [1,7,8,9,10]

