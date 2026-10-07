class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for num in nums:
            streak, curr = 0, num

            while curr in numSet:
                streak += 1
                curr += 1
            
            maxLen = max(maxLen, streak)
        
        return maxLen
        