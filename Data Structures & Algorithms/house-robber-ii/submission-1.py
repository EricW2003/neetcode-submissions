class Solution:
    def rob(self, nums: List[int]) -> int:
        def aux(nums):
            if len(nums)<3:
                return max(nums[0],nums[-1])

            nums[2]= nums[0]+nums[2]
            for i in range(3,len(nums)):
                nums[i] = nums[i]+max(nums[i-2],nums[i-3])

            return max(nums[-2],nums[-3])
        a = nums.copy()
        a.reverse()
        return max(aux(nums),aux(a))
