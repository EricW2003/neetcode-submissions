class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for k in range(len(nums)-1,0,-1):
            if nums[k]==nums[k-1]:
                nums.pop(k)
        return len(nums)