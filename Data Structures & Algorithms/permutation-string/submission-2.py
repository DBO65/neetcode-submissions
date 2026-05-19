class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_f, perm_f = defaultdict(int), defaultdict(int)

        if len(s1) > len(s2):
            return False

        for let in s1:
            s1_f[let] += 1

        for l in range(len(s2)-len(s1) + 1):
            r = l + len(s1) - 1
            for i in range(len(s1)):
                perm_f[s2[l + i]] += 1
            if perm_f == s1_f:
                return True 
            else:
                perm_f.clear()   
        return False
        
            
        