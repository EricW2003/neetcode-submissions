class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        upper_bound = len(nums)//2
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num]> upper_bound:
                return num