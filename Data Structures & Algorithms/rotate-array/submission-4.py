class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        k = k % n  
        def reverse(left,right):
            while left<right:
                arr[left],arr[right] = arr[right],arr[left]
                left +=1
                right-=1
        reverse(0,len(arr)-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        
