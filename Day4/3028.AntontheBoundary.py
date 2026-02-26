class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        from itertools import accumulate
        boundary_count = sum(cumulative_sum == 0 for cumulative_sum in accumulate(nums))
      
        return boundary_count
        
