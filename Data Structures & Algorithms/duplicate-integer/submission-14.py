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

        # for i in range(len(nums)):
        #     for j in range( i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
                    
        # time Comp = O(n)
        # space comp = O(1)

        # sortedNums = sorted(nums)

        # for i in range(1, len(nums)):
        #     if sortedNums[i] == sortedNums[i - 1]:
        #         return True
        # return False
        # TC = O(nlogn)
        # SC = O(1) or O(n)

        dupSet = set(nums)

        if len(dupSet) == len(nums):
            return False
        return True

        # Time Comp = O(1)
        # Space Comp = O(n) , where n is the length of the input array



