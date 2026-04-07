class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []

        # cannot sell before buying 
        for i, price in enumerate(prices):
            max_profit_for_window = 0
        # iteratively add all the maximum profit of each subgroup
            for j in range(i+1, len(prices)):
                profit = prices[j] - price
                if profit > max_profit_for_window:
                    max_profit_for_window = profit
            profits.append(max_profit_for_window)

        # at the end, return max(profits)

        return max(profits)
