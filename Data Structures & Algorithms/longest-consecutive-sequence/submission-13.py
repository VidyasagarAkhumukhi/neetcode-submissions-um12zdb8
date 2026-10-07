class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #brute force TC n2 SC n
        # maxLen = 0
        # numSet = set(nums)

        # for num in nums:
        #     streak, curr = 0, num

        #     while curr in numSet:
        #         streak += 1
        #         curr += 1
            
        #     maxLen = max(maxLen, streak)
        
        # return maxLen

        #TC n SC n

        maxLen = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                
                maxLen = max(maxLen, length)
            
        
        return maxLen

    