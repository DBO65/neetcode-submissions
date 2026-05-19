class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
                return False
        
        check = [0]*26
        l = 0
        r = len(s1) - 1
        window = [0]*26

        for i in s1:
            check[ord(i) - ord('a')] += 1

        for j in s2[0:r]:
            window[ord(j) - ord('a')] += 1

        while r < len(s2):
            window[ord(s2[r]) - ord('a')] += 1
            if window == check:
                return True
            else:
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
        return False
            
            
