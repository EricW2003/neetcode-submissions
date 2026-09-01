class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for _ in range(len(nums))]

        pref=1
        suff=1

        for i in range(1,len(nums)):
            pref*=nums[i-1]
            res[i]*=pref
            suff*=nums[len(nums)-i]
            res[len(nums)-1-i]*=suff

        return res

