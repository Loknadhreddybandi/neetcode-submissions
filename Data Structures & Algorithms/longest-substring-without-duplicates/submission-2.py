class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = {}
        result = 0
        for right in range(len(s)):
            add_char = s[right]
            freq[add_char] = 1+freq.get(add_char,0)
            while freq[add_char]>1:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left +=1
            result = max(result,right-left+1)
        return result        