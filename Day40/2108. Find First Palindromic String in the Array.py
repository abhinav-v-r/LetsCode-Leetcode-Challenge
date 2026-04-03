class Solution:
    def checkPalindrome(self,word):
        return word==word[::-1]
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.checkPalindrome(word):
                return word
        return ""
        
