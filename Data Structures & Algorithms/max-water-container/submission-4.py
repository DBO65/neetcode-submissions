class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        sol = 0 


        while l < r:
            cont = (r-l)*min(heights[r],heights[l])
            sol = max(cont, sol)

            if heights[l] <= heights [r]:
                l += 1
            else:
                r -= 1

        return sol
        