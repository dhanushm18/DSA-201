# Power of Four
# Topic: Recursion
# Type: Home Challenge

class Solution:  
    def isPowerOfFour(self, n: int) -> bool:  
        # Implement using recursion  
        if n==1:
            return True
        if n<=0 or n%4 !=0:
            return False
        
        return self.isPowerOfFour(n//4) 
# Demo 
if __name__ == '__main__':
    sol = Solution() 
    print(sol.isPowerOfFour(1))   
    print(sol.isPowerOfFour(16))   
    print(sol.isPowerOfFour(8))   
    print(sol.isPowerOfFour(0))    
    print(sol.isPowerOfFour(-4))  