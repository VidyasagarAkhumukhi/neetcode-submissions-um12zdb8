class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]

                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


        # brute force Tc n2 sc 1
        # maxP = 0

        # for i in range(len(prices)):
        #     buyP = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sellP = prices[j]
        #         maxP = max(maxP, (sellP - buyP))
        
        # return maxP



