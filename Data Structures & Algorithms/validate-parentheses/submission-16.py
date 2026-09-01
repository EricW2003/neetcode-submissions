
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversion_dic = {"(":")", "[": "]", "{" : "}"}
        for letter in s:
            print(stack)
            if letter in "{[(":
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if conversion_dic[a]!=letter:
                    return False
        return len(stack) == 0
