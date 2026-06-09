class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False       
        # TC = O(nSquare) SC= O(1)
        
        # sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False 
        # TC= O(nlogn) SC= O(1) or O(n)

        # Using hashset
        # duplicate = set()
        # for n in nums:
        #     if n in duplicate:
        #         return True
        #     duplicate.add(n)
        # return False
    
        # TC = O(n) SC= O(n)


        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        dup = set()
        for i in range(len(nums)):
            if nums[i] in dup:
                return True
            dup.add(nums[i])
        return False



        