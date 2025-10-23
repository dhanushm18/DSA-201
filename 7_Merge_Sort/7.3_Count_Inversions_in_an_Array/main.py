# Count Inversions in an Array
# Topic: Merge Sort
# Type: Home Challenge

from typing import List

class Solution:
    def merge(self, arr: List[int], left: int, mid: int, right: int) -> int:
        inversions = 0
        i = left
        j = mid + 1
        temp = []
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                # When arr[i] > arr[j], all elements from i to mid form inversions with arr[j]
                inversions += mid - i + 1
                temp.append(arr[j])
                j += 1
        
        # Add remaining elements
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
            
        # Copy back to original array
        for k in range(len(temp)):
            arr[left + k] = temp[k]
            
        return inversions
    
    def mergeSortAndCount(self, arr: List[int], left: int, right: int) -> int:
        inversions = 0
        if left < right:
            mid = (left + right) // 2
            
            # Count inversions in left and right halves
            inversions += self.mergeSortAndCount(arr, left, mid)
            inversions += self.mergeSortAndCount(arr, mid + 1, right)
            
            # Count cross inversions while merging
            inversions += self.merge(arr, left, mid, right)
            
        return inversions
    
    def countInversions(self, arr: List[int]) -> int:
        return self.mergeSortAndCount(arr, 0, len(arr) - 1)

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.countInversions([2,4,1,3,5]))  # Output: 3
    print(sol.countInversions([5,4,3,2,1]))  # Output: 10

