class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for j in range(1,num+1):  
            digsum=0
            i=j
            while(i>0):
                digsum+=(i%10)
                i//=10
            if digsum%2==0:
                count+=1
        return count
        
