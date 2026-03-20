class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag=0;
        max_area=0;
        for rectangle in dimensions:
            diag=(rectangle[0]**2)+(rectangle[1]**2)
            area=rectangle[0]*rectangle[1]
            if diag>max_diag:
                max_diag=diag
                max_area=area
            elif diag==max_diag:
                max_area=max(max_area,area)
        return max_area
                
            
            
        
