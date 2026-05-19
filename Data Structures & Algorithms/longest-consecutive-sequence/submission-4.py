class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numbers = set(nums)
        maxCount = 1 

        for num in nums:
            count = 1
            if num - 1 not in numbers:
                while num + 1 in numbers:
                    count += 1
                    num += 1  
            maxCount = max(maxCount, count)
        
        return maxCount


        