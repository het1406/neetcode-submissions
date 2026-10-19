class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0 
        for i in range(len(prices)): 
            profit = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            
            if profit > max_profit:
                max_profit = profit 
        return max_profit 

        