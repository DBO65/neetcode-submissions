class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        i = 0

        while i < len(nums):
            diff = target - nums[i]
            if diff in sumMap:
                return [sumMap[diff], i]
            sumMap[nums[i]] = i
            i += 1
