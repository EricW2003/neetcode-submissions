class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol_list = []
        def aux(curr_list, nums_left):
            if nums_left == []:
                sol_list.append(curr_list)
                return 
            a = curr_list.copy()
            element = nums_left[-1]
            a.append(element)
            i = len(nums_left)-1
            while i>0 and nums_left[i-1]==nums_left[i]:
                i-=1
            aux(curr_list, nums_left[:i])
            aux(a,nums_left[:-1])
        nums.sort()
        aux([], nums)
        return sol_list