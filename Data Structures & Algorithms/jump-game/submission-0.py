class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_min_index = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=curr_min_index:
                curr_min_index = i
        return curr_min_index == 0