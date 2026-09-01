class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums[0],nums[-1])
        res = [-1]*len(nums)
        # res[i] maximum money I can rob if I was given only nums[:i+1] as the list
        # and nums[i] is among the robbed houses !

        #Dynamic programming
        res[0]= nums[0]
        res[1]= nums[1]
        for i in range(2,len(nums)):
            res[i] = nums[i]+max(res[i-2],res[i-3])
            # if the ith house i robbed I can't rob the house i-1
            # Also, if I don't rob i-2 AND i-3, I'm missing on gains
            # Hence, I need to rob at least i-2 or i-3 (but I can't rob both !!!)
        print(res)
        return max(res[-1],res[-2])
        