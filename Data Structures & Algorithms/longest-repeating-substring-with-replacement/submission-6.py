class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Repeating character - freq <= k 
        l = 0
        count = {}
        lrcr = 0

        for rIdx, rVal in enumerate(s):
            count[rVal] = count.get(rVal, 0 ) + 1

            while rIdx - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            lrcr = max(lrcr, rIdx - l + 1)
        
        return lrcr



        