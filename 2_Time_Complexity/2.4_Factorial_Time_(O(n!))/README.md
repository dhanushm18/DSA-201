# Factorial Time (O(n!))
**Topic:** Time & Space Complexity

**Type:** In-Session

### Problem Description
Generate all possible permutations of a given string without using Python's built-in itertools library.

### Approach
The solution uses a backtracking algorithm with the following steps:
1. Start with an empty result string and the full set of available characters
2. For each position in the permutation:
   - Try each remaining unused character
   - Recursively generate permutations with the remaining characters
   - Add completed permutations to the result list
3. Return all generated permutations

### Pseudocode
```
function allPermutations(s: string) -> list[string]:
    result = []
    
    function backtrack(chars: list, path: string, result: list):
        if chars is empty:
            add path to result
            return
            
        for i from 0 to length(chars)-1:
            curr = chars[i]
            remaining = chars excluding chars[i]
            backtrack(remaining, path + curr, result)
    
    backtrack(list of characters in s, "", result)
    return result
```

### Time Complexity
- O(n!) where n is the length of the input string
- This is because we generate all possible permutations, and there are n! permutations for a string of length n
- For each permutation, we also need O(n) work to construct the string

### Space Complexity
- O(n!) to store all permutations in the result list
- O(n) additional space for the recursion stack depth
- O(n) space for storing the current permutation being built
