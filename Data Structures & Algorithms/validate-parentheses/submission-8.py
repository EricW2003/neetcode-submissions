class Solution:
    def isValid(self, s: str) -> bool:
        conversion_dic={'}':'{',']':'[',')':'('}
        # first condition current_any >=0
        # second condition stack of the newest left of any should be the first to be closed
        stack=[]
        for letter in s:
            if letter in conversion_dic.values():
                stack.append(letter)
            else:
                if stack==[]:
                    return False
                if conversion_dic[letter]!=stack.pop():
                    return False
        return stack==[]

                