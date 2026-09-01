class Solution:
    def sign(self,n):
        if n>=0:
            return 1
        else:
            return -1
    def myPow(self, x: float, n: int) -> float:
        val=1
        if x==0 and n==0:
            return 1
        sign_n=self.sign(n)
        pos_n=sign_n*n
        
        for _ in range(pos_n):
            val*=x
        if sign_n==-1:
            val=1.0/val
        return val