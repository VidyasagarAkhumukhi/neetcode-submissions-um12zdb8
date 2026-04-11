class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tararr = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    tararr.insert(0, i)
                    tararr.insert(1, j)
        return tararr
