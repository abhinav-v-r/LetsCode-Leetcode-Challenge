class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hori=0
        verti=0
        for i in moves:
            if i=='U':
                verti+=1
            elif i=='D':
                verti-=1
            elif i=='L':
                hori-=1
            elif i=='R':
                hori+=1
        return (verti==0 and hori==0)
        
