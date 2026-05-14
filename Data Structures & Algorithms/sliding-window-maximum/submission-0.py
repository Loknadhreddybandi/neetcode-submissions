class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = list(nums[0:k])
        result.append(max(window))
        for right in range(k,len(nums)):
            left = right - k
            window.remove(nums[left])
            window.append(nums[right])
            result.append(max(window))
        return result

        