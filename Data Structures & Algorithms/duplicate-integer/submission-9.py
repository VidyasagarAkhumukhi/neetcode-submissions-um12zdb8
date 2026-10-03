class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dupSet = set(nums)
        # if len(dupSet) == len(nums):
        #     return False
        # return True

        # dupSet = set()

        # for num in nums:
        #     if num not in dupSet:
        #         dupSet.add(num)
        # if len(dupSet) == len(nums):
        #     return False
        # return True

        for i in range(len(nums)):
            for j in range( i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

        # time Comp = O(n)
        # space comp = O(1)