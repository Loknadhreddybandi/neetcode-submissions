class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1 
        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m
        while low<=high:
            i = (low+high)//2
            j = (m+n+1)//2-i
            if i>0:
                left1 = nums1[i-1]
            else:
                left1 = float('-inf')
            if j>0:
                left2 = nums2[j-1]
            else:
                left2 = float('-inf')
            if i<m:
                right1= nums1[i]
            else:
                right1 = float('inf')
            if j<n:
                right2 = nums2[j]
            else:
                right2 = float('inf')
            #valid is when 
            if left2<=right1 and right2>=left1:
                #get the length
                if (m+n)%2==1:
                    return float(max(left1,left2))
                else:
                    median1 = max(left1,left2)
                    median2 = min(right1,right2)
                    return (median1+median2)/2
            else:
                if left1>right2:
                    high = i-1
                else:
                    low = i+1
                    

