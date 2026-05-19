class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_map = {}

        for i, n in enumerate(nums):
            sol_map[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sol_map and sol_map[diff] != i: 
                return [i, sol_map[diff]]


        