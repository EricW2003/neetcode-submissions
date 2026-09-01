class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for k in range(n-1,0,-1):
            if nums[k]==nums[k-1]:
                nums.pop(k)
        return n