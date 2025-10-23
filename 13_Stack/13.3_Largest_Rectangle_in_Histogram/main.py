# Largest Rectangle in Histogram
# Topic: Stack
# Type: Home Challenge

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Calculate largest rectangle area in histogram using monotonic stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Add 0 at end to handle remaining elements in stack
        heights.append(0)
        stack = [-1]  # Stack to store indices, initialized with -1 for edge case
        max_area = 0
        
        # Process all bars
        for i in range(len(heights)):
            # While current height is smaller than height at top of stack
            while heights[i] < heights[stack[-1]]:
                # Pop and calculate area with popped bar as height
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        # Remove the added 0
        heights.pop()
        return max_area
    
    def visualize_histogram(self, heights: List[int]) -> str:
        """Helper method to visualize histogram"""
        if not heights:
            return "Empty histogram"
            
        # Find maximum height for visualization
        max_height = max(heights)
        
        # Build histogram visualization
        visualization = []
        for h in range(max_height, 0, -1):
            row = ""
            for bar in heights:
                if bar >= h:
                    row += "█ "
                else:
                    row += "  "
            visualization.append(row)
            
        # Add bar values at bottom
        bottom = ""
        for val in heights:
            bottom += f"{val} "
            
        visualization.append("-" * (len(heights) * 2))
        visualization.append(bottom)
        
        return "\n".join(visualization)

# Demo
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = [
        [2, 1, 5, 6, 2, 3],      # Example 1
        [2, 4],                  # Example 2
        [6, 2, 5, 4, 5, 1, 6],  # Example 3
        [1, 1, 1, 1],           # Example 4
        [4, 3, 2, 1],           # Example 5
        [0, 0, 0],              # Example 6
        [2, 1, 2],              # Example 7
    ]
    
    for i, heights in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print("Input histogram:")
        print(sol.visualize_histogram(heights))
        area = sol.largestRectangleArea(heights)
        print(f"\nLargest rectangle area: {area}")
        print("-" * 40)

