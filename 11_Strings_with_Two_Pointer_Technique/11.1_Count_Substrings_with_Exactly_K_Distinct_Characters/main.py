# Count Substrings with Exactly K Distinct Characters
# Topic: Strings with Two Pointer Technique
# Type: In-Session

class Solution:
    def exactly_k_chars(self, s: str, k: int) -> int:
        # Helper function to count windows with exactly k distinct characters
        char_count = {}
        distinct = 0
        result = 0
        left = 0
        
        for right in range(len(s)):
            # Add right character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            if char_count[s[right]] == 1:
                distinct += 1
            
            # Shrink window while we have more than k distinct characters
            while distinct > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    distinct -= 1
                left += 1
                
        return left, right + 1

    def substrCount(self, s: str, k: int) -> int:
        # Count substrings with exactly k distinct characters using the 
        # difference between at most k and at most (k-1) distinct characters
        def at_most_k(s: str, k: int) -> int:
            if k == 0:
                return 0
                
            char_count = {}
            distinct = 0
            result = 0
            left = 0
            
            for right in range(len(s)):
                # Add right character to window
                char_count[s[right]] = char_count.get(s[right], 0) + 1
                if char_count[s[right]] == 1:
                    distinct += 1
                
                # Shrink window while we have more than k distinct characters
                while distinct > k:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        distinct -= 1
                    left += 1
                
                # Add count of all valid substrings ending at right
                result += right - left + 1
            
            return result
        
        # Result is the difference between substrings with at most k distinct
        # and at most (k-1) distinct characters
        return at_most_k(s, k) - at_most_k(s, k - 1)

# Demo
if __name__ == "__main__":
    sol = Solution()
    print(sol.substrCount("pqpqs", 2))  # Output: 7
