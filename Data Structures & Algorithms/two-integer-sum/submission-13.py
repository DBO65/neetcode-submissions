class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for idx, num in enumerate(nums):
            diff = target - num 
            if diff in numMap:
                return [numMap[diff], idx]
            numMap[num] = idx

        