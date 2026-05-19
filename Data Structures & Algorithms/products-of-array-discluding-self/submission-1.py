class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1]*len(nums)
        
        mult = 1
        for idx in range(len(nums) - 1):
            mult *= nums[idx] 
            sol[idx + 1] *= mult if idx + 1 < len(nums) + 1 else sol[idx]
        
        mult = 1
        for idx in range(len(nums) - 1, 0, -1):
            mult *= nums[idx] 
            sol[idx - 1] *= mult if idx - 1 > -1 else sol[idx]
        
        return sol


            
            
            

       
            

        