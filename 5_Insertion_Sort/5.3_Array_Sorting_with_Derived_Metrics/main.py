# Array Sorting with Derived Metrics
# Topic: Insertion Sort
# Type: Home Challenge

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        def insertionSort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return arr
        
        # Sort both arrays
        seats = insertionSort(seats)
        students = insertionSort(students)
        
        # Calculate total moves
        total_moves = 0
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
            
        return total_moves

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.minMovesToSeat([3,1,5], [2,7,4]))  # Output: 4