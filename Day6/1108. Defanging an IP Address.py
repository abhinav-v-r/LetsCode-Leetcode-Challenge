class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_ip=address.replace('.','[.]')
        return new_ip
