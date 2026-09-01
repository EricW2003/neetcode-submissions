class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=nums[r]:
                if target<=nums[r] and nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
            else:
                if target>=nums[l] and nums[mid]>=target:
                    r=mid
                else:  
                    l=mid+1
            print(l,r)
        if nums[l]!=target:
            return -1

        return l