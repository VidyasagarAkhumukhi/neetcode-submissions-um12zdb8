class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        for i in range(len(prices)):
            buyP = prices[i]
            for j in range(i + 1, len(prices)):
                sellP = prices[j]
                maxP = max(maxP, (sellP - buyP))
        
        return maxP



