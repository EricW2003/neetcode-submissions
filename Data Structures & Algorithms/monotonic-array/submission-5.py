class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return True
        
        start, end = nums[0], nums[-1]

        sign = end - start
        if sign ==0:
            for i in range(1,len(nums)-1):
                if nums[i]!=start:
                    return False
        else:
            for i in range(len(nums)-1):
                if sign*(nums[i+1]-nums[i])<0:
                    return False
        return True
