class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum += num
            best_sum = max(best_sum, curr_sum)
            curr_sum = max(curr_sum,0)
        
        return best_sum
