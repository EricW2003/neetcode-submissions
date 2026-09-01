
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversion_dic = {")":"(", "]": "[", "}" : "{"}
        for letter in s:
            if letter in "{[(":
                stack.append(letter)
            else:
                if not stack or conversion_dic[letter]!= stack.pop():
                    return False
        return len(stack) == 0
