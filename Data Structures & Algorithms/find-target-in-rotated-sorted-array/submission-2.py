class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # right sorted portion of the pile
            if nums[r] <= nums[m]:
                if target > nums[m] or target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                
            #left sorted portion of the pile
            else:
                if target < nums[m] or target > nums[l]:
                    r = m - 1
                else:
                    l = l + 1
        
        return -1
