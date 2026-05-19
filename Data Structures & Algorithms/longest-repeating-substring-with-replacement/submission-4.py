class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = s[0]
        sol = 0
        l = 0

        for rIdx, rVal in enumerate(s):
            count[rVal] = count.get(rVal, 0) + 1

            while (rIdx - l + 1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1

            sol = max(sol, rIdx - l + 1)

        return sol






        
        

        