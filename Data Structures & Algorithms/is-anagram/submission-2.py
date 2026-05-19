class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in range(len(t)) :
            if s[0] not in t:
                return False
            x = t.find(s[0])
            s = s[1:]
            t = t[:x] + t[x + 1:]
        return True
                
                





        