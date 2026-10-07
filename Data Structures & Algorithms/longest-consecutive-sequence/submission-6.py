class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longSet = set(nums)

        longSeq = 1 
        
        if len(longSet) == 0:
            longSeq = 0
            return longSeq

        for num in longSet:
            
            if (num - 1 and num + 1) in longSet:
                longSeq += 1
        
        return longSeq