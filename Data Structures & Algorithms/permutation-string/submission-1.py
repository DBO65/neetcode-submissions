class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        s1_f, perm_f = defaultdict(int), defaultdict(int)

        if len(s1) > len(s2):
            return False

        for let in s1:
            s1_f[let] += 1

        for r in range(len(s2)):
            if r - l + 1 == len(s1):
                temp_l = l
                while temp_l <= r:
                    perm_f[s2[temp_l]] += 1
                    temp_l += 1
                if perm_f == s1_f:
                    return True 
                else:
                    perm_f.clear()
                    l += 1    
        return False
        
            
        