class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_map = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in ans_map:
                return [ans_map[diff], idx]
            ans_map[num] = idx

        





        