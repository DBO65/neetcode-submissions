class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        area = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if lMax - height[l] > 0:
                    area += lMax - height[l]
                lMax = max(lMax, height[l])
            else:
                r -= 1
                if rMax - height[r] > 0:
                    area += rMax - height[r]
                rMax = max(rMax, height[r])
        
        return area
            

        