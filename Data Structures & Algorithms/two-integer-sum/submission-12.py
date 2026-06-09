class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        tarMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in tarMap:
                return [tarMap[diff], i]
            
            tarMap[num] = i