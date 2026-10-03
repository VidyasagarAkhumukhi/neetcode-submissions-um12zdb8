class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #TC = O(n2)
        #SC = O(1)

        # num1 + num2 = target
        # target + num1 = difference

        numsMap = {} # value -> index  3, 4, 5, 6 target = 7 | num1 + num2 = target | target - num1 = difference

        for i, val in enumerate(nums): 
            diff = target - val
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[val] = i
            
