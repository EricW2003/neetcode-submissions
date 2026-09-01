class Solution:
    def isValid(self, s: str) -> bool:
        current_any={'(':0,'[':0,'{':0}
        conversion_dic={'}':'{',']':'[',')':'('}
        # first condition current_any >=0
        # second condition stack of the newest left of any should be the first to be closed
        stack=[]
        for letter in s:
            for left_any in ['(','{','[']:
                if letter==left_any:
                    stack.append(left_any)
                    current_any[letter]+=1
                pass
            for right_any in [')','}',']']:
                if letter==right_any:
                    if stack==[]:
                        return False
                    last_el=stack.pop()
                    if conversion_dic[letter]!=last_el:
                        return False
                    if current_any[last_el]==0:
                        return False
                    current_any[last_el]-=1
        return [0]*3==list(current_any.values())

                