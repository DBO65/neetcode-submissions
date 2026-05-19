class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in s:
            sMap[i] = sMap.get(i, 0) + 1
        
        for j in t:
            tMap[j] = tMap.get(j, 0) + 1

        return tMap == sMap

        
