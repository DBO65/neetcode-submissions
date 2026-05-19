class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0 
        r_ptr = len(numbers) - 1

        while l_ptr < r_ptr:
            tot = numbers[l_ptr] + numbers[r_ptr]
            if tot == target:
                return [l_ptr + 1, r_ptr + 1]
            elif tot < target:
                l_ptr += 1
            else:
                r_ptr -= 1

        