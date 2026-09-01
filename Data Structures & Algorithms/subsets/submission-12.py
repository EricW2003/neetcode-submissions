class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_sets = []
        def aux(curr_set, element_left):
            if element_left == []:
                return all_sets.append(curr_set)
            a = curr_set.copy()
            b = element_left.copy()
            a.append(element_left[-1])
            aux(curr_set.copy(), element_left[:-1])
            aux(a, element_left[:-1])
        aux([], nums)
        return all_sets