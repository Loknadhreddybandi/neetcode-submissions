class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        left = 0
        res = [-1,-1]
        minLen = float('inf')
        count_s = {}
        count_t = {}
        have = 0
        for char in t:
            count_t[char] = 1+count_t.get(char,0)
        needed = len(count_t)
        for right in range(len(s)):
            add_char = s[right]
            count_s[add_char] = 1+ count_s.get(add_char,0)

            if add_char in count_t and count_t[add_char]==count_s[add_char]:
                have +=1
            while have == needed:
                if right - left + 1 < minLen:
                    res = [left,right]
                    minLen = right - left + 1
                count_s[s[left]]-=1
                if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                    have -=1
                left +=1
        left,right = res
        if minLen !=float('inf'):
            return s[left : right + 1]
        return ""
        