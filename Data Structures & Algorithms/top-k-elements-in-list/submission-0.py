class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        top_set = set()

        for num in nums:
            if num not in top_set:
                if len(top_set)<k:
                    top_set.add(num)
                else:
                    for remove_key in top_set:
                        if dic[remove_key]<dic[num]:
                            top_set.remove(remove_key)
                            top_set.add(num)
                            break
        
        return list(top_set)
                