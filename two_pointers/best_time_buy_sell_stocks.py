class Solution:
    def maxProfit(self, prices) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                currentProfit = prices[r] - prices[l]
                maxP = max(maxP, currentProfit)
            else:
                l = r
            r += 1

        return maxP
