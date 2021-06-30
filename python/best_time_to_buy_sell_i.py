class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        max = 0
        current_max = 0
        for i in range(1, len(prices)):
            if (prices[i] < prices[min] and i > min):
                min = i
                if (min >= max):
                    max = min
            if (prices[i] > prices[max] and i > max):
                max = i
            
            if (prices[max]-prices[min] > current_max):
                current_max = prices[max] - prices[min]
                
        return current_max