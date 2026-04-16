class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # in case k > n
        # Split at n-k
        left = nums[:n-k]
        right = nums[n-k:]  
        nums[:] = right + left  # modify in-place