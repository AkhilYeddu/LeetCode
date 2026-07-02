class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        n = len(prices)
        sell = prices[n -1]
        for i in range(n - 2, -1, -1):  # start, stop, step
            buy = prices[i]
            if sell - buy < 0:
                sell = buy
            elif sell - buy > 0:
                profit = max(profit, sell - buy)
        return profit
