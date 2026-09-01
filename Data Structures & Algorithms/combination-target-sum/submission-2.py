class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol_list = []
        def aux(curr_list, curr_sum, nums_left):
            if nums_left == []:
                if curr_sum == target:
                    sol_list.append(curr_list)
                return 
            if curr_sum>target:
                return
            a = curr_list.copy()
            a.append(nums_left[-1])
            aux(curr_list, curr_sum,nums_left[:-1])

            aux(a, curr_sum+nums_left[-1],nums_left)

        aux([],0, nums)
        return sol_list