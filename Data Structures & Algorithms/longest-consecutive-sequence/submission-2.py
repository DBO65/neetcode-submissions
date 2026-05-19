from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums) 
        answer = 0
    
        for num in set_num:
            if num - 1 not in set_num:
                lcs = 1
                while num + 1 in set_num:
                    lcs += 1
                    num += 1
                answer = max(answer, lcs)
    
        return answer
        
        