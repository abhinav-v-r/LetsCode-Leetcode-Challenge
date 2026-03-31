class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum=sum(nums[:k])
        max_sum=temp_sum

        for i in range(k,len(nums)):
            temp_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,temp_sum)
        return max_sum/k
            
