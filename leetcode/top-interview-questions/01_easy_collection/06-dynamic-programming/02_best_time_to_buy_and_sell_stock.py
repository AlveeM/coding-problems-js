class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        
        minStock = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < minStock:
                minStock = prices[i]
                continue
            profit = max(prices[i] - minStock, profit)
        
        return profit