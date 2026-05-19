class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0 
        r_ptr = len(numbers) - 1
        s = 0

        while l_ptr < len(numbers) - 1:
            if l_ptr == r_ptr:
                l_ptr += 1
                r_ptr = len(numbers) - 1 
            if l_ptr < r_ptr:
                if numbers[l_ptr] + numbers[r_ptr] == target:
                    return [l_ptr + 1, r_ptr + 1]
            r_ptr -= 1
        