class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        max_profit = 0 
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                if profit>max_profit:
                    max_profit = profit

        if max_profit > 0:
            return max_profit 
        else:
            return 0 