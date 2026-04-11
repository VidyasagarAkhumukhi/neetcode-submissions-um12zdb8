class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force, TC = O(n2), SC = O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # sorting the array, TC = O(nlogn), SC = O(1)
        # nums.sort()
        # for i in range(1 , len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # using HashSet as they are unique, TC = O(n), SC = O(n)
        dupSet = set()

        for i in nums:
            if i in dupSet:
                return True
            dupSet.add(i)
        return False

