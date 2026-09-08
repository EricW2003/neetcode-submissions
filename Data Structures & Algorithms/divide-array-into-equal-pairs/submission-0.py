class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] = (dic[num]+1)%2
            else:
                dic[num] = 1
        for n in dic.values():
            if n!=0:
                return False
        return True