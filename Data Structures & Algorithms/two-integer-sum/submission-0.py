class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_num_Map = {}  # Value -> index pair

        for i, n in enumerate(nums):    # i and n stands for index an number respectively 
            diff = target - n
            if diff in prev_num_Map:
                return [prev_num_Map[diff], i]
            prev_num_Map[n] = i
        
        return prev_num_Map
        