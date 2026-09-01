class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set(nums)
        return len(dic) != len(nums)