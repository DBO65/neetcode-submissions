class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1
        check = [0]*26
        window = [0]*26 

        for i in s1:
            check[ord(i) - ord('a')] += 1 

        for j in s2[l:r]:
            window[ord(j) - ord('a')] += 1 

        while r < len(s2):
            window[ord(s2[r]) - ord('a')] += 1 

            if window == check:
                return True
            
            window[ord(s2[l]) - ord('a')] -= 1 
            l += 1
            r += 1

        return False


        
        