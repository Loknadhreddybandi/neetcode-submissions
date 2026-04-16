class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left = 0
        length = -1
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            length = max(length,right-left+1)
        return length

        