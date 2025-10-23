# Recursive Sum of Digits Until One
# Topic: Recursion
# Type: In-Session
class Solution:  
    def recursiveDigitSum(self, n: int) -> int:  
        # Implement using recursion  
        if n < 10:
            return n
        
        sum=0
        while n > 0:
            sum=sum+(n%10)
            n=n//10
        
        
             
        return self.recursiveDigitSum(sum)
# Demo   
if __name__ == '__main__':
    sol = Solution() 
    print(sol.recursiveDigitSum(9875))   
    print(sol.recursiveDigitSum(1234))   
    print(sol.recursiveDigitSum(5)) 
