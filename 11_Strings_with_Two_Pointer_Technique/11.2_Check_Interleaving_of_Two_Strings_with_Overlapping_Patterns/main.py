# Check Interleaving of Two Strings with Overlapping Patterns
# Topic: Strings with Two Pointer Technique
# Type: Home Challenge

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if lengths match
        if len(s1) + len(s2) != len(s3):
            return False
            
        # Make s1 the shorter string to optimize space
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            
        # Initialize the dp array
        # dp[j] represents if we can form s3[:i+j] using s1[:i] and s2[:j]
        m, n = len(s1), len(s2)
        dp = [False] * (m + 1)
        dp[0] = True
        
        # Initialize first row (using only s1)
        for i in range(1, m + 1):
            dp[i] = dp[i-1] and s1[i-1] == s3[i-1]
            
        # Fill dp array row by row
        for j in range(1, n + 1):
            dp[0] = dp[0] and s2[j-1] == s3[j-1]
            for i in range(1, m + 1):
                # Current position in s3
                k = i + j - 1
                # dp[i] represents previous row's value
                dp[i] = (dp[i] and s2[j-1] == s3[k]) or (dp[i-1] and s1[i-1] == s3[k])
                
        return dp[m]

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.isInterleave("aabcc","dbbca","aadbbcbcac"))  # Output: True 
    print(sol.isInterleave("aabcc","dbbca","aadbbbaccc"))  # Output: False
