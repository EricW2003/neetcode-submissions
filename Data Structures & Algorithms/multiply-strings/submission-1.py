class Solution:
    def str_to_int(self,num):
        res=0
        for letter in num:
            res=res*10+ord(letter)-ord("0")
        return res
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.str_to_int(num1)*self.str_to_int(num2))