class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            j = n - i
            if '0' in str(i) or '0' in str(j):
                continue
            return [i, j]
