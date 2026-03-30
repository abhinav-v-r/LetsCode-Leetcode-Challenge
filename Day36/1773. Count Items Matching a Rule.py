class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=='type':
            k=0
        elif ruleKey=='color':
            k=1
        else:
            k=2
        for categ in items:
            if categ[k]==ruleValue:
                count+=1
        return count
            
                
            
        
