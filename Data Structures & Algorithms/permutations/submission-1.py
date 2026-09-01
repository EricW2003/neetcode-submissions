class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_sol = []
        def aux(curr_list, not_chosen_element):
            if not_chosen_element == []:
                all_sol.append(curr_list)
            for i in range(len(not_chosen_element)):
                a = curr_list.copy()
                not_chosen = not_chosen_element.copy()

                element = not_chosen_element[i]
                a.append(element)
                not_chosen = not_chosen_element.copy()
                not_chosen.pop(i)
                aux(a, not_chosen)
        aux([],nums)
        return all_sol
            