class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sol = ""
        l, have, need = 0, 0, len(set(t))
        check = {}
        window = {}

        if not t or not s or len(t) > len (s):
            return sol
         
        for i in t:
            check[i] = check.get(i, 0) + 1


        for rIdx, rVal in enumerate(s):
            #Expands window
            if rVal in check:
                window[rVal] = window.get(rVal, 0) + 1
                if window[rVal] == check[rVal]:
                    have += 1

            #Contracts window
            while have == need:
                if not sol or rIdx - l + 1 < len(sol):
                    sol = s[l:rIdx + 1]

                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < check[s[l]]:
                        have -= 1

                l += 1

        return sol







        