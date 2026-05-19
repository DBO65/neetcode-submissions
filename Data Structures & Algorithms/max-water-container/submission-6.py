class Solution:
    def maxArea(self, heights: List[int]) -> int:
        minHeight = maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            minHeight = min(heights[l], heights[r])
            maxArea = max(minHeight*(r-l), maxArea)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return maxArea

        