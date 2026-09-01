class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol_list = []
        def aux(curr_list, curr_sum, nums_left):
            if nums_left == []:
                if curr_sum == target:
                    sol_list.append(curr_list)
                return 
            if curr_sum>target:
                return
            a = curr_list.copy()
            element = nums_left[-1]
            a.append(element)
            i = len(nums_left)-1
            while i>0 and nums_left[i-1]==nums_left[i]:
                i-=1
            aux(curr_list, curr_sum,nums_left[:i])

            aux(a, curr_sum+nums_left[-1],nums_left[:-1])
        candidates.sort()
        aux([],0, candidates)
        return sol_list