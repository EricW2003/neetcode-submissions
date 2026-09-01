class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr_digit=digits[-1]
        pointer=len(digits)-1
        loop=True
        while loop and pointer>=0:
            if digits[pointer]!=9:
                loop=False
            digits[pointer]=(digits[pointer]+1)%10
            pointer-=1
        if digits[pointer+1]==0:
            return [1]+digits
        return digits
