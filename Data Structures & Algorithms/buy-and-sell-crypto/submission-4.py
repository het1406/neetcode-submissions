class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices2 = [0]
        for i in range(len(prices)):
            for n in range(i+1,len(prices)):
                if prices[n]-prices[i] > max(prices2):
                    prices2.append(prices[n]-prices[i])
                
        return max(prices2)
        