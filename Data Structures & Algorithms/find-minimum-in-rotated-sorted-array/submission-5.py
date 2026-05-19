class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        sol = nums[0]

        if not nums:
            ret

        while l <= r:
            mid = (l+r) // 2

            if l == r:
                return nums[l]

            elif nums[l] > nums[r] and nums[mid] <  nums[r]:
                r = mid 
            elif nums[l] > nums[r] and nums[mid] > nums[r]:
                l = mid + 1
            elif nums[l] < nums[r]:
                sol = min(sol, nums[l])
                break

        return sol

        