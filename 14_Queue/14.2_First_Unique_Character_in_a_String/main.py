# First Unique Character in a String
# Topic: Queue
# Type: In-Session

from collections import Counter, deque

def firstUniqChar(s: str) -> int:
    """
    Find the first non-repeating character in the string and return its index
    Time Complexity: O(n)
    Space Complexity: O(1) - limited by alphabet size (26)
    """
    # Count frequency of each character
    char_count = Counter(s)
    
    # Create queue of potential unique characters with their indices
    queue = deque()
    
    # Process each character and its index
    for i, char in enumerate(s):
        # If character appears only once, add to queue with its index
        if char_count[char] == 1:
            return i
        
    return -1

def firstUniqCharWithQueue(s: str) -> int:
    """
    Alternative implementation using queue to track potential unique characters
    Useful for streaming data where we don't have the entire string at once
    """
    # Count frequency of each character
    char_count = {}
    # Queue to maintain order of characters
    queue = deque()
    
    # Process each character and its index
    for i, char in enumerate(s):
        # Update character count
        char_count[char] = char_count.get(char, 0) + 1
        
        # If this is first occurrence, add to queue
        if char_count[char] == 1:
            queue.append((char, i))
        
        # Remove characters from queue front if they are no longer unique
        while queue and char_count[queue[0][0]] > 1:
            queue.popleft()
    
    # Return index of first unique character if exists
    return queue[0][1] if queue else -1

# Demo
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "leetcode",      # First unique: 'l' at index 0
        "loveleetcode",  # First unique: 'v' at index 2
        "aabb",          # No unique character
        "aabcd",         # First unique: 'b' at index 2
        "z",             # Single character
        "aadadaad",      # No unique character
        "abcabcabc",     # No unique character
        "abcdefg",       # All unique characters
    ]
    
    print("Using Counter approach:")
    for s in test_cases:
        result = firstUniqChar(s)
        unique_char = s[result] if result != -1 else "None"
        print(f'Input: "{s}"')
        print(f"First unique character index: {result}")
        print(f"Character: {unique_char}")
        print()
        
    print("\nUsing Queue approach:")
    for s in test_cases:
        result = firstUniqCharWithQueue(s)
        unique_char = s[result] if result != -1 else "None"
        print(f'Input: "{s}"')
        print(f"First unique character index: {result}")
        print(f"Character: {unique_char}")
        print()
