class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_f, perm_f= defaultdict(int), defaultdict(int)

        for ch in s1:
            s1_f[ch] += 1

        l = 0
        max_l = len(s1)

        for r in range(len(s2)):
            perm_f[s2[r]] += 1

            if r - l + 1 > max_l:
                perm_f[s2[l]] -= 1
                if perm_f[s2[l]] == 0:
                    del perm_f[s2[l]]
                l += 1

            if r - l + 1 == max_l and perm_f == s1_f:
                return True

        return False
