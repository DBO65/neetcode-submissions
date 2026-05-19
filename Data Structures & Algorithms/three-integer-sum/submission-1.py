class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1] :
                continue
            
            m_ptr, r_ptr = i + 1, len(nums)-1
            while m_ptr < r_ptr:
                threes = (a + nums[m_ptr] + nums[r_ptr])
                if threes < 0:
                    m_ptr += 1
                elif threes > 0:
                    r_ptr -= 1
                else:
                    sol.append([a, nums[m_ptr], nums[r_ptr]])   
                    m_ptr += 1
                    while nums[m_ptr] == nums[m_ptr-1] and m_ptr < r_ptr:
                        m_ptr += 1
        return sol

