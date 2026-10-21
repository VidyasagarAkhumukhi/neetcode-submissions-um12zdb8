class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # eg [3,4,5,6,7,1,2], target = 7  # eg [3,5,6,0,1,2], target = 4
        # eg [6,7,1,2,3,4,5], target = 1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:           
                if target > nums[mid] or nums[l] > target:
                    l = mid + 1 
                
                else:
                    r = mid - 1
            
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1

                else:
                    l = mid + 1
                 
                
        
        return -1





        
        
        # for i, num in enumerate(nums):

        #     if num == target:
        #         return i
        # return -1

