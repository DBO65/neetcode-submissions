from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set()
        seq = {} 
        cs = 0

        if len(nums) == 0:
            return 0

        for number in nums:
            set_num.add(number)
    
        for num in set_num:
            if num - 1 not in set_num:
                seq[cs] = 1
                while num + 1 in set_num:
                    seq[cs] += 1
                    num += 1
                cs += 1

        answer = seq[0]
        for i in seq:
            if seq[i] > answer:
                answer = seq[i]
        
        return answer
        
        