class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [0]*(2*n)
        for i,num in enumerate(nums):
            L[i] = num
            L[i+n] = num
        return L