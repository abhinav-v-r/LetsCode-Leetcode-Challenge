class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        sum_=0
        while(n>0):
            sum_+=(n%10)
            prod*=(n%10)
            n//=10
        return prod-sum_
            
