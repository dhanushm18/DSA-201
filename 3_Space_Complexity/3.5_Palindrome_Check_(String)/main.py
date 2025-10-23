# Palindrome Check (String)
# Topic: Space Complexity
# Type: Home Challenge

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("madam"))      # Output: True
    print(sol.isPalindrome("hello"))      # Output: False

