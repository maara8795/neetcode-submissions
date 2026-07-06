class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        for i in range(len(prices)):
            j = i+1
            while j<len(prices):
                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
                j+=1
        return maxP