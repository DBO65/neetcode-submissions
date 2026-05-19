class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = [0]*52

        for i in s:
            letterMap[ord(i) - ord('a')] += 1 
        
        for j in t:
            letterMap[ord(j) - ord('a') + 26] += 1 

        return letterMap[:26] == letterMap[26:]

        
