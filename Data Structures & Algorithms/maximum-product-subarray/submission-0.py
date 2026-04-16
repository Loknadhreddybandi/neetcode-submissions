class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]          
        
        for i in range(len(nums)):
            product = nums[i]          
            max_product = max(max_product, product)
            for j in range(i+1, len(nums)):
                product *= nums[j]     
                max_product = max(max_product, product)
        
        return max_product
        