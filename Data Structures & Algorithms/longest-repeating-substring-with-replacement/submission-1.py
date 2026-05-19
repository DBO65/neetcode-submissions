class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        lrcr = 0 
        count = defaultdict(int)
        l = 0 

        for r in range(len(s)):
            count[s[r]] += 1 

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            lrcr = max(lrcr, r - l + 1)

        return lrcr




        
        

        