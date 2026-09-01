class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(x):
            n = len(x)
            for i in range(n//2):
                if x[i]!=x[n-1-i]:
                    return False
            return True
        
        all_sol = []

        def aux(curr_list, curr_word, letters_left):
            if letters_left == "":
                if is_palindrome(curr_word):
                    curr_list.append(curr_word)
                    all_sol.append(curr_list)
                return
            if is_palindrome(curr_word) and curr_word!="":
                a = curr_list.copy()
                a.append(curr_word)
                aux(a,"",letters_left)
            aux(curr_list, curr_word+letters_left[0],letters_left[1:])
        aux([],"",s)
        return all_sol