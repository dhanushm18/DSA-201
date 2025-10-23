# Cubic Time (O(n³))
# Topic: Time & Space Complexity
# Type: Home Challenge

class Solution:
    def allTriplets(self, arr: list[int]) -> list[tuple[int,int,int]]:
        result = []
        for i in arr:
            for j in arr:
                for k in arr:
                    result.append((i,j,k))
        return result

# Demo
if __name__ == '__main__':
    sol = Solution()
    print(sol.allTriplets([1,2,3]))  # 27 triplets
    print(sol.allTriplets([4,5]))    # 8 triplets
    print(sol.allTriplets([9]))      # 1 triplet

