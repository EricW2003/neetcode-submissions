class Solution:
    def digit(self,n):
        res=0
        while n>0:
            res+=(n%10)**2
            n=n//10
        return res
    def isHappy(self, n: int) -> bool:
        L=[]
        def aux(k):
            if k==1:
                return True
            new_val=self.digit(k)
            if new_val in L:
                return False
            L.append(new_val)
            return aux(new_val)
        return aux(n)

            