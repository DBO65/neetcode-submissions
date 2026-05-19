class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, h = 0, 1
        sell = 0

        while h < len(prices):
            if prices[l] > prices[h]:
                l = h
            else:
                sell = max((prices[h] - prices[l]), sell)
            h += 1            

        return (sell)
