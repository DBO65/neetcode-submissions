class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += str(length) + '@' + word
        
        return string
            


    def decode(self, s: str) -> List[str]:
        i = 0 
        sol =[]

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            i = j + 1 
            sol.append(s[i: length + i])
            i = length + i

        return sol
        
