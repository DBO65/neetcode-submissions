class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = [0]*26, [0]*26

        for let in s:
            sCount[ord(let)-ord('a')] += 1
        
        for let in t:
            tCount[ord(let)-ord('a')] += 1
        
        return sCount == tCount


        