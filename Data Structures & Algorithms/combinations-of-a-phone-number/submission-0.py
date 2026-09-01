class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def aux(curr_word, digit_left):
            if digit_left =="":
                if curr_word!="":
                    ans.append(curr_word)
                return
            
            for letter in dic[digit_left[0]]:
                aux(curr_word+letter,digit_left[1:])
        aux("",digits)
        return ans
