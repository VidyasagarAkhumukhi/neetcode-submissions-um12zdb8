class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [numMap[diff, i]]
            numMap[n] = 1
        return