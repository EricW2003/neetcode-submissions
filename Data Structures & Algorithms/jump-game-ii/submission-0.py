class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            min_step = float("inf")
            n = nums[i]
            for j in range(i+1,min(i+n+1,len(nums))):
                if nums[j] +1 <min_step:
                    min_step = nums[j] + 1
            nums[i] = min_step
        print(nums)
        return nums[0]

