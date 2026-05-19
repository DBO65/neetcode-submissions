class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for let in s:
            sMap[let] = sMap.get(let, 0) + 1
        
        for let in t:
            tMap[let] = tMap.get(let, 0) + 1
    
        return tMap == sMap

        
                





        