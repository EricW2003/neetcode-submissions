class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        dic = {}
        for word in words:
            for letter in word:
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] += 1
        print(dic)
        for key in dic:
            if dic[key] % n != 0:
                return False
        return True