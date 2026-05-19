class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        substr = {}
        check = {}
        sol = ""
        have, need = 0, len(set(t))

        for i in t:
            substr[i] = substr.get(i, 0) + 1

        if len(t) > len(s) or not s or not t:
            return ""

        for rIdx, rVal in enumerate(s):
            if rVal in substr:
                check[rVal] = check.get(rVal, 0) + 1
                if check[rVal] == substr[rVal]:
                    have += 1
            
            while have == need:
                if not sol or len(sol) > rIdx - l + 1:
                    sol = s[l:rIdx + 1]

                if s[l] in substr: 
                    if check[s[l]] == substr[s[l]]:
                        have -= 1
                    check[s[l]] -= 1
                l += 1
                
        return sol