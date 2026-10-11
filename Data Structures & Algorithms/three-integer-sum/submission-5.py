class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []   
        nums.sort()

        for i, num1 in enumerate(nums):
            if num1 > 0:
                break

            if i > 0 and num1 == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num1 + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[i] == nums[ i - 1] and l < r:
                        l += 1
        
        return res