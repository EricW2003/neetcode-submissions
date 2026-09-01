class Solution:

    def encode(self, strs: List[str]) -> str:
        all_str = ""
        for string in strs:
            size = len(string)
            all_str += str(size)+"#"+string
        return all_str
    def decode(self, s: str) -> List[str]:
        list_str = []
        curr = ""
        i = 0
        while i < len(s):
            digit = ""
            while s[i].isdigit():
                digit += s[i]
                i+=1
            size = int(digit)
            i+=1
            for j in range(size):
                curr+=s[i]
                i+=1
            list_str.append(curr)
            curr = ""
        return list_str
            

