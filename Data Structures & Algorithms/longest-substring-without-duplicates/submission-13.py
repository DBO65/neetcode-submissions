class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        check = set()
        l = 0
        subStr = 1

        for rIdx, r in enumerate(s):
            while r in check:
                check.remove(s[l])
                l += 1 

            subStr = max(subStr, rIdx - l + 1)
            check.add(r)
        
        return subStr


        