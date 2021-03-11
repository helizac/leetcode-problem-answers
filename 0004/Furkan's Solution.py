class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l%2 == 0:
            return float(nums1[l/2]+nums1[l/2-1])/2.0
        return float(nums1[int(l/2+.5)])
