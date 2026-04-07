class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimise buying price
        minSoFar = prices[0]   
        max_profit = 0
        # maximise selling price
        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            max_profit = max(max_profit, prices[i]-minSoFar)

        return max_profit