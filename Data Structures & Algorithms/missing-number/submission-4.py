class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=0
        sums = 0
        for num in nums:
            n+=1
            sums+=num
        return n*(n+1)//2-sums