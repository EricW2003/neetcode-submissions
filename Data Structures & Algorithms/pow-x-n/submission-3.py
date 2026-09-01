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
        
        # for _ in range(pos_n):
        #     val*=x

        curr_pow=x
        while pos_n>0:
            if pos_n%2:
                val*=curr_pow
            curr_pow*=curr_pow
            pos_n=pos_n//2
        if sign_n==-1:
            val=1.0/val
        return val