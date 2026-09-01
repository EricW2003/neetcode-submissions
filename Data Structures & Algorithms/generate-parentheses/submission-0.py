class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_sol = []

        def aux(curr_candidate, n_left, n_right):
            if n_left == 0 and n_right == 0:
                all_sol.append(curr_candidate)
                return
            if n_left >0:
                aux(curr_candidate+"(",n_left-1,n_right)
            if n_right > n_left:
                aux(curr_candidate+")",n_left,n_right-1)
        aux("",n,n)
        return all_sol