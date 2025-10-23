# Longest Palindromic Substring using Manacher's Algorithm
# Topic: Strings with Two Pointer Technique
# Type: Home Challenge

class Solution:
    def preprocess(self, s: str) -> str:
        # Transform string to handle even length palindromes
        # e.g., "abc" -> "^#a#b#c#$"
        return '^#' + '#'.join(s) + '#$'
        
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        # Preprocess the string
        processed = self.preprocess(s)
        n = len(processed)
        # P[i] represents palindrome radius at center i
        P = [0] * n
        center = right = 0  # center and right boundary of current palindrome
        max_center = max_len = 0  # center and length of longest palindrome
        
        # Main Manacher's algorithm loop
        for i in range(1, n-1):
            if i < right:
                # Mirror property: P[i] is at least min(P[2*center-i], right-i)
                P[i] = min(right - i, P[2*center - i])
            
            # Attempt to expand palindrome centered at i
            while processed[i + P[i] + 1] == processed[i - P[i] - 1]:
                P[i] += 1
            
            # Update center and right boundary if needed
            if i + P[i] > right:
                center = i
                right = i + P[i]
            
            # Update longest palindrome if needed
            if P[i] > max_len:
                max_len = P[i]
                max_center = i
        
        # Extract the longest palindromic substring
        start = (max_center - max_len) // 2
        return s[start:start + max_len]

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abacdfgdcaba"))  # Output: "aba"
    print(sol.longestPalindrome("bananas"))       # Output: "anana"
