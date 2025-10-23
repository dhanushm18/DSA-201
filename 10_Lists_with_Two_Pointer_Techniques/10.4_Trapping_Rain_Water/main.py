# Trapping Rain Water
# Topic: Lists with Two Pointer Techniques
# Type: Home Challenge

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        
        while left < right:
            # Update maximum height from left
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            # Update maximum height from right
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # Output: 6
    print(sol.trap([4,2,0,3,2,5]))               # Output: 9

