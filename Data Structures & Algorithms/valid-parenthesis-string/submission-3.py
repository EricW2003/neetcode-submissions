class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = right_count =0
        for letter in s:
            if letter == "(":
                left_count+=1
                right_count+=1

            elif letter == ")":
                left_count-=1
                right_count-=1
            else:
                left_count-=1
                right_count+=1
            left_count = max(0, left_count)
            if right_count<0:
                return False
        # count -> left_count and a right count, set both to 0 

        # count = a I have a "*" count -> left_count and a right_count

        return left_count<=0<=right_count