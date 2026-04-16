class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #edge case if empty list
        if len(nums)==0:
            return 
        final_list = [] # after pushing everything this has a length n
        for n in nums:
            final_list.append(n)
        return final_list + nums
        
        