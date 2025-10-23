# Modular Arithmetic Application
# Topic: Math Essentials
# Type: Home Challenge

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k is even or ends in 5, it can't divide a number made of all 1s
        if k % 2 == 0 or k % 5 == 0:
            return -1
            
        remainder = 1
        length = 1
        
        # Use a set to detect cycle
        seen = set()
        
        while remainder % k != 0:
            remainder = (remainder * 10 + 1) % k
            length += 1
            
            # If we've seen this remainder before, we're in a cycle
            if remainder in seen:
                return -1
            seen.add(remainder)
            
        return length

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestRepunitDivByK(1))  # Output: 1
    print(sol.smallestRepunitDivByK(2))  # Output: -1
    print(sol.smallestRepunitDivByK(3))  # Output: 3
