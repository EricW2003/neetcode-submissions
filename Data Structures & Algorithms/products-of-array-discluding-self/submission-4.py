class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1 for _ in range(n)]
        suffix=[1 for _ in range(n)]
        pref=1
        suff=1
        for i in range(1,n):
            pref*=nums[i-1]
            prefix[i]=pref
            j=n-1-i
            suff*=nums[j+1]
            suffix[j]=suff

        for k in range(n):
            suffix[k]*=prefix[k]
        return suffix

