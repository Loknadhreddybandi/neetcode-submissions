#Approach
# clearly states that input may have a duplicates so we will use set
# then loop through nums and figure out if its a starting points where n-1 will not there then increase length if n+1 ...n+2..exists
#then update the longest length (we will update for different starting points ----> 3 start points we will update 3 times and compare what is longest then return this)




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if n-1 not in numSet:#its a starting number
                length = 0
                while n+length in numSet:#if n+length exists then update 
                    length +=1
                longest = max(length,longest) # compare for every starting point
        return longest

        