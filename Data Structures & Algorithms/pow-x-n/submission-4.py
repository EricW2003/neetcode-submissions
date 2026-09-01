class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        val=1
        if x==0 and n==0:
            return 1
        pos_n=abs(n)
        curr_pow=x
        while pos_n>0:
            if pos_n%2:
                val*=curr_pow
            curr_pow*=curr_pow
            pos_n=pos_n//2

        if n<0:
            val=1.0/val
        return val