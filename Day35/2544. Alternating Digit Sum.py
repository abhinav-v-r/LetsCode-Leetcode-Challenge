class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=-1
        sum=0
        n=int((str(n)[::-1]))
        while(n>0):
            s=-1*s
            sum+=(n%10)*s
            n=n//10
        return sum
            
            
            
        
