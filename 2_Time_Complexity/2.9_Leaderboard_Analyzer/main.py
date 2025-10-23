# Leaderboard Analyzer
# Topic: Time & Space Complexity
# Type: Home Challenge

class Solution:
    def leaderboard(self, scores: list[int]) -> None:
        # Find highest score - O(n)
        highest = max(scores)
        
        # Compute average - O(n)
        avg = sum(scores) / len(scores)
        
        # Count above average - O(n)
        above_avg = sum(1 for score in scores if score > avg)
        
        # Sort in descending order - O(nlogn)
        rank_list = sorted(scores, reverse=True)
        
        # Print results
        print(f"Highest Score: {highest}")
        print(f"Average Score: {avg}")
        print(f"Students Above Average: {above_avg}")
        print(f"Rank List: {rank_list}\n")

# Demo
if __name__ == '__main__':
    sol = Solution()
    sol.leaderboard([50,70,90,60,80])
    sol.leaderboard([30,30,30])
    sol.leaderboard([100,40,60,80])

