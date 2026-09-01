class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        if x==0 and n==0:
            return 1

        val=1  
        pos_n=abs(n)
        while pos_n>0:
            if pos_n%2:
                val*=x
            x*=x
            pos_n=pos_n//2

        if n<0:
            val=1.0/val
        return val