# Longest Continuous Subarray With Absolute Diff ≤ K
# Topic: Queue
# Type: Home Challenge

from typing import List
from collections import deque

def longestSubarray(nums: List[int], limit: int) -> int:
    """
    Find the longest continuous subarray with max absolute difference <= limit
    Time Complexity: O(n) where n is length of nums
    Space Complexity: O(n) for the deques
    """
    if not nums:
        return 0
        
    n = len(nums)
    max_deque = deque()  # Monotonic decreasing queue for maximums
    min_deque = deque()  # Monotonic increasing queue for minimums
    left = 0            # Left pointer of window
    max_length = 0      # Length of longest valid subarray
    
    for right in range(n):
        # Update maximum deque
        while max_deque and nums[max_deque[-1]] < nums[right]:
            max_deque.pop()
        max_deque.append(right)
        
        # Update minimum deque
        while min_deque and nums[min_deque[-1]] > nums[right]:
            min_deque.pop()
        min_deque.append(right)
        
        # Shrink window while max difference > limit
        while max_deque and min_deque and \
              nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left += 1
            
            # Remove elements outside window from deques
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
        
    return max_length

def visualize_subarray(nums: List[int], start: int, end: int, limit: int) -> str:
    """Helper function to visualize the subarray and its properties"""
    if not nums or start > end or start < 0 or end >= len(nums):
        return "Invalid subarray"
        
    # Create visualization
    result = ["Subarray visualization:"]
    
    # Show full array with highlighted subarray
    array_viz = "Array: "
    for i, num in enumerate(nums):
        if i == start:
            array_viz += "["
        array_viz += str(num)
        if i == end:
            array_viz += "]"
        if i < len(nums) - 1:
            array_viz += " "
    result.append(array_viz)
    
    # Show subarray properties
    subarray = nums[start:end+1]
    min_val = min(subarray)
    max_val = max(subarray)
    diff = max_val - min_val
    
    result.append(f"Length: {end - start + 1}")
    result.append(f"Minimum: {min_val}")
    result.append(f"Maximum: {max_val}")
    result.append(f"Max difference: {diff}")
    result.append(f"Limit: {limit}")
    result.append(f"Valid: {diff <= limit}")
    
    return "\n".join(result)

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([8, 2, 4, 7], 4),                 # Basic case
        ([10, 1, 2, 4, 7, 2], 5),         # Multiple valid subarrays
        ([4, 2, 2, 2, 4, 4, 2, 2], 0),    # Zero limit
        ([1, 5, 6, 7, 8, 10, 6, 5, 6], 4),# Complex case
        ([1, 1, 1], 1),                    # All same elements
        ([5], 5),                          # Single element
        ([3, 6, 9, 1, 4, 7], 3),          # Various differences
        ([10, 5, 2, 7, 8, 7], 4)          # Multiple windows
    ]
    
    for i, (nums, limit) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Limit: {limit}")
        
        # Find longest subarray
        result = longestSubarray(nums, limit)
        print(f"Length of longest valid subarray: {result}")
        
        # Find and visualize one valid subarray of maximum length
        left = 0
        max_length = 0
        best_start = best_end = 0
        
        for right in range(len(nums)):
            while left <= right and max(nums[left:right+1]) - min(nums[left:right+1]) > limit:
                left += 1
            if right - left + 1 > max_length:
                max_length = right - left + 1
                best_start = left
                best_end = right
                
        print("\nFound valid subarray:")
        print(visualize_subarray(nums, best_start, best_end, limit))
        print("-" * 50)
