class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        dig_sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                dig_sum+=i
                if i!=num//i:
                    dig_sum+=num//i
        return dig_sum==num
                
            
        
