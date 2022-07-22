class Solution:
    def maxProfit(self, prices) -> int:
        l, r = 0, 1
        max_prof = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_prof = max(max_prof, profit)
            else:
                l = r
            r += 1

        return max_prof


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))