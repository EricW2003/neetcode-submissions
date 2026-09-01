class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums[0],nums[-1])

        nums[2]= nums[0]+nums[2]
        for i in range(3,len(nums)):
            nums[i] = nums[i]+max(nums[i-2],nums[i-3])
            # if the ith house i robbed I can't rob the house i-1
            # Also, if I don't rob i-2 AND i-3, I'm missing on gains
            # Hence, I need to rob at least i-2 or i-3 (but I can't rob both !!!)
        return max(nums[-1],nums[-2])
        