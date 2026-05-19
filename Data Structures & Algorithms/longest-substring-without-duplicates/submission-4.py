class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        lnrsub = 0
        length = 1
        nrsub = set()

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        while r < len(s):
            nrsub.add(s[l])
            if s[r] in nrsub:
                l += 1
                r = l 
                length = 1
                nrsub.clear()                
            else:
                nrsub.add(s[r]) 
                length += 1
            lnrsub = max(lnrsub, length)
            r += 1

        return lnrsub



        