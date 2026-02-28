from math import gcd
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n=gcd(a,b)
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        return count
        
