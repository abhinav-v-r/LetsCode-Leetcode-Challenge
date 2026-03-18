class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set=set(nums)
        while True:
            if original in num_set:
                original=original << 1
            else:
                return original
        
