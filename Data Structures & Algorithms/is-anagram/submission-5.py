class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for let in s:
            s_map[let] = s_map.get(let, 0) + 1 
        
        for letr in t:
            t_map[letr] = t_map.get(letr, 0) + 1 
        
        return s_map == t_map

        
                





        