class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        res = nums1 + nums2

        res.sort()
        l, r = 0, len(res) - 1

        mid = ((l + r) / 2) + 1

        return mid