from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num=max(nums)
        min_num=min(nums)
        return gcd(max_num,min_num)
        
