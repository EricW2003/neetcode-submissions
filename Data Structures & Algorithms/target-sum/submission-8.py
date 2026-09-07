class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        ans = [{i:0 for i in range(-s,s+1)} for _ in range(len(nums)+1)]
        ans[0][0] = 1
        min_val = max_val = 0
        for i in range(len(nums)):
            num = nums[i]
            for j in range(min_val,max_val+1):
                ans[i+1][j+num] += ans[i][j]
                ans[i+1][j-num] += ans[i][j]
            min_val-=num
            max_val+=num
        return ans[-1][target]
