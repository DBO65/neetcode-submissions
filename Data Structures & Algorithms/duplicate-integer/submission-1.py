class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = []
        for n in range(len(nums)-1):
            checker.append(nums[n])
            if nums[n+1] in checker:
                return True
        return False
        