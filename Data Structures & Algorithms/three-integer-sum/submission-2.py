class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    sol.append([nums[j], nums[k], nums[i]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    j += 1
        return sol
        