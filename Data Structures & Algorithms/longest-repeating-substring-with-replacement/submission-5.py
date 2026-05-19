class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = s[0]
        sol = 0
        l = 0

        for rIdx, rVal in enumerate(s):
            count[rVal] = count.get(rVal, 0) + 1

            if count[rVal] >= count[maxFreq]:
                maxFreq = rVal

            while (rIdx - l + 1) - count[maxFreq] > k:
                count[s[l]] = count.get(s[l]) - 1

                if count[rVal] >= count[maxFreq]:
                    maxFreq = rVal

                l += 1

            sol = max(sol, rIdx - l + 1)

        return sol






        
        

        