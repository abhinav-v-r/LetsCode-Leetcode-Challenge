class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count=0
        count=0
        for sent in sentences:
            count=sent.count(" ")+1
            max_count=max(count,max_count)
        return max_count
            
        
