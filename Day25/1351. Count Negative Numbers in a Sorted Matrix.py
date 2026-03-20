class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for lis in grid:
            for i in lis[::-1]:
                if i>=0:
                    break
                count+=1
        return count
        
