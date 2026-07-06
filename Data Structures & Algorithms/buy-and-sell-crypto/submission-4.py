class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        l = 0 
        r = 1
        maxp = 0
        while(r<len(prices)):

            if prices[r] - prices[l] > 0 :
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r+=1
        return maxp
        # maxP = 0

        # for i in range(len(prices)):
        #     j = i+1 
        #     while j<len(prices):
        #         profit = prices[j]-prices[i]
        #         maxP = max(maxP, profit)
        #         j+=1

        # return maxP
                
                