class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)

        for i in range(len(nums)):
            index = n-1-i
            num = nums[index]
            if num == val:
                k+=1

        for _ in range(k):
            nums.remove(val)  
        ans = n - k
        return ans