class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = sorted(nums1+nums2)
        length = len(array)
        if length%2 == 0:
            return ((array[(length-1)/2]+array[(length)/2])/2.000)
        else:
            return array[(length-1)/2]
