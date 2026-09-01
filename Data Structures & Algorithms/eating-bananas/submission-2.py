class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the reverse problem is given k in how many hours h at minimum I can eat all bananas
        # it is decreseing in k so
        # and k is bounded above by maxval of piles as if it higher h=len(piles)
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            s=0
            for val in piles:
                s+=self.ceiling(float(val)/mid)
            s=int(s)
            if s<=h:
                r=mid
            else:
                l=mid+1
        return l
    def ceiling(self,x):
        n=int(x)
        if x-n>0:
            n+=1
        return n
