# Jump Game VI
# Topic: Queue
# Type: Home Challenge

from typing import List, Tuple
from collections import deque

def maxResult(nums: List[int], k: int) -> int:
    """
    Calculate maximum score by jumping through array with constraints
    Time Complexity: O(n) where n is length of nums
    Space Complexity: O(k) for the deque
    """
    if not nums:
        return 0
        
    n = len(nums)
    # dp[i] represents max score reaching index i
    dp = [0] * n
    dp[0] = nums[0]
    
    # Monotonic decreasing deque storing indices
    # deque[0] always contains index with maximum score within window
    deque_max = deque([0])
    
    for i in range(1, n):
        # Remove indices outside the window of size k
        while deque_max and deque_max[0] < i - k:
            deque_max.popleft()
            
        # Current max score is the score at front of deque plus current number
        dp[i] = dp[deque_max[0]] + nums[i]
        
        # Remove indices with smaller scores from the back
        while deque_max and dp[deque_max[-1]] <= dp[i]:
            deque_max.pop()
            
        deque_max.append(i)
        
    return dp[n-1]

def visualize_jumps(nums: List[int], k: int) -> str:
    """Helper function to visualize the jump game and optimal path"""
    if not nums:
        return "Empty array"
        
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    prev = [-1] * n  # Store previous jump index
    
    # Monotonic deque storing (score, index)
    deque_max = deque([0])
    
    # Calculate dp and track path
    for i in range(1, n):
        while deque_max and deque_max[0] < i - k:
            deque_max.popleft()
            
        dp[i] = dp[deque_max[0]] + nums[i]
        prev[i] = deque_max[0]  # Track where we jumped from
        
        while deque_max and dp[deque_max[-1]] <= dp[i]:
            deque_max.pop()
            
        deque_max.append(i)
    
    # Reconstruct optimal path
    path = []
    curr = n - 1
    while curr != -1:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    
    # Create visualization
    result = ["Jump Game Visualization:"]
    
    # Show array with values
    array_viz = "Array:  "
    for i, num in enumerate(nums):
        array_viz += f"{num:3d} "
    result.append(array_viz)
    
    # Show indices
    index_viz = "Index:  "
    for i in range(n):
        index_viz += f"{i:3d} "
    result.append(index_viz)
    
    # Show optimal path
    path_viz = "Path:   "
    for i in range(n):
        if i in path:
            path_viz += " *  "
        else:
            path_viz += "    "
    result.append(path_viz)
    
    # Show details
    result.append(f"\nOptimal path indices: {path}")
    result.append(f"Maximum score: {dp[n-1]}")
    result.append(f"Path values: {[nums[i] for i in path]}")
    result.append(f"Maximum jump distance (k): {k}")
    
    return "\n".join(result)

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, -1, -2, 4, -7, 3], 2),            # Basic case
        ([10, -5, -2, 4, 0, 3], 3),            # Longer jumps
        ([1, -5, -20, 4, -1, 3, -6, -3], 2),   # Negative values
        ([100, -1, -100, -1, 100], 2),         # Large differences
        ([1, 1, 1, 1], 2),                     # All same values
        ([5], 1),                              # Single element
        ([1, -10, 2, -10, 3], 2),              # Strategic jumps needed
        ([10, -2, -3, -4, 10], 3)              # Skip negative values
    ]
    
    for i, (nums, k) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Maximum jump distance (k): {k}")
        
        result = maxResult(nums, k)
        print(f"\n{visualize_jumps(nums, k)}")
        print("-" * 50)

