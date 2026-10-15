class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1 2 3 4 5 6] = l < mid and r > mid 
        
        # [6 1 2 3 4 5] = l > mid and r > mid

        # [3 4 5 6 1 2] = l < mid and r < mid

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = l + (r - l) // 2
        #     if nums[m] < nums[r]:
        #         r = m
        #     else:
        #         l = m + 1
        # return nums[l]

        # brute force

        # mini = nums[0]

        # for num in nums:
        #     if mini > num:
        #         mini = num
        # return mini

        # return min(nums)
