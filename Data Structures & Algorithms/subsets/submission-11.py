class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_sets = []
        def aux(curr_set, element_left):
            if element_left == []:
                return all_sets.append(curr_set)
            element = element_left.pop()
            a = curr_set.copy()
            b = element_left.copy()
            a.append(element)
            aux(curr_set.copy(), element_left)
            aux(a, b)
        aux([], nums)
        return all_sets