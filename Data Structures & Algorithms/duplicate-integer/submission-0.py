class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for item in nums:
            if item in dic:
                return True
            else:
                dic[item]="in"
        return False