class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1 for _ in range(n)]
        pref=1
        suff=1
        for i in range(1,n):
            pref*=nums[i-1]
            res[i]*=pref
            suff*=nums[n-i]
            res[n-1-i]*=suff
        return res

