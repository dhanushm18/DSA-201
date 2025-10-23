# Logarithmic Time (O(logn))
**Topic:** Time & Space Complexity

**Type:** In-Session



Statement: Given a number n, divide it by 2 until it becomes 1. Print the number of steps. 

Constraints: 1 ≤ n ≤ 10^9 

Time Complexity: O(log n) 

Space Complexity: O(1) 

Test Cases: 

Input: n=16 → Output: 4 

Input: n=8 → Output: 3 

Input: n=1 → Output: 0 

Input: n=100 → Output: 6 

## Time Complexity
O(log n)

## Space Complexity
O(1)

## Approach
Each step divides n by 2, counting how many steps until n equals 1. This is because dividing repeatedly by 2 halves the number each time, so the total steps are approximately log base 2 of n.

