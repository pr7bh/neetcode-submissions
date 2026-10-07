class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        best = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price-minPrice
                if profit > best:
                    best = profit
        return best
        