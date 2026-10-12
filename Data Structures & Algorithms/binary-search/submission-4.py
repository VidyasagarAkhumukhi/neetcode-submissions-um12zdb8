class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            # in case of over flow: mid = l + ((r - l) // 2) || mid  =  (2 + 6) // 2 = 4 || mid = 2 + ((6 - 2) // 2) = 4
            mid = (l + r) // 2

            if target < nums[mid]:
                r =  mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        
        return -1

        # brute force
        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i
        # return -1