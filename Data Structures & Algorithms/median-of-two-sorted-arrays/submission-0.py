class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = nums1+nums2
        merged_nums.sort()
        n = len(merged_nums)
        if n%2==1:
            return float(merged_nums[n//2])
        else:
            median_1 = merged_nums[n//2-1]
            median_2 = merged_nums[n//2 ]
            return (median_1 + median_2)/2        