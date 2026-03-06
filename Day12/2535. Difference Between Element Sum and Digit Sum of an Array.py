class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_arr=sum(nums)
        sum_dig=0
        for i in nums:
            while(i>0):
                sum_dig+=(i%10)
                i//=10
        return abs(sum_arr-sum_dig)
                
