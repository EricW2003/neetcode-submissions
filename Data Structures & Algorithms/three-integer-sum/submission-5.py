class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        for k in range(len(nums)):
            target = -nums[k]
            dic ={}
            for i in range(len(nums)):
                if i!=k:
                    if target-nums[i]  in dic:
                        j = dic[target-nums[i]]

                        duplicate = False
                        for element in triplet:
                            duplicate =duplicate or set(element) == set([nums[k],nums[j],nums[i]])
                        if not duplicate:
                            triplet.append([nums[k],nums[j],nums[i]])
                    dic[nums[i]] = i
        return triplet