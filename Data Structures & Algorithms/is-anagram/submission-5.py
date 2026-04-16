from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dct_s = {}
        dct_t = {}
        for i in range(len(s)):
            dct_s[s[i]]= 1+dct_s.get(s[i],0)
        for i in range(len(t)):
            dct_t[t[i]]=1+dct_t.get(t[i],0)
        if dct_s == dct_t:
            return True
        return False

       
            
        
        