class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # run binary search on  nums1 only by swapping if nums1 has more elements than nums2
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1 
        m = len(nums1) #get length of nums1
        n = len(nums2) # get length of nums2
        low = 0
        high = m
        #we only run binary search on nums1
        while low<=high:
            i = (low+high)//2    #how many elements from nums1
            j = (m+n+1)//2-i     #how many elements from nums2
            if i>0:  #its like we are taking element from nums1 into left half and that element is nums1[i-1]
                left1 = nums1[i-1]
            else:
                left1 = float('-inf')
            if j>0: #its like we are taking element from nums2 into left half and that element is nums2[j-1]
                left2 = nums2[j-1]
            else:
                left2 = float('-inf')
            if i<m: #its like we are taking element from nums1 into right half and that element is nums1[i]
                right1= nums1[i]
            else:
                right1 = float('inf')
            if j<n:  #its like we are taking element from nums2 into right half and that element is nums2[j]
    
                right2 = nums2[j]
            else:
                right2 = float('inf')
            #valid is when  all elements in left half and right half are sorted
            if left2<=right1 and right2>=left1:
                #get the length
                if (m+n)%2==1:
                    return float(max(left1,left2))
                else:
                    median1 = max(left1,left2)
                    median2 = min(right1,right2)
                    return (median1+median2)/2
            #invalid so to make valid shift pointer
            else:
                if left1>right2:
                    high = i-1
                else:
                    low = i+1
                    

