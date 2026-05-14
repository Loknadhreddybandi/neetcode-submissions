class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxLen = 0
        maxFreq = 0
        left =  0 
        for right in range(len(s)):
            add_char = s[right]
            freq[s[right]] = 1 + freq.get(s[right],0)
            maxFreq = max(maxFreq,freq[s[right]])

            if right - left + 1 - maxFreq >k:
                remove_char = s[left]
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left +=1
            maxLen = max(maxLen,right - left +1) 
        return maxLen       