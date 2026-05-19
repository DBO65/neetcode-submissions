class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101
        l = 0

        for r in prices:
            if r < minPrice:
                minPrice = r
                l = r
            maxProfit = max(maxProfit, r-l)
            
        return maxProfit


        