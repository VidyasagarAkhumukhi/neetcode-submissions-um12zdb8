class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1 2 3 4 5 6] = l < mid and r > mid 
        
        # [6 1 2 3 4 5] = l > mid and r > mid

        # [3 4 5 6 1 2] = l < mid and r < mid

        # brute force

        # mini = nums[0]

        # for num in nums:
        #     if mini > num:
        #         mini = num
        # return mini

        return min(nums)