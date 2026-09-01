class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()
        for k in range(len(nums)):
            if k==0 or (k>0 and nums[k]!=nums[k-1]):
                i = k+1
                j = len(nums)-1
                while k<i and i<j:
                    res = nums[i]+nums[j]+nums[k]
                    if res >0:
                        j-=1
                    elif res< 0:
                        i+=1
                    else:
                        triplet.append([nums[i], nums[j], nums[k]])
                        j-=1
                        i+=1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
        return triplet