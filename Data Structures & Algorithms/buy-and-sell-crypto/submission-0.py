class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #my brute force solution would be for each i
        # assume you buy on that day and to sell iterate and find max
        # of remaining in array. the diff is the best 
        # then among best take max again
        res = [0]
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = max(prices[i+1:])
            profit = sell - buy

            res.append(profit)

        return max(res)