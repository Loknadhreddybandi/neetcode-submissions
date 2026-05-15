#Approach
# clearly states that input may have a duplicates so we will use set
# then loop through nums and figure out if its a starting points where n-1 will not there then increase length if n+1 ...n+2..exists
#then update the longest length (we will update for different starting points ----> 3 start points we will update 3 times and compare what is longest then return this)




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in nums:
            if num -1 not in numSet: #this is starting so
                length = 1
                while length + num in numSet:
                    length +=1
                maxLen = max(maxLen,length)
        return maxLen
        
        