class Solution:
    def isPalindrome(self, s: str) -> bool:
        safe_word = []

        for let in s.lower():
            if let.isalnum():
                safe_word.append(let)
        
        l_ptr = 0
        r_ptr = len(safe_word) - 1      
        while l_ptr < r_ptr:
            if safe_word[l_ptr] != safe_word[r_ptr]:
                return False
            l_ptr += 1
            r_ptr -= 1
        return True 

        