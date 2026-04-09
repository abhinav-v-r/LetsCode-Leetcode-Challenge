import math as mt
class Solution:
    def numberOfMatches(self, n: int) -> int:
        match=0
        while(n>1):
            if n%2==0:
                match+=(n/2)
                n/=2
            else:
                match+=mt.floor(n/2)
                n=mt.ceil(n/2)
        return int(match)
            
            
            
            
        
