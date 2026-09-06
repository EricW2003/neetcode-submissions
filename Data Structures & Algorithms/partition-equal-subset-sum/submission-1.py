class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        def backtracking(s,remaining):
            if not remaining:
                return total-s == s
            
            if total-s==s:
                return True

            element = remaining.pop()
            copy = remaining.copy()
            return backtracking(s+element, copy) or backtracking(s,remaining)

        return backtracking(0,nums)
