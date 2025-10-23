# Unique Permutations
# Topic: Math Essentials
# Type: Home Challenge

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(counter, curr_perm, n):
            if len(curr_perm) == n:
                result.append(curr_perm[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    curr_perm.append(num)
                    backtrack(counter, curr_perm, n)
                    curr_perm.pop()
                    counter[num] += 1
        
        # Count frequency of each number
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        result = []
        backtrack(counter, [], len(nums))
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1,1,2]))  # Output: [[1,1,2],[1,2,1],[2,1,1]]
    print(sol.permuteUnique([1,2,3]))  # Output: 6 unique permutations

