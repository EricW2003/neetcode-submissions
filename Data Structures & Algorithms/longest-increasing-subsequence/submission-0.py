class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1]*len(nums)
        max_val = 1
        # ans[i] longest strictly increasing subsequence starting at nums[i]
        # ans[i] = 1+max(ans[j]) for j>i such that nums[j]>nums[i]
        for i in range(len(nums)-2,-1,-1):
            num = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    ans[i] = max(ans[i],1+ans[j])
            max_val = max( max_val, ans[i])

        return max_val

