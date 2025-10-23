# Factorial Time (O(n!))
# Topic: Time & Space Complexity
# Type: In-Session

class Solution:
    def allPermutations(self, s: str) -> list[str]:
        
        def backtrack(chars: list, path: str, result: list):
            # If current permutation is complete
            if not chars:
                result.append(path)
                return
            
            # Try each remaining character at current position
            for i in range(len(chars)):
                # Choose current character
                curr = chars[i]
                # Remove it from available characters
                remaining = chars[:i] + chars[i+1:]
                # Recursively build permutations with remaining chars
                backtrack(remaining, path + curr, result)
        
        result = []
        backtrack(list(s), "", result)
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allPermutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(sol.allPermutations("ab"))   # Output: ['ab', 'ba']
    print(sol.allPermutations("a"))    # Output: ['a']
