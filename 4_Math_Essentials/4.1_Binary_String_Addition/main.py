# Binary String Addition
# Topic: Math Essentials
# Type: In-Session

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize variables
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get digits, use 0 if string is exhausted
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            
            # Calculate sum and new carry
            current_sum = x + y + carry
            carry = current_sum // 2
            result.append(str(current_sum % 2))
            
            i -= 1
            j -= 1
        
        # Reverse and join the result
        return ''.join(result[::-1])

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("11", "1"))      # Output: "100"
    print(sol.addBinary("1010", "1011")) # Output: "10101"
