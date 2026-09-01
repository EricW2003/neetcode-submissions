class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        for i, num in enumerate(nums):
            if num-1 not in nums:
                k = 1
                while num+k in nums:
                    k +=1
                max_length = max(max_length, k)
        return max_length
